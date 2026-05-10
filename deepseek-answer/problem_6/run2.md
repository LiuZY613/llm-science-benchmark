# problem_6 / run2 — deepseek-v4-pro

- elapsed: 142.6s
- finish_reason: stop
- usage: {'prompt_tokens': 215, 'completion_tokens': 4713, 'total_tokens': 4928, 'prompt_tokens_details': {'cached_tokens': 128}, 'completion_tokens_details': {'reasoning_tokens': 4164}, 'prompt_cache_hit_tokens': 128, 'prompt_cache_miss_tokens': 87}
- content_len: 986
- reasoning_len: 6276

---

乘客1的行为决定了后续的走向。我们将原问题记为规模为 \(n\) 的问题，设 \(P_n\) 为第 \(n\) 号乘客坐到自己座位的概率。

**分析：**

- **乘客1** 以 \(\frac{1}{2}\) 的概率坐在1号座位，此时所有后续乘客都能对号入座，第 \(n\) 号乘客一定坐到自己座位。
- **乘客1** 以 \(\frac{1}{2} \times \frac{1}{n-1}\) 的概率坐在第 \(k\) 号座位（\(2 \le k \le n-1\)）。此时，乘客 \(2\) 到 \(k-1\) 都会坐自己的座位。轮到乘客 \(k\) 时，其座位已被占，他将在剩余的空座位 \(\{1, k+1, k+2, \dots, n\}\) 中等概率随机选择。这一情景等价于一个**经典的飞机座位问题**，规模为 \(n-k+1\)。已知对于规模 \(M \ge 2\) 的经典问题，最后一个乘客坐对的概率为 \(\frac{1}{2}\)。
- **乘客1** 以 \(\frac{1}{2} \times \frac{1}{n-1}\) 的概率坐在第 \(n\) 号座位，此时第 \(n\) 号乘客必然坐不到自己的座位，概率为 \(0\)。

综合以上情况，可以建立递推式：
\[
P_n = \frac{1}{2} \cdot 1 + \frac{1}{2} \cdot \frac{1}{n-1} \left( \sum_{k=2}^{n-1} \frac{1}{2} + 0 \right)
\]
求和部分有 \(n-2\) 项，因此：
\[
P_n = \frac{1}{2} + \frac{1}{2(n-1)} \cdot \frac{n-2}{2} = \frac{1}{2} + \frac{n-2}{4(n-1)}
\]
化简得：
\[
P_n = \frac{2(n-1) + (n-2)}{4(n-1)} = \frac{3n-4}{4n-4}
\]

对于 \(n = 100\)：
\[
P_{100} = \frac{3 \times 100 - 4}{4 \times 100 - 4} = \frac{296}{396} = \frac{74}{99}
\]

**答案：** \(\dfrac{74}{99}\)
