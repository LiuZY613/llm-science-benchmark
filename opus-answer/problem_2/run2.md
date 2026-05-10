# problem_2 / run2 — opus (claude-opus-4-7)

- elapsed: 87.7s
- exit_code: 0
- turns: 1
- stop_reason: end_turn
- usage: {'input_tokens': 5, 'cache_creation_input_tokens': 7426, 'cache_read_input_tokens': 19826, 'output_tokens': 9867, 'server_tool_use': {'web_search_requests': 0, 'web_fetch_requests': 0}, 'service_tier': 'standard', 'cache_creation': {'ephemeral_1h_input_tokens': 7426, 'ephemeral_5m_input_tokens': 0}, 'inference_geo': '', 'iterations': [{'input_tokens': 5, 'output_tokens': 9867, 'cache_read_input_tokens': 19826, 'cache_creation_input_tokens': 7426, 'cache_creation': {'ephemeral_5m_input_tokens': 0, 'ephemeral_1h_input_tokens': 7426}, 'type': 'message'}], 'speed': 'standard'}

---

# 答案

**定点为坐标原点 $\boxed{(0,\,0)}$**（即椭圆中心）。

---

## 推导思路

### 关键观察

对椭圆 $\frac{x^2}{a^2}+\frac{y^2}{b^2}=1$（此处 $a^2=4,\ b^2=1$）上任两点 $P(x_0,y_0)$、$A(x_A,y_A)$，由椭圆方程相减立得

$$
\frac{x_0^2-x_A^2}{a^2}=-\frac{y_0^2-y_A^2}{b^2}.
$$

因此

$$
k_{PA}\cdot k_{P(-A)}=\frac{y_0-y_A}{x_0-x_A}\cdot\frac{y_0+y_A}{x_0+x_A}=\frac{y_0^2-y_A^2}{x_0^2-x_A^2}=-\frac{b^2}{a^2}.
$$

### 应用到本题

题目给出的斜率乘积条件恰为

$$
k_1 k_2=-\frac{1}{4}=-\frac{b^2}{a^2}.
$$

设直线 $PA$ 斜率为 $k_1$，$A$ 关于原点的对称点为 $A'=-A$（仍在椭圆上）。由上述恒等式，$k_{PA'}=-\dfrac{1}{4k_1}=k_2$。

因此过 $P$、斜率为 $k_2$ 的直线必过 $-A$，即 $B=-A$。

### 结论

$A,B$ 关于原点对称，故直线 $AB$ 永远过 **原点 $(0,0)$**。

### 验证（以 $k_1=\tfrac12,\ k_2=-\tfrac12$ 为例）

- 由 $k_1=\tfrac12$ 解得 $A=(-\sqrt3,\,-\tfrac12)$；
- 由 $k_2=-\tfrac12$ 解得 $B=(\sqrt3,\,\tfrac12)$；

恰有 $A+B=0$，直线 $AB$ 过原点。✓
