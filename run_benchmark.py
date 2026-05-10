"""
Cross-model math benchmark runner.

Three harnesses:
- opus       : claude.exe -p (Claude Code, OAuth, tools enabled, per-run sandbox)
- deepseek   : HTTP /v1/chat/completions streaming (DS official OpenAI-compat)
- panshi100  : HTTP /v1/chat/completions streaming (cstcloud OpenAI-compat) —
               extracts `delta.content` separately from `delta.reasoning_content`
               to bypass the <think>-black-hole problem in the Anthropic protocol.

Per-run sandbox isolation (claude only):
  runs/opus/<stem>/run<k>/  -- contains ONLY the single problem markdown.
  No README, no other problems, no solutions/, no answers from other runs.

For HTTP harnesses, isolation is by construction (no file system access at all).

Usage:
  python run_benchmark.py <model_key>             # all 6 problems × 3 runs
  python run_benchmark.py <model_key> problem_3   # one problem × 3 runs
  python run_benchmark.py <model_key> problem_3 1 # single (problem, run) cell
"""

import json
import os
import shutil
import subprocess
import sys
import time
import urllib.request
from pathlib import Path

PROBLEMS = Path("01_math_reasoning")
RUNS_PER_PROBLEM = 3
TIMEOUT_S = 3 * 3600  # 3h ceiling per call (S1 worst case)


def safe_print(msg: str) -> None:
    """Windows console GBK can't render every Unicode char (e.g. ✓ ✗ ★).
    Strip / replace before writing so a stray emoji doesn't kill the batch."""
    try:
        sys.stdout.write(msg + "\n")
        sys.stdout.flush()
    except UnicodeEncodeError:
        sys.stdout.write(msg.encode("ascii", errors="replace").decode("ascii") + "\n")
        sys.stdout.flush()

CLAUDE = os.path.expandvars(r"%USERPROFILE%\.local\bin\claude.exe")

from config import DS_KEY, CST_KEY, KIMI_TOKEN, MIMO_TOKEN, get_kimi_env, get_ds_cc_env, get_mimo_env, get_panshi_env

MODELS = {
    "opus": {
        "harness": "claude_code",
        "model": "claude-opus-4-7",
        "out_dir": "opus-answer",
        "prompt_suffix": "",
    },
    "deepseek": {
        "harness": "openai_stream",
        "endpoint": "https://api.deepseek.com/v1/chat/completions",
        "api_key": DS_KEY,
        "model": "deepseek-v4-pro",
        "out_dir": "deepseek-answer",
        "prompt_suffix": "",
    },
    # 备用：DS 走 claude -p (Anthropic-compat)，享受 agent loop + 工具，
    # 用来抢救 HTTP 模式下 reasoning 爆掉的硬题。
    "deepseek_cc": {
        "harness": "claude_code",
        "model": "deepseek-v4-pro[1m]",
        "out_dir": "deepseek-answer",
        "sandbox_root": "runs/deepseek_cc",
        "prompt_suffix": "",
        "env_overrides": get_ds_cc_env(),
    },
    "kimi": {
        "harness": "claude_code",
        "model": "kimi-k2.6",
        "out_dir": "kimi-answer",
        "sandbox_root": "runs/kimi",
        "prompt_suffix": "",
        "env_overrides": get_kimi_env(),
    },
    "kimi_http": {
        "harness": "openai_stream",
        "endpoint": "https://api.moonshot.cn/v1/chat/completions",
        "api_key": KIMI_TOKEN,
        "model": "kimi-k2.6",
        "out_dir": "kimi-answer",
        "temperature": 1.0,
        "max_tokens": 32768,
        "extra_body": {"thinking": {"type": "enabled"}},
        "prompt_suffix": "",
    },
    "panshi100": {
        # 已实测：S1-Base-Ultra 和 S1-Base-Pro 在 HTTP 单轮模式下，硬题推理都会
        # 填满 token 预算，content 字段始终空。多种 nudge / pre-fill / 关闭推理
        # 指令均无效。这里保留单次最简调用作为基线记录，让 18 次都跑掉以诚实
        # 反映模型在该 harness 下的表现。
        "harness": "openai_stream",
        "endpoint": "https://uni-api.cstcloud.cn/v1/chat/completions",
        "api_key": CST_KEY,
        "model": "S1-Base-Ultra",
        "out_dir": "panshi100-answer",
        "retry_suffixes": [""],  # single attempt, no nudge
    },
    "mimo": {
        "harness": "claude_code",
        "model": "mimo-v2.5-pro",
        "out_dir": "mimo-answer",
        "sandbox_root": "runs/mimo",
        "prompt_suffix": "",
        "env_overrides": get_mimo_env(),
    },
}


def write_answer(out_file: Path, header: str, body: str, dt: float, meta: dict, raw):
    out_file.parent.mkdir(parents=True, exist_ok=True)
    lines = [f"# {out_file.parent.name} / {out_file.stem} — {header}", ""]
    lines.append(f"- elapsed: {dt:.1f}s")
    for k, v in meta.items():
        lines.append(f"- {k}: {v}")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append(body if body else "(empty)")
    out_file.write_text("\n".join(lines) + "\n", encoding="utf-8")
    if raw is not None:
        raw_dir = out_file.parent / "_raw"
        raw_dir.mkdir(exist_ok=True)
        (raw_dir / f"{out_file.stem}.json").write_text(
            json.dumps(raw, ensure_ascii=False, indent=2), encoding="utf-8"
        )


def run_claude_code(cfg: dict, problem_path: Path, out_file: Path, run_idx: int):
    sandbox_root = cfg.get("sandbox_root", "runs/opus")
    sandbox = Path(sandbox_root) / problem_path.stem / f"run{run_idx}"
    if sandbox.exists():
        shutil.rmtree(sandbox)
    sandbox.mkdir(parents=True)
    shutil.copy(problem_path, sandbox / problem_path.name)
    prompt = problem_path.read_text(encoding="utf-8")

    # Strip every ANTHROPIC_* var so claude.exe falls back to OAuth Max subscription
    # (or apply per-model env_overrides for third-party Anthropic-compat endpoints).
    env = {k: v for k, v in os.environ.items() if not k.startswith("ANTHROPIC_") and k != "CLAUDE_CODE_SUBAGENT_MODEL" and k != "CLAUDE_CODE_EFFORT_LEVEL"}
    env.update(cfg.get("env_overrides", {}))

    t0 = time.time()
    proc = subprocess.run(
        [
            CLAUDE,
            "-p", prompt,
            "--model", cfg["model"],
            "--permission-mode", "bypassPermissions",
            "--output-format", "json",
        ],
        cwd=sandbox,
        env=env,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        timeout=TIMEOUT_S,
    )
    dt = time.time() - t0

    text = proc.stdout
    meta = {"exit_code": proc.returncode}
    raw = proc.stdout
    try:
        j = json.loads(proc.stdout)
        text = j.get("result") or proc.stdout
        meta["turns"] = j.get("num_turns")
        meta["stop_reason"] = j.get("stop_reason")
        meta["usage"] = j.get("usage", {})
        raw = j
    except json.JSONDecodeError:
        meta["parse"] = "json_decode_failed"
    if proc.stderr:
        meta["stderr_len"] = len(proc.stderr)
        (sandbox / "_stderr.log").write_text(proc.stderr, encoding="utf-8")

    if proc.returncode != 0 or not text.strip():
        write_answer(out_file, f"{cfg['model']} FAILED (exit={proc.returncode})", text or proc.stderr[:2000], dt, meta, raw)
        return dt, "", meta
    write_answer(out_file, cfg["model"], text, dt, meta, raw)
    return dt, text, meta


def _stream_one(cfg: dict, prompt: str):
    req_body: dict = {
        "model": cfg["model"],
        "messages": [{"role": "user", "content": prompt}],
        "stream": True,
        "temperature": cfg.get("temperature", 0.7),
        "max_tokens": cfg.get("max_tokens", 65536),
    }
    # Merge any extra body params (e.g. Kimi thinking, top_p override, etc.)
    extra = cfg.get("extra_body", {})
    if extra:
        req_body.update(extra)
    body = json.dumps(req_body).encode("utf-8")
    req = urllib.request.Request(
        cfg["endpoint"],
        data=body,
        headers={
            "Authorization": f"Bearer {cfg['api_key']}",
            "Content-Type": "application/json",
            "Accept": "text/event-stream",
        },
    )
    content_parts: list[str] = []
    reasoning_parts: list[str] = []
    finish_reason = None
    usage = {}
    chunks = []
    t0 = time.time()
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT_S) as resp:
            for raw_line in resp:
                line = raw_line.decode("utf-8", errors="replace").strip()
                if not line or not line.startswith("data:"):
                    continue
                data = line[5:].strip()
                if data == "[DONE]":
                    break
                try:
                    ev = json.loads(data)
                except json.JSONDecodeError:
                    continue
                chunks.append(ev)
                choice = (ev.get("choices") or [{}])[0]
                delta = choice.get("delta") or {}
                c = delta.get("content")
                if c:
                    content_parts.append(c)
                rc = delta.get("reasoning_content")
                if rc:
                    reasoning_parts.append(rc)
                if choice.get("finish_reason"):
                    finish_reason = choice["finish_reason"]
                if ev.get("usage"):
                    usage = ev["usage"]
    except urllib.error.HTTPError as e:
        body_resp = e.read().decode("utf-8", errors="replace")[:2000]
        return time.time() - t0, "", "", {"http_status": e.code, "error": body_resp}, []
    except Exception as e:
        return time.time() - t0, "", "", {"exception": f"{type(e).__name__}: {e}"}, []
    dt = time.time() - t0
    content = "".join(content_parts)
    reasoning = "".join(reasoning_parts)
    meta = {
        "finish_reason": finish_reason,
        "usage": usage,
        "content_len": len(content),
        "reasoning_len": len(reasoning),
    }
    return dt, content, reasoning, meta, chunks


def run_openai_stream(cfg: dict, problem_path: Path, out_file: Path, run_idx: int):
    base_prompt = problem_path.read_text(encoding="utf-8")
    suffixes = cfg.get("retry_suffixes") or [cfg.get("prompt_suffix", "")]
    attempts_log = []
    total_dt = 0.0
    for attempt_idx, suffix in enumerate(suffixes, 1):
        prompt = base_prompt + suffix
        safe_print(f"    [attempt {attempt_idx}/{len(suffixes)}] suffix_len={len(suffix)}")
        dt, content, reasoning, meta, chunks = _stream_one(cfg, prompt)
        total_dt += dt
        attempts_log.append({
            "attempt": attempt_idx,
            "suffix": suffix,
            "elapsed": dt,
            "content_len": len(content),
            "reasoning_len": len(reasoning),
            "meta": meta,
        })
        if content.strip():
            # Got a non-empty answer.
            header = f"{cfg['model']} (attempt {attempt_idx}/{len(suffixes)})"
            full_meta = {
                **meta,
                "total_elapsed": f"{total_dt:.1f}s",
                "attempt": attempt_idx,
                "suffix_used": suffix.strip()[:80] + ("..." if len(suffix) > 80 else ""),
                "prior_attempts": attempts_log[:-1],
            }
            raw = {
                "chunks": chunks,
                "content": content,
                "reasoning_content": reasoning,
                "attempts_log": attempts_log,
            }
            write_answer(out_file, header, content, total_dt, full_meta, raw)
            return total_dt, content, full_meta
        safe_print(f"      empty content; retrying with stronger nudge..." if attempt_idx < len(suffixes) else "      empty content; out of attempts")

    # All attempts produced empty content.
    header = f"{cfg['model']} EMPTY after {len(suffixes)} attempts"
    write_answer(
        out_file, header, "(empty after all retries)", total_dt,
        {"all_empty": True, "attempts": attempts_log}, {"attempts_log": attempts_log},
    )
    return total_dt, "", {"all_empty": True}


def run_one(cfg: dict, problem_path: Path, run_idx: int):
    out_file = Path(cfg["out_dir"]) / problem_path.stem / f"run{run_idx}.md"
    if out_file.exists() and out_file.stat().st_size > 200:
        # already done with non-trivial content
        try:
            existing = out_file.read_text(encoding="utf-8")
            if "(empty)" not in existing.split("---")[-1]:
                print(f"skip {cfg['out_dir']}/{problem_path.stem}/run{run_idx} (exists)")
                return None
        except Exception:
            pass

    runner = {
        "claude_code": run_claude_code,
        "openai_stream": run_openai_stream,
    }[cfg["harness"]]

    safe_print(f">>> {cfg['out_dir']}/{problem_path.stem}/run{run_idx}")
    t0 = time.time()
    try:
        dt, text, meta = runner(cfg, problem_path, out_file, run_idx)
    except Exception as e:
        dt = time.time() - t0
        out_file.parent.mkdir(parents=True, exist_ok=True)
        out_file.write_text(
            f"# {problem_path.stem} run{run_idx} EXCEPTION\n\n{type(e).__name__}: {e}\n",
            encoding="utf-8",
        )
        safe_print(f"    EXCEPTION {type(e).__name__}: {e}")
        return None

    snippet = text.strip().replace("\n", " ")[:120] if text else "(empty)"
    safe_print(f"    done {dt:.1f}s len={len(text)}  | {snippet}")
    return dt, text, meta


def main():
    if len(sys.argv) < 2 or sys.argv[1] not in MODELS:
        print(f"usage: python run_benchmark.py <{'|'.join(MODELS.keys())}> [problem_stem [run_idx]]")
        sys.exit(2)
    model_key = sys.argv[1]
    cfg = MODELS[model_key]

    if len(sys.argv) >= 3:
        problems = [PROBLEMS / f"{sys.argv[2]}.md"]
    else:
        problems = sorted(PROBLEMS.glob("problem_*.md"))

    if len(sys.argv) >= 4:
        run_indices = [int(sys.argv[3])]
    else:
        run_indices = list(range(1, RUNS_PER_PROBLEM + 1))

    for p in problems:
        for k in run_indices:
            run_one(cfg, p, k)


if __name__ == "__main__":
    main()
