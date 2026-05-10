# problem_2 / run2 — deepseek-v4-pro

- elapsed: 152.5s
- finish_reason: stop
- usage: {'prompt_tokens': 135, 'completion_tokens': 5036, 'total_tokens': 5171, 'prompt_tokens_details': {'cached_tokens': 128}, 'completion_tokens_details': {'reasoning_tokens': 4490}, 'prompt_cache_hit_tokens': 128, 'prompt_cache_miss_tokens': 7}
- content_len: 914
- reasoning_len: 6621

---

**定点坐标**：\((0,0)\)

**推导思路**：
1. 验证点 \(P(1,\frac{\sqrt{3}}{2})\) 在椭圆 \(\frac{x^2}{4}+y^2=1\) 上。
2. 平移坐标系，使 \(P\) 为新原点：令 \(X=x-1,\; Y=y-\frac{\sqrt{3}}{2}\)。代入椭圆方程化简得 \(X^2 + 4Y^2 + 2X + 4\sqrt{3}Y = 0\)。
3. 在新系下，直线 \(PA, PB\) 过原点，设其方程为 \(Y=k_1X\) 与 \(Y=k_2X\)，已知 \(k_1k_2=-\frac{1}{4}\)。
4. 设直线 \(AB\) 的方程为 \(pX+qY=1\)。结合椭圆方程，将 \(1 = pX+qY\) 代入一次项，得到关于 \(X,Y\) 的齐次方程：
   \((1+2p)X^2 + (2q+4\sqrt{3}p)XY + (4+4\sqrt{3}q)Y^2 = 0\)。
   此方程表示直线 \(OA, OB\) 的斜率 \(k = \frac{Y}{X}\) 满足 \((4+4\sqrt{3}q)k^2 + (2q+4\sqrt{3}p)k + (1+2p) = 0\)。
5. 由韦达定理，\(k_1k_2 = \frac{1+2p}{4+4\sqrt{3}q} = -\frac{1}{4}\)，解得 \(2p + \sqrt{3}q = -2\)。
6. 将 \(p = -1 - \frac{\sqrt{3}}{2}q\) 代入直线方程 \(pX+qY=1\)，整理得 \(-X + q(Y-\frac{\sqrt{3}}{2}X) = 1\)。该方程对任意 \(q\) 恒成立当且仅当 \(X=-1,\; Y=-\frac{\sqrt{3}}{2}\)。即在新系下直线 \(AB\) 恒过点 \((-1, -\frac{\sqrt{3}}{2})\)。
7. 平移回原坐标系：\(x = X+1 = 0,\; y = Y+\frac{\sqrt{3}}{2} = 0\)，故直线 \(AB\) 恒过定点 \((0,0)\)。
