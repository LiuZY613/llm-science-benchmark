# problem_3 / run2 — opus (claude-opus-4-7)

- elapsed: 58.3s
- exit_code: 0
- turns: 1
- stop_reason: end_turn
- usage: {'input_tokens': 5, 'cache_creation_input_tokens': 7294, 'cache_read_input_tokens': 19826, 'output_tokens': 5322, 'server_tool_use': {'web_search_requests': 0, 'web_fetch_requests': 0}, 'service_tier': 'standard', 'cache_creation': {'ephemeral_1h_input_tokens': 7294, 'ephemeral_5m_input_tokens': 0}, 'inference_geo': '', 'iterations': [{'input_tokens': 5, 'output_tokens': 5322, 'cache_read_input_tokens': 19826, 'cache_creation_input_tokens': 7294, 'cache_creation': {'ephemeral_5m_input_tokens': 0, 'ephemeral_1h_input_tokens': 7294}, 'type': 'message'}], 'speed': 'standard'}

---

# 解答

**所有解：** $(a,b) = (1,1)$ 与 $(a,b) = (2,4)$。

验证：$7^1 - 3\cdot 2^1 = 7-6 = 1$；$7^2 - 3\cdot 2^4 = 49 - 48 = 1$。

---

## 唯一性证明

将方程改写为
$$7^a - 1 = 3\cdot 2^b. \tag{$\star$}$$

### 第一步：分析 $a$ 的奇偶性（用 2 的赋值）

记 $v_2(\cdot)$ 表示 2 的赋值。由 $(\star)$ 得 $v_2(7^a-1) = b$。

- 若 $a$ 为奇数：$7^a - 1 = (7-1)(7^{a-1}+7^{a-2}+\cdots+1)$，括号内是 $a$ 个奇数之和，仍为奇数，故 $v_2(7^a-1) = v_2(6) = 1$，即 $b=1$。代回得 $7^a = 7$，故 $a=1$。
  得解 $\boxed{(1,1)}$。

- 若 $a$ 为偶数：写 $a = 2c$，将左边因式分解：
$$7^{2c}-1 = (7^c-1)(7^c+1) = 3\cdot 2^b. \tag{$\star\star$}$$

### 第二步：分析偶数情形 $a=2c$

由 $(\star\star)$，乘积 $(7^c-1)(7^c+1)$ 的素因子只有 $2$ 与 $3$，且 $3$ 仅出现一次。

**关于 3：** 因 $7\equiv 1\pmod 3$，故 $3\mid 7^c-1$，$3\nmid 7^c+1$。又 $v_3$ 在乘积中等于 $1$，故
$$v_3(7^c-1) = 1,\qquad 3\nmid 7^c+1.$$

**关于 2：** 两个相邻偶数 $7^c\pm 1$ 之最大公约数为 $2$，故其中之一恰满足 $v_2=1$。区分 $c$ 的奇偶：

**(i) $c$ 为奇数。** 此时 $7^c\equiv -1\pmod 4$，故 $v_2(7^c-1)=1$，$v_2(7^c+1)\ge 2$。

因 $7^c-1$ 在乘积里贡献了全部 $v_3$，且其素因子只能是 $2,3$，所以
$$7^c - 1 = 2\cdot 3 = 6 \;\Longrightarrow\; 7^c = 7 \;\Longrightarrow\; c=1.$$

于是 $a=2$，$7^c+1 = 8$，$b = v_2(48)=4$。
得解 $\boxed{(2,4)}$。

**(ii) $c$ 为偶数。** 此时 $7^c\equiv 1\pmod 4$，故 $v_2(7^c+1)=1$。

因 $3\nmid 7^c+1$，且 $7^c+1$ 的素因子只能是 $2,3$，又 $v_2(7^c+1)=1$，所以必须有
$$7^c + 1 = 2.$$
但 $c\ge 2$ 时 $7^c+1 \ge 50$，矛盾。故此情形无解。

### 结论

综合所有情形，方程 $7^a - 3\cdot 2^b = 1$ 的全部正整数解为
$$(a,b) = (1,1)\quad\text{和}\quad (a,b)=(2,4). \qquad\blacksquare$$
