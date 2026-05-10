# problem_3 / run3 — opus (claude-opus-4-7)

- elapsed: 63.9s
- exit_code: 0
- turns: 1
- stop_reason: end_turn
- usage: {'input_tokens': 5, 'cache_creation_input_tokens': 7294, 'cache_read_input_tokens': 19826, 'output_tokens': 5914, 'server_tool_use': {'web_search_requests': 0, 'web_fetch_requests': 0}, 'service_tier': 'standard', 'cache_creation': {'ephemeral_1h_input_tokens': 7294, 'ephemeral_5m_input_tokens': 0}, 'inference_geo': '', 'iterations': [{'input_tokens': 5, 'output_tokens': 5914, 'cache_read_input_tokens': 19826, 'cache_creation_input_tokens': 7294, 'cache_creation': {'ephemeral_5m_input_tokens': 0, 'ephemeral_1h_input_tokens': 7294}, 'type': 'message'}], 'speed': 'standard'}

---

# 解答

**所有解：$(a,b) = (1,1)$ 与 $(a,b) = (2,4)$。**

验证：$7^1 - 3\cdot 2^1 = 7-6 = 1$；$7^2 - 3\cdot 2^4 = 49-48 = 1$。

下证再无其它解。方程改写为
$$
7^a - 1 = 3\cdot 2^b. \tag{$\ast$}
$$

---

## 情形一：$a$ 为奇数

由因式分解
$$
7^a - 1 = (7-1)\bigl(7^{a-1}+7^{a-2}+\cdots+7+1\bigr) = 6S,
$$
其中 $S = \sum_{i=0}^{a-1}7^i$。$S$ 是 $a$ 个奇数之和，$a$ 奇时 $S$ 也奇。

代入 $(\ast)$：$6S = 3\cdot 2^b$，即 $2S = 2^b$，故 $S = 2^{b-1}$。
$S$ 为奇数迫使 $b-1 = 0$，从而 $S=1$，于是 $a=1$，$b=1$。

---

## 情形二：$a$ 为偶数，$a = 2k$（$k\ge 1$）

$(\ast)$ 化为
$$
(7^k - 1)(7^k + 1) = 3\cdot 2^b.
$$

设 $7^k - 1 = 2u,\ 7^k + 1 = 2v$，则 $v = u+1$。两数相邻故 $\gcd(u,v)=1$，且
$$
4uv = 3\cdot 2^b \;\Longrightarrow\; uv = 3\cdot 2^{b-2} \quad (b\ge 2\text{ 自然成立，因 }k\ge1\text{ 时 }7^a-1\ge48).
$$

由 $\gcd(u,v)=1$，因子 $3$ 与所有 $2$ 的幂不能分散到二者中（否则二者必有公因子）。所以必为以下两类之一：
- $\{u,v\} = \{1,\;3\cdot 2^{b-2}\}$，或
- $\{u,v\} = \{3,\;2^{b-2}\}$。

再用 $v = u + 1$ 逐一检查：

| 情况 | 推导 | 结果 |
|---|---|---|
| $u=1,\ v=3\cdot 2^{b-2}$ | $3\cdot 2^{b-2} = 2$ | 无整数解 |
| $u=3\cdot 2^{b-2},\ v=1$ | $v>u\ge1$ 矛盾 | 无解 |
| $u=2^{b-2},\ v=3$ | $u = 2,\ 7^k - 1 = 4,\ 7^k=5$ | 无整数解 |
| $u=3,\ v=2^{b-2}$ | $v=4,\ b=4,\ 7^k=7,\ k=1$ | $(a,b)=(2,4)$ ✓ |

故偶数 $a$ 情形下唯一解为 $(2,4)$。

---

## 结论

综合两种情形，方程 $7^a - 3\cdot 2^b = 1$ 在正整数范围内的全部解为
$$
\boxed{(a,b) = (1,1)\quad\text{与}\quad (a,b) = (2,4).}
$$
