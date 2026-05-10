"""自动化判定脚本：对一个被测 AI 修复后的 buggy_project 运行物理判据检查。

用法：python auto_grade.py <path_to_fixed_project>

输出：是否通过 4 项物理判据，是否运行无 warning。
"""
import subprocess
import sys
import os


CRITERIA = [
    ("Initial energy", 3.6, 0.05),
    ("Initial <x>", 2.0, 0.001),
    ("Initial <p>", 1.0, 0.01),
    ("Final norm", 1.0, 1e-3),
]


def parse_value(line, key):
    # Normalize whitespace on both sides for matching
    norm_line = " ".join(line.split())
    if not norm_line.startswith(key):
        return None
    rhs = norm_line.split("=", 1)[1].strip()
    try:
        return float(rhs.split()[0])
    except (ValueError, IndexError):
        return None


def grade(project_dir):
    project_dir = os.path.abspath(project_dir)
    print(f"Running main.py in: {project_dir}")
    result = subprocess.run(
        [sys.executable, "-W", "error", "main.py"],
        cwd=project_dir, capture_output=True, text=True,
    )

    runs_clean = (result.returncode == 0)
    print(f"\n--- stdout ---\n{result.stdout}")
    if result.stderr.strip():
        print(f"--- stderr ---\n{result.stderr}")

    score_run = 1.0 if runs_clean else 0.0
    print(f"\n[Pass] python main.py without warning/error: {runs_clean}  ({score_run}/1.0)")

    # parse observables
    parsed = {}
    for line in result.stdout.splitlines():
        for key, expected, tol in CRITERIA:
            v = parse_value(line, key)
            if v is not None:
                parsed[key] = v

    score_phys = 0.0
    for key, expected, tol in CRITERIA:
        actual = parsed.get(key, None)
        ok = (actual is not None) and (abs(actual - expected) <= tol)
        delta = "n/a" if actual is None else f"{actual - expected:+.4e}"
        print(f"  {key:20s}: expected {expected:.4f} ± {tol:g}, got {actual}, "
              f"delta={delta}  {'OK' if ok else 'FAIL'}")
        if ok:
            score_phys += 1.5 / len(CRITERIA)

    print(f"\nPhysics-criterion score: {score_phys:.3f}/1.5")
    print(f"Total non-bug-listing score: {score_run + score_phys:.3f}/2.5")
    print("(Bug-listing score must be added manually from findings.md, max 7.5)")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: python auto_grade.py <path_to_fixed_project>")
        sys.exit(1)
    grade(sys.argv[1])
