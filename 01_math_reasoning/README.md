# 数学推理 Benchmark

本目录共 6 题，覆盖代数不等式、解析几何、数论、组合计数、微积分极限、概率。

- 题目难度定位：清北强基笔试 ~ Putnam 中段
- 不含证明题；所有题答案为**数值**或**显式表达式**
- 题 4、5、6 为自编（防训练集污染）

## 题目列表

| 编号 | 类型 | 文件 |
|------|------|------|
| 1 | 代数 / 不等式 | [problem_1.md](problem_1.md) |
| 2 | 解析几何 | [problem_2.md](problem_2.md) |
| 3 | 数论 | [problem_3.md](problem_3.md) |
| 4 | 组合计数（自编） | [problem_4.md](problem_4.md) |
| 5 | 微积分极限（自编） | [problem_5.md](problem_5.md) |
| 6 | 概率（自编） | [problem_6.md](problem_6.md) |

## 评测使用建议

1. 将每道题的 markdown 内容**完整复制**给被测模型（包含上下文，不要裁剪）。
2. 不提供任何提示词工程辅助（如 "let's think step by step"），以反映模型默认能力。
3. 同一题对每个模型独立采样 3 次，按多数票判定。
4. 评分见 `../solutions/math/solutions.md`。
