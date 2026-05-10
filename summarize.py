"""
Aggregate run_benchmark.py outputs into a single comparison report.

Reads:
  opus-answer/problem_N/runK.md
  deepseek-answer/problem_N/runK.md
  panshi100-answer/problem_N/runK.md
  01_math_reasoning/problem_N.md (problem text)

Writes:
  _summary.md  — per-problem section listing each model's 3 runs with
                 elapsed time, length, and the first ~600 chars of answer.
  _summary.csv — flat table for spreadsheet review.
"""

import csv
import re
from pathlib import Path

PROBLEMS_DIR = Path("01_math_reasoning")
MODELS = ["opus", "deepseek", "panshi100"]
RUNS = [1, 2, 3]

META_LINE = re.compile(r"^- ([\w_]+):\s*(.*)$")


def parse_run(path: Path) -> dict:
    if not path.exists():
        return {"missing": True}
    text = path.read_text(encoding="utf-8")
    parts = text.split("\n---\n", 1)
    head = parts[0]
    body = parts[1] if len(parts) > 1 else ""
    meta = {}
    for line in head.splitlines():
        m = META_LINE.match(line.strip())
        if m:
            meta[m.group(1)] = m.group(2)
    body = body.strip()
    return {"meta": meta, "body": body, "is_empty": (not body) or body == "(empty)" or body == "(empty after all retries)"}


def extract_final_answer(body: str) -> str:
    """Best-effort: grab the most likely final-answer line.
    Heuristics: a line containing 'boxed', '答案', '最小值', '最大值', or the last
    non-trivial line in the body."""
    if not body:
        return "(empty)"
    lines = [l.strip() for l in body.splitlines() if l.strip()]
    keywords = ["boxed", "答案", "解为", "最小值", "最大值", "总数", "概率", "极限", "条件概率"]
    for line in lines:
        if any(k in line for k in keywords):
            # trim noise
            cleaned = line.replace("**", "").strip()
            if 4 < len(cleaned) < 250:
                return cleaned
    # Fallback: first non-trivial line
    return lines[0][:200] if lines else "(empty)"


def main():
    out_lines = ["# Math Benchmark — 三模型对比汇总", "",
                 "| 模型 | harness |",
                 "|---|---|",
                 "| opus | Claude Code (`claude -p`)，OAuth Max 订阅，工具启用 |",
                 "| deepseek | DS 官方 OpenAI 协议流式 (`api.deepseek.com/v1`)，无工具 |",
                 "| panshi100 | cstcloud OpenAI 协议流式，含 prompt nudge 让推理收敛，无工具 |",
                 "",
                 "每题每模型采样 3 次。**评分由用户对照 solutions/ 完成**。",
                 ""]

    csv_rows = [["problem", "model", "run", "missing", "is_empty", "elapsed", "content_len", "final_answer_excerpt"]]

    for problem_path in sorted(PROBLEMS_DIR.glob("problem_*.md")):
        stem = problem_path.stem
        problem_text = problem_path.read_text(encoding="utf-8").strip()
        out_lines.append(f"---\n\n## {stem}\n")
        out_lines.append("**题目**：")
        out_lines.append("")
        for line in problem_text.splitlines():
            out_lines.append(f"> {line}" if line.strip() else ">")
        out_lines.append("")

        for model in MODELS:
            out_lines.append(f"### {model}")
            out_lines.append("")
            out_lines.append("| run | 耗时 | content 长度 | 提取的最终答案行 |")
            out_lines.append("|---|---|---|---|")
            for k in RUNS:
                p = Path(f"{model}-answer") / stem / f"run{k}.md"
                info = parse_run(p)
                if info.get("missing"):
                    out_lines.append(f"| {k} | (missing) | – | – |")
                    csv_rows.append([stem, model, k, "yes", "", "", ""])
                    continue
                meta = info["meta"]
                body = info["body"]
                is_empty = info["is_empty"]
                elapsed = meta.get("elapsed", meta.get("total_elapsed", "?"))
                length = len(body)
                final_line = extract_final_answer(body)
                # markdown safe (no | inside)
                final_md = final_line.replace("|", "\\|").replace("\n", " ")
                if len(final_md) > 180:
                    final_md = final_md[:180] + "…"
                out_lines.append(f"| {k} | {elapsed} | {length} | {final_md} |")
                csv_rows.append([stem, model, k, "no", "yes" if is_empty else "no",
                                 elapsed, length, final_line[:180]])
            out_lines.append("")

            # Show full body of each run
            for k in RUNS:
                p = Path(f"{model}-answer") / stem / f"run{k}.md"
                info = parse_run(p)
                if info.get("missing"):
                    continue
                body = info["body"] or "(empty)"
                excerpt = body[:1500] + ("\n…(truncated)" if len(body) > 1500 else "")
                out_lines.append(f"<details><summary>{model} run{k} 完整回答（前 1500 字）</summary>")
                out_lines.append("")
                out_lines.append(excerpt)
                out_lines.append("")
                out_lines.append("</details>")
                out_lines.append("")
        out_lines.append("")

    Path("_summary.md").write_text("\n".join(out_lines) + "\n", encoding="utf-8")

    with open("_summary.csv", "w", newline="", encoding="utf-8-sig") as f:
        csv.writer(f).writerows(csv_rows)

    print("wrote _summary.md and _summary.csv")
    print(f"  problems: {len(list(PROBLEMS_DIR.glob('problem_*.md')))}")
    print(f"  rows in csv: {len(csv_rows) - 1}")


if __name__ == "__main__":
    main()
