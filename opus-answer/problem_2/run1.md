# problem_2 / run1 — opus (claude-opus-4-7)

- elapsed: 62.7s
- exit_code: 0
- turns: 1
- stop_reason: end_turn
- usage: {'input_tokens': 5, 'cache_creation_input_tokens': 7426, 'cache_read_input_tokens': 19826, 'output_tokens': 6629, 'server_tool_use': {'web_search_requests': 0, 'web_fetch_requests': 0}, 'service_tier': 'standard', 'cache_creation': {'ephemeral_1h_input_tokens': 7426, 'ephemeral_5m_input_tokens': 0}, 'inference_geo': '', 'iterations': [{'input_tokens': 5, 'output_tokens': 6629, 'cache_read_input_tokens': 19826, 'cache_creation_input_tokens': 7426, 'cache_creation': {'ephemeral_5m_input_tokens': 0, 'ephemeral_1h_input_tokens': 7426}, 'type': 'message'}], 'speed': 'standard'}

---

# 答：直线 $AB$ 过定点 $(0,\,0)$（坐标原点）

## 推导思路

**1. 求 $A$ 的坐标关于 $k_1$ 的表达式**

设过 $P(1,\tfrac{\sqrt 3}{2})$、斜率为 $k$ 的直线为 $y=k(x-1)+\tfrac{\sqrt 3}{2}$，代入椭圆 $x^2/4+y^2=1$：

$$
(1+4k^2)x^2 + (4\sqrt 3\,k - 8k^2)x + (4k^2-4\sqrt 3\,k-1)=0
$$

$x_P=1$ 是其一根。由韦达定理 $x_P x_A=\dfrac{4k^2-4\sqrt 3\,k-1}{1+4k^2}$，故

$$
x_A(k)=\frac{4k^2-4\sqrt 3\,k-1}{1+4k^2},\qquad
y_A(k)=\frac{-4\sqrt 3\,k^2-4k+\sqrt 3}{2(1+4k^2)}.
$$

**2. 利用条件 $k_1k_2=-\tfrac14$，即 $k_2=-\dfrac{1}{4k_1}$**

把 $k\to -\dfrac{1}{4k}$ 代入上式（分子、分母同乘 $4k^2$ 化简）：

$$
x_A\!\left(-\tfrac{1}{4k}\right)=\frac{1+4\sqrt 3\,k-4k^2}{4k^2+1}=-x_A(k),
$$
$$
y_A\!\left(-\tfrac{1}{4k}\right)=\frac{4\sqrt 3\,k^2+4k-\sqrt 3}{2(4k^2+1)}=-y_A(k).
$$

**3. 结论**

因此 $B=-A$（关于原点对称），直线 $AB$ 必过原点。

$$
\boxed{\,(0,\,0)\,}
$$

**验证（取 $k_1=\tfrac12,\;k_2=-\tfrac12$）**：直接解得 $A=(-\sqrt3,-\tfrac12)$，$B=(\sqrt3,\tfrac12)$，确实关于 $O$ 对称。

> 注：条件 $k_1k_2=-\tfrac14=-\tfrac{b^2}{a^2}$ 恰为该椭圆共轭方向的斜率关系，这正是 $A,B$ 与 $O$ 共线的几何根源。
