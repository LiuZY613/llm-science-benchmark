"""
02_code_debug benchmark runner.

CRITICAL: each run executes inside a sandbox located OUTSIDE the benchmark tree
(under %TEMP%\\bench-codedebug\\<model>\\run<k>\\) so that even with bash + read
tools the model cannot navigate via `..` to reach `solutions/code_debug/` (which
contains the reference answer key) or `02_code_debug/README.md` (which leaks
bug categories and points at the answer key).

Per-run artifacts:
  <model>-answer/code_debug/run<k>.md             summary (elapsed/usage/stdout/findings/verify)
  <model>-answer/code_debug/run<k>/buggy_project/ archived post-run sandbox (copied back after run)
  <model>-answer/code_debug/run<k>/_stderr.log    claude stderr (if any)
  <model>-answer/code_debug/run<k>/_verify_*.txt  rerun output of python main.py

Usage:
  python run_codedebug.py                # opus×3 + deepseek×3
  python run_codedebug.py opus           # opus×3
  python run_codedebug.py deepseek 2     # deepseek run2 only
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
SOURCE = ROOT / "02_code_debug" / "buggy_project"
# Sandbox lives OUTSIDE the benchmark tree to prevent answer-key leakage via `..`.
SANDBOX_ROOT = Path(tempfile.gettempdir()) / "bench-codedebug"

PROMPT = (
    "你将得到一个 Python 项目，路径为 `./buggy_project/`。它本应模拟一个被外场驱动的谐振子势中"
    "高斯波包的时间演化，并输出一张 4 子图（密度热图、能量、⟨x⟩、⟨p⟩+ 模长）。\n\n"
    "该项目当前**恰好包含 5 处 bug**，分布于不同文件，运行后结果在物理上错误"
    "（例如能量异常漂移、⟨p⟩ 与初始动量不一致、产生 ComplexWarning 等）。\n\n"
    "你的任务：\n"
    "1. 阅读 `buggy_project/` 下全部源码。\n"
    "2. 定位并修复全部 5 处 bug。\n"
    "3. 运行 `python main.py`，确保程序无 warning、无 error 完成，且输出的物理量满足下列正确性判据。\n"
    "4. 在 `buggy_project/` 下创建 `findings.md`，**逐条**记录你找到的每个 bug：所在文件:行号、bug 简述、为何错、如何改。\n\n"
    "### 正确性判据\n\n"
    "修复后运行 `python main.py`，应满足：\n"
    "- **无 warning、无 error**；\n"
    "- `Initial energy` 在 `3.6` 附近（容差 ±0.05）；\n"
    "- `Initial <x>` ≈ `2.0000`（容差 ±0.001）；\n"
    "- `Initial <p>` ≈ `1.0`（容差 ±0.01）；\n"
    "- `Final norm` 在 `1.0` 附近（容差 ±1e-3）。\n\n"
    "你可以使用任何工具（编辑文件、运行 Python、查看输出）。"
)

CLAUDE = os.path.expandvars(r"%USERPROFILE%\.local\bin\claude.exe")

from config import DS_KEY, CST_KEY, KIMI_TOKEN, MIMO_TOKEN, get_kimi_env, get_mimo_env, get_panshi_env
TIMEOUT_S = 3600  # 1h ceiling per run

MODELS = {
    "opus": {
        "model": "claude-opus-4-7",
        "out_dir": "opus-answer/code_debug",
        "env_overrides": {},
    },
    "deepseek": {
        "model": "deepseek-v4-pro[1m]",
        "out_dir": "deepseek-answer/code_debug",
        "env_overrides": {
            "ANTHROPIC_BASE_URL": "https://api.deepseek.com/anthropic",
            "ANTHROPIC_AUTH_TOKEN": DS_KEY,
            "ANTHROPIC_DEFAULT_OPUS_MODEL": "deepseek-v4-pro[1m]",
            "ANTHROPIC_DEFAULT_SONNET_MODEL": "deepseek-v4-pro[1m]",
            "ANTHROPIC_DEFAULT_HAIKU_MODEL": "deepseek-v4-flash",
            "CLAUDE_CODE_SUBAGENT_MODEL": "deepseek-v4-flash",
            "CLAUDE_CODE_EFFORT_LEVEL": "max",
        },
    },
    "kimi": {
        "model": "kimi-k2.6",
        "out_dir": "kimi-answer/code_debug",
        "env_overrides": get_kimi_env(),
    },
    "panshi100": {
        "model": "S1-Base-Ultra",
        "out_dir": "panshi100-answer/code_debug",
        "env_overrides": get_panshi_env(),
    },
    "mimo": {
        "model": "mimo-v2.5-pro",
        "out_dir": "mimo-answer/code_debug",
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
    # Execution sandbox: outside the benchmark tree, so `cd ..` cannot reach solutions/
    sandbox = SANDBOX_ROOT / model_key / f"run{run_idx}"
    if sandbox.exists():
        shutil.rmtree(sandbox)
    sandbox.mkdir(parents=True)
    shutil.copytree(SOURCE, sandbox / "buggy_project")

    # Archive destination (inside the benchmark tree, populated AFTER the run completes)
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

    findings_path = sandbox / "buggy_project" / "findings.md"
    has_findings = findings_path.exists()
    meta["findings_md"] = "yes" if has_findings else "missing"

    # Verification: re-run python main.py independently (still inside sandbox tmpdir)
    try:
        verify = subprocess.run(
            ["python", "main.py"],
            cwd=sandbox / "buggy_project",
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=300,
        )
        v_out = verify.stdout or ""
        v_err = verify.stderr or ""
        v_exit = verify.returncode
    except Exception as e:
        v_out = ""
        v_err = f"verify_exception: {type(e).__name__}: {e}"
        v_exit = -2
    meta["verify_exit"] = v_exit
    (archive_dir / "_verify_stdout.txt").write_text(v_out, encoding="utf-8")
    (archive_dir / "_verify_stderr.txt").write_text(v_err, encoding="utf-8")

    # Archive the post-run sandbox (model's edited files) into the benchmark tree for inspection
    try:
        shutil.copytree(sandbox / "buggy_project", archive_dir / "buggy_project")
    except Exception as e:
        meta["archive_error"] = f"{type(e).__name__}: {e}"

    # Write summary
    lines = [
        f"# code_debug / run{run_idx} — {model_key} ({cfg['model']})",
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
    lines += [
        "", "---", "",
        "## Verification rerun: `python main.py`",
        f"- exit_code: {v_exit}",
        "",
        "### stdout", "```", v_out or "(empty)", "```",
        "",
        "### stderr", "```", v_err or "(empty)", "```",
    ]

    out_md.parent.mkdir(parents=True, exist_ok=True)
    out_md.write_text("\n".join(lines) + "\n", encoding="utf-8")

    # Save raw json for later inspection
    raw_dir = ROOT / cfg["out_dir"] / "_raw"
    raw_dir.mkdir(parents=True, exist_ok=True)
    raw_payload = raw if isinstance(raw, dict) else {"stdout": stdout, "stderr": stderr}
    (raw_dir / f"run{run_idx}.json").write_text(
        json.dumps(raw_payload, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    safe_print(
        f"    done {dt:.1f}s  exit={returncode}  findings={'yes' if has_findings else 'NO'}  verify_exit={v_exit}"
    )


def main():
    args = sys.argv[1:]
    if not args:
        targets = [(m, r) for m in ("opus", "deepseek") for r in (1, 2, 3)]
    elif len(args) == 1:
        m = args[0]
        targets = [(m, r) for r in (1, 2, 3)]
    elif len(args) == 2:
        targets = [(args[0], int(args[1]))]
    else:
        safe_print("usage: python run_codedebug.py [model [run]]")
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
