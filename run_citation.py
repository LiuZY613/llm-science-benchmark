"""
03_citation_check benchmark runner.

CRITICAL: each run executes inside a sandbox located OUTSIDE the benchmark tree
(under %TEMP%\\bench-citation\\<model>\\run<k>\\). Sandbox contains ONLY paper.tex
(renamed from paper_buggy.tex so the filename does not leak the task). Model
cannot reach references_truth.md or answer_key.md via `..`.

Per-run artifacts:
  <model>-answer/citation/run<k>.md             summary (elapsed/usage/findings)
  <model>-answer/citation/run<k>/paper/         archived post-run sandbox
  <model>-answer/citation/run<k>/_stderr.log    claude stderr (if any)
  <model>-answer/citation/_raw/run<k>.json      raw json output

Usage:
  python run_citation.py                         # opus + deepseek + panshi100, run 1
  python run_citation.py opus                    # opus run 1
  python run_citation.py deepseek 2              # deepseek run 2 only
"""

import json
import os
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SOURCE_TEX = ROOT / "03_citation_check" / "paper_buggy.tex"
SANDBOX_ROOT = Path(tempfile.gettempdir()) / "bench-citation"

PROMPT = (
    "你将得到一篇 LaTeX 论文（关于 N-queens 问题的统计力学），路径为 `./paper.tex`。\n\n"
    "任务：作为一位严谨的学术审稿人，复核这篇论文中所有引用（`\\cite` 命令 + "
    "`thebibliography` 中的每一条 `\\bibitem`）的事实准确性和恰当性。\n\n"
    "你可以使用：\n"
    "- WebSearch / WebFetch（搜索引擎、Crossref、arXiv、Google Scholar、APS 网站等）\n"
    "- Bash / Python（可调 Crossref REST API、arXiv API 等）\n"
    "- 编辑文件、运行脚本\n\n"
    "输出要求：在当前目录下创建 `findings.md`，逐条记录每个发现的引用问题：\n"
    "- 位置（`\\cite` 所在 line 或 bibitem key）\n"
    "- 你认为存在什么问题\n"
    "- 证据（你查到的真实信息 vs 论文中的写法 + 来源 / 检索手段）\n"
    "- 修复建议（可选）\n\n"
    "注意事项：\n"
    "- 不要修改 paper.tex 本身，只在 findings.md 中记录\n"
    "- 对每条引用做独立判断；可疑就调研，不要因为大多数引用看起来正确就放过其他条目\n"
    "- 不确定的条目：说明 \"不确定 + 已用的验证手段 + 缺失的信息\"\n"
    "- 不要预设有多少处问题，可能很多，也可能很少\n"
    "- **请你直接完成所有核查工作，不要使用 Task 工具派遣 subagent。"
    "所有 WebSearch / WebFetch / Bash / Python 调用都由你本人执行。**\n"
)

CLAUDE = os.path.expandvars(r"%USERPROFILE%\.local\bin\claude.exe")

from config import DS_KEY, CST_KEY, KIMI_TOKEN, MIMO_TOKEN, get_kimi_env, get_ds_cc_env, get_mimo_env, get_panshi_env
TIMEOUT_S = 3 * 3600  # 3h ceiling per run (web search rounds can be slow)

MODELS = {
    "opus": {
        "model": "claude-opus-4-7",
        "out_dir": "opus-answer/citation",
        "env_overrides": {},
    },
    "deepseek": {
        "model": "deepseek-v4-pro[1m]",
        "out_dir": "deepseek-answer/citation",
        "env_overrides": get_ds_cc_env(),
    },
    "kimi": {
        "model": "kimi-k2.6",
        "out_dir": "kimi-answer/citation",
        "env_overrides": get_kimi_env(),
    },
    "panshi100": {
        "model": "S1-Base-Ultra",
        "out_dir": "panshi100-answer/citation",
        "env_overrides": get_panshi_env(),
    },
    "mimo": {
        "model": "mimo-v2.5-pro",
        "out_dir": "mimo-answer/citation",
        "env_overrides": get_mimo_env(),
    },
}


def safe_print(msg: str) -> None:
    try:
        sys.stdout.write(msg + "\n")
        sys.stdout.flush()
    except UnicodeEncodeError:
        sys.stdout.write(msg.encode("ascii", errors="replace").decode("ascii") + "\n")
        sys.stdout.flush()


def run_one(model_key: str, run_idx: int):
    cfg = MODELS[model_key]
    sandbox = SANDBOX_ROOT / model_key / f"run{run_idx}"
    if sandbox.exists():
        shutil.rmtree(sandbox)
    sandbox.mkdir(parents=True)
    # Copy paper_buggy.tex into sandbox AS paper.tex (filename does not leak the task)
    shutil.copy(SOURCE_TEX, sandbox / "paper.tex")

    archive_dir = ROOT / cfg["out_dir"] / f"run{run_idx}"
    if archive_dir.exists():
        shutil.rmtree(archive_dir)
    archive_dir.mkdir(parents=True)

    out_md = ROOT / cfg["out_dir"] / f"run{run_idx}.md"

    env = {
        k: v for k, v in os.environ.items()
        if not k.startswith("ANTHROPIC_")
        and k not in ("CLAUDE_CODE_SUBAGENT_MODEL", "CLAUDE_CODE_EFFORT_LEVEL")
    }
    env.update(cfg["env_overrides"])

    safe_print(f">>> {cfg['out_dir']}/run{run_idx}  model={cfg['model']}  cwd={sandbox}")
    t0 = time.time()
    timed_out = False
    try:
        proc = subprocess.run(
            [
                CLAUDE,
                "-p", PROMPT,
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
        stdout = proc.stdout
        stderr = proc.stderr
        returncode = proc.returncode
    except subprocess.TimeoutExpired as e:
        dt = time.time() - t0
        stdout = (e.stdout.decode("utf-8", errors="replace") if isinstance(e.stdout, bytes) else (e.stdout or ""))
        stderr = (e.stderr.decode("utf-8", errors="replace") if isinstance(e.stderr, bytes) else (e.stderr or ""))
        returncode = -1
        timed_out = True

    text = stdout
    meta: dict = {"exit_code": returncode}
    if timed_out:
        meta["timeout"] = TIMEOUT_S
    raw = stdout
    try:
        j = json.loads(stdout)
        text = j.get("result") or stdout
        meta["turns"] = j.get("num_turns")
        meta["stop_reason"] = j.get("stop_reason")
        meta["usage"] = j.get("usage", {})
        raw = j
    except (json.JSONDecodeError, TypeError):
        meta["parse"] = "json_decode_failed"

    if stderr:
        meta["stderr_len"] = len(stderr)
        (archive_dir / "_stderr.log").write_text(stderr, encoding="utf-8")

    findings_path = sandbox / "findings.md"
    has_findings = findings_path.exists()
    meta["findings_md"] = "yes" if has_findings else "missing"

    # Archive sandbox (paper.tex + findings.md if any) for inspection
    try:
        shutil.copytree(sandbox, archive_dir / "paper", dirs_exist_ok=True)
    except Exception as e:
        meta["archive_error"] = f"{type(e).__name__}: {e}"

    # Write summary
    lines = [
        f"# citation_check / run{run_idx} — {model_key} ({cfg['model']})",
        "",
        f"- elapsed: {dt:.1f}s",
    ]
    for k, v in meta.items():
        lines.append(f"- {k}: {v}")
    lines += ["", "---", "", "## Model final output", "", text or "(empty)"]
    if has_findings:
        try:
            lines += ["", "---", "", "## findings.md (model-authored)", "",
                      findings_path.read_text(encoding="utf-8")]
        except Exception as e:
            lines += ["", f"(findings.md exists but failed to read: {e})"]

    out_md.parent.mkdir(parents=True, exist_ok=True)
    out_md.write_text("\n".join(lines) + "\n", encoding="utf-8")

    raw_dir = ROOT / cfg["out_dir"] / "_raw"
    raw_dir.mkdir(parents=True, exist_ok=True)
    raw_payload = raw if isinstance(raw, dict) else {"stdout": stdout, "stderr": stderr}
    (raw_dir / f"run{run_idx}.json").write_text(
        json.dumps(raw_payload, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    safe_print(
        f"    done {dt:.1f}s  exit={returncode}  findings={'yes' if has_findings else 'NO'}"
    )


def main():
    args = sys.argv[1:]
    if not args:
        targets = [(m, 1) for m in ("opus", "deepseek", "panshi100")]
    elif len(args) == 1:
        targets = [(args[0], 1)]
    elif len(args) == 2:
        targets = [(args[0], int(args[1]))]
    else:
        safe_print("usage: python run_citation.py [model [run]]")
        sys.exit(2)

    for m, r in targets:
        if m not in MODELS:
            safe_print(f"unknown model: {m}")
            continue
        try:
            run_one(m, r)
        except Exception as e:
            safe_print(f"    EXCEPTION run_one({m}, {r}): {type(e).__name__}: {e}")


if __name__ == "__main__":
    main()
