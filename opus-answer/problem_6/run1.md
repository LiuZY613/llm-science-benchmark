# problem_6 / run1 — opus (claude-opus-4-7)

- elapsed: 41.3s
- exit_code: 0
- turns: 1
- stop_reason: end_turn
- usage: {'input_tokens': 5, 'cache_creation_input_tokens': 7527, 'cache_read_input_tokens': 19826, 'output_tokens': 3298, 'server_tool_use': {'web_search_requests': 0, 'web_fetch_requests': 0}, 'service_tier': 'standard', 'cache_creation': {'ephemeral_1h_input_tokens': 7527, 'ephemeral_5m_input_tokens': 0}, 'inference_geo': '', 'iterations': [{'input_tokens': 5, 'output_tokens': 3298, 'cache_read_input_tokens': 19826, 'cache_creation_input_tokens': 7527, 'cache_creation': {'ephemeral_5m_input_tokens': 0, 'ephemeral_1h_input_tokens': 7527}, 'type': 'message'}], 'speed': 'standard'}

---

# 解答

设事件 $A$ = "100 号乘客坐到 100 号座位"。按 1 号乘客的选择分类讨论：

**1 号乘客的分布：**
- $P(\text{选 1 号}) = \dfrac{1}{2}$
- $P(\text{选 } j \text{ 号}) = \dfrac{1}{2} \cdot \dfrac{1}{99} = \dfrac{1}{198}$，$j=2,\dots,100$

**情形 1：** 1 号坐自己座位 → 之后所有人都坐自己的座位，$P(A) = 1$。

**情形 2：** 1 号坐 $j$ 号座位（$2 \le j \le 99$）→ 乘客 $2,\dots,j-1$ 坐自己座位；乘客 $j$ 被挤掉，从剩余 $101-j$ 个座位 $\{1, j+1, \dots, 100\}$ 中**等概率**随机选。

此时问题归约为经典"飞机座位问题"的 $m = 101-j$ 人版本（首位乘客在所有 $m$ 个座位上均匀选择）。由经典结论：最后一位坐自己座位的概率恒为 $\dfrac{1}{2}$。

**情形 3：** 1 号坐 100 号座位 → $P(A) = 0$。

**合并计算：**

$$
P(A) = \underbrace{\dfrac{1}{2} \cdot 1}_{\text{情形 1}} \;+\; \underbrace{\sum_{j=2}^{99} \dfrac{1}{198} \cdot \dfrac{1}{2}}_{\text{情形 2}} \;+\; \underbrace{\dfrac{1}{198} \cdot 0}_{\text{情形 3}}
$$

$$
= \dfrac{1}{2} + 98 \cdot \dfrac{1}{198} \cdot \dfrac{1}{2}
= \dfrac{1}{2} + \dfrac{49}{198}
= \dfrac{99}{198} + \dfrac{49}{198}
= \dfrac{148}{198}
= \boxed{\dfrac{74}{99}}
$$

**验证（$n=3$）：** 公式给出 $\frac{1}{2} + \frac{1}{4}\cdot\frac{1}{2} = \frac{5}{8}$，与直接枚举一致。✓
