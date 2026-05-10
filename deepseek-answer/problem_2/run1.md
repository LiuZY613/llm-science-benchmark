# problem_2 / run1 — deepseek-v4-pro

- elapsed: 214.7s
- finish_reason: stop
- usage: {'prompt_tokens': 135, 'completion_tokens': 7306, 'total_tokens': 7441, 'prompt_tokens_details': {'cached_tokens': 128}, 'completion_tokens_details': {'reasoning_tokens': 6835}, 'prompt_cache_hit_tokens': 128, 'prompt_cache_miss_tokens': 7}
- content_len: 835
- reasoning_len: 9893

---

**定点坐标**：\((0, 0)\)

**推导思路**：
1. **平移坐标系**：将坐标原点平移到点 \(P\left(1, \frac{\sqrt{3}}{2}\right)\)。令 \(X = x - 1\)，\(Y = y - \frac{\sqrt{3}}{2}\)，在新坐标系下椭圆方程化为 \(X^2 + 4Y^2 + 2X + 4\sqrt{3}Y = 0\)，点 \(P\) 成为新原点 \((0,0)\)。
2. **设定弦的方程**：过 \(P\) 的两条直线在新系下为过原点的直线 \(Y = kX\)，与椭圆联立可求得另一交点 \(A', B'\) 的坐标。设弦 \(A'B'\) 的方程为 \(Y = \lambda X + \mu\)。
3. **利用斜率条件**：将 \(Y = \lambda X + \mu\) 代入椭圆方程，得到关于 \(X\) 的二次方程。两交点 \(A', B'\) 与原点连线的斜率即为方程 \(Y/X = \lambda + \mu/X\) 的两个根 \(k_1, k_2\)。由韦达定理求得 \(k_1 k_2\) 的表达式，并利用已知条件 \(k_1 k_2 = -\frac{1}{4}\) 得到 \(\lambda\) 与 \(\mu\) 的关系：\(2\mu - 2\lambda + \sqrt{3} = 0\)。
4. **求出定点**：代回直线方程得 \(Y - \frac{\sqrt{3}}{2}X = \mu(X + 1)\)，该直线系恒过定点 \((X, Y) = (-1, -\frac{\sqrt{3}}{2})\)。将定点平移回原坐标系得 \((x, y) = (0, 0)\)。
5. **结论**：直线 \(AB\) 恒过椭圆的中心 \((0, 0)\)，这也符合椭圆中“过椭圆上一点的两弦斜率之积为 \(-\frac{b^2}{a^2}\) 时，对应弦过中心”的性质。
