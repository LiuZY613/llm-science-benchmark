# problem_2 / run3 — opus (claude-opus-4-7)

- elapsed: 369.1s
- exit_code: 0
- turns: 1
- stop_reason: end_turn
- usage: {'input_tokens': 26785, 'cache_creation_input_tokens': 0, 'cache_read_input_tokens': 2048, 'output_tokens': 20834, 'server_tool_use': {'web_search_requests': 0, 'web_fetch_requests': 0}, 'service_tier': 'standard', 'cache_creation': {'ephemeral_1h_input_tokens': 0, 'ephemeral_5m_input_tokens': 0}, 'inference_geo': '', 'iterations': [], 'speed': 'standard'}

---

# 求解直线 AB 所过定点

## 答案

直线 $AB$ 恒过定点 $\boxed{\left(\dfrac{7}{4},\, -\dfrac{3\sqrt{3}}{4}\right)}$。

## 推导思路

**第一步：坐标变换简化问题**

作仿射变换 $u = \dfrac{x}{2},\ v = y$，将椭圆映射为单位圆 $u^2 + v^2 = 1$。此时：

- $P(1, \frac{\sqrt{3}}{2})$ 变为 $P'(\frac{1}{2}, \frac{\sqrt{3}}{2})$（圆上点，对应角度 $60°$）
- 斜率变为 $k' = 2k$，条件 $k_1 k_2 = -\frac{1}{4}$ 变为 $k_1' k_2' = -1$

**关键简化：两条过 $P'$ 的直线互相垂直。**

**第二步：在单位圆上求交点**

过 $P'$ 斜率为 $k$ 的直线与圆的另一交点为：

$$A' = \left(\frac{k^2 + 2\sqrt{3}k - 3}{2(1+k^2)},\ \frac{-\sqrt{3}k^2 + 2k + \sqrt{3}}{2(1+k^2)}\right)$$

斜率为 $-\frac{1}{k}$（垂直方向）的另一交点为：

$$B' = \left(\frac{k^2 - 2\sqrt{3}k - 3}{2(1+k^2)},\ \frac{\sqrt{3}k^2 + 2k - \sqrt{3}}{2(1+k^2)}\right)$$

**第三步：求 $A'B'$ 的斜率和截距**

$$m_{A'B'} = \frac{k^2+9}{-4k}, \qquad b = \frac{9\sqrt{3}-20}{8}$$

**第四步：验证定点**

取圆上直线方程 $v = \frac{k^2+9}{-4k}\,u + \frac{9\sqrt{3}-20}{8}$，代入 $(u_0, v_0) = (\frac{7}{8}, -\frac{3\sqrt{3}}{4})$，验证等式恒成立。换回原坐标即得定点 $\left(\frac{7}{4}, -\frac{3\sqrt{3}}{4}\right)$。

**几何意义：** 该定点位于椭圆在 $P$ 点的切线 $x + \sqrt{3}\,y = 2$ 上。条件 $k_1 k_2 = -\frac{b^2}{a^2} = -\frac{1}{4}$ 对应共轭方向，而共轭方向弦的包络性质决定了 $AB$ 必过此定点。
