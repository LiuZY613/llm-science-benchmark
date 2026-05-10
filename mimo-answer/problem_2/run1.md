# problem_2 / run1 — opus (claude-opus-4-7)

- elapsed: 630.7s
- exit_code: 0
- turns: 2
- stop_reason: end_turn
- usage: {'input_tokens': 31618, 'cache_creation_input_tokens': 0, 'cache_read_input_tokens': 57664, 'output_tokens': 40206, 'server_tool_use': {'web_search_requests': 0, 'web_fetch_requests': 0}, 'service_tier': 'standard', 'cache_creation': {'ephemeral_1h_input_tokens': 0, 'ephemeral_5m_input_tokens': 0}, 'inference_geo': '', 'iterations': [], 'speed': 'standard'}

---

No Python available, but the algebra verifies cleanly by hand. Here's the complete solution:

---

## 解答

**定点坐标为 $(0,\, 0)$（原点）。**

### 推导过程

**1. 设直线方程**

过 $P(1, \frac{\sqrt3}{2})$ 作斜率为 $k$ 的直线，代入椭圆方程 $\frac{x^2}{4} + y^2 = 1$：

$$
\frac{x^2}{4} + \left[k(x-1) + \frac{\sqrt3}{2}\right]^2 = 1
$$

整理为关于 $x$ 的二次方程（乘以4）：

$$
(1+4k^2)\,x^2 + 4k(\sqrt3 - 2k)\,x + (4k^2 - 4\sqrt3\,k - 1) = 0
$$

**2. 求另一交点坐标**

已知 $x=1$ 是一个根（对应点 $P$），由韦达定理得另一交点 $A$ 的坐标：

$$
x_A = \frac{4k^2 - 4\sqrt3\,k - 1}{1 + 4k^2}, \quad y_A = \frac{-2\sqrt3\,k^2 - 2k + \frac{\sqrt3}{2}}{1 + 4k^2}
$$

**3. 利用条件 $k_1 k_2 = -\frac{1}{4}$**

设 $k_1 = k$，$k_2 = m = -\frac{1}{4k}$。将 $m$ 代入上述公式求 $B$ 的坐标：

$$
x_B = \frac{4m^2 - 4\sqrt3\,m - 1}{1 + 4m^2}
$$

计算分子：$4m^2 - 4\sqrt3\,m - 1 = \frac{1}{4k^2} + \frac{\sqrt3}{k} - 1 = \frac{1 + 4\sqrt3\,k - 4k^2}{4k^2}$

分母：$1 + 4m^2 = \frac{4k^2 + 1}{4k^2}$

因此：

$$
x_B = \frac{1 + 4\sqrt3\,k - 4k^2}{1 + 4k^2}
$$

类似地：

$$
y_B = \frac{4\sqrt3\,k^2 + 4k - \sqrt3}{2(1 + 4k^2)}
$$

**4. 关键发现——对称性**

直接相加：

$$
x_A + x_B = \frac{(4k^2 - 4\sqrt3k - 1) + (1 + 4\sqrt3k - 4k^2)}{1 + 4k^2} = 0
$$

$$
y_A + y_B = \frac{(-4\sqrt3k^2 - 4k + \sqrt3) + (4\sqrt3k^2 + 4k - \sqrt3)}{2(1+4k^2)} = 0
$$

即 **$B = -A$**（$B$ 是 $A$ 关于原点的对称点）。

**5. 结论**

$A$ 和 $B$ 关于椭圆中心（原点）对称，因此直线 $AB$ 必过原点。

> 注：条件 $k_1 k_2 = -\frac{b^2}{a^2} = -\frac{1}{4}$ 正是椭圆共轭直径的条件。共轭直径的一个基本性质是：对同一点 $P$，两共轭方向与椭圆的另一交点关于中心对称，从而连线过中心。
