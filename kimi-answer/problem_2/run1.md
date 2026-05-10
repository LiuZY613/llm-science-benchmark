# problem_2 / run1 — kimi-k2.6 (attempt 1/1)

- elapsed: 467.2s
- finish_reason: stop
- usage: {}
- content_len: 1665
- reasoning_len: 37308
- total_elapsed: 467.2s
- attempt: 1
- suffix_used: 
- prior_attempts: []

---

**定点坐标**：\(\displaystyle (0,\,0)\)

---

### 推导思路（参数法）

1. **参数化椭圆**  
   设椭圆的参数方程为  
   \[
   x=2\cos\theta,\qquad y=\sin\theta .
   \]
   则点 \(P\!\left(1,\dfrac{\sqrt3}{2}\right)\) 对应的参数为 \(\theta_0=\dfrac{\pi}{3}\)。  
   设另外两交点分别为  
   \[
   A(2\cos\theta_1,\sin\theta_1),\qquad B(2\cos\theta_2,\sin\theta_2).
   \]

2. **用和差化积求斜率**  
   对任意两点 \(\theta,\theta_0\)（\(\theta\neq\theta_0\)），有  
   \[
   \frac{\sin\theta-\sin\theta_0}{\cos\theta-\cos\theta_0}
   =\frac{2\cos\frac{\theta+\theta_0}{2}\sin\frac{\theta-\theta_0}{2}}
          {-2\sin\frac{\theta+\theta_0}{2}\sin\frac{\theta-\theta_0}{2}}
   =-\cot\frac{\theta+\theta_0}{2}.
   \]
   因此
   \[
   k_{PA}=-\frac12\cot\frac{\theta_1+\theta_0}{2},\qquad
   k_{PB}=-\frac12\cot\frac{\theta_2+\theta_0}{2}.
   \]

3. **利用条件 \(k_1k_2=-\dfrac14\)**  
   \[
   k_{PA}\cdot k_{PB}
   =\frac14\cot\frac{\theta_1+\theta_0}{2}\cot\frac{\theta_2+\theta_0}{2}
   =-\frac14.
   \]
   化简得
   \[
   \cot\frac{\theta_1+\theta_0}{2}\cot\frac{\theta_2+\theta_0}{2}=-1
   \;\Longleftrightarrow\;
   \tan\frac{\theta_1+\theta_0}{2}\tan\frac{\theta_2+\theta_0}{2}=-1.
   \]
   这说明
   \[
   \frac{\theta_1+\theta_0}{2}=\frac{\theta_2+\theta_0}{2}+\frac{\pi}{2}+n\pi
   \quad(n\in\mathbb Z),
   \]
   即
   \[
   \theta_1=\theta_2+\pi\pmod{2\pi}.
   \]

4. **得出对称关系**  
   参数相差 \(\pi\) 意味着
   \[
   (2\cos\theta_2,\sin\theta_2)=(-2\cos\theta_1,-\sin\theta_1),
   \]
   故 \(B=-A\)，两点关于原点中心对称。于是直线 \(AB\) 必经过原点。

---

**结论**：无论 \(k_1,k_2\) 如何变化（只要满足 \(k_1k_2=-\dfrac14\)），直线 \(AB\) 恒过定点 **\((0,0)\)**。  

（事实上，对椭圆 \(\dfrac{x^2}{a^2}+\dfrac{y^2}{b^2}=1\) 上任意一点，只要两弦斜率之积为 \(-\dfrac{b^2}{a^2}\)，则另外两交点必关于中心对称。本题中 \(a^2=4,\;b^2=1\)。）
