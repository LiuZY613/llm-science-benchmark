# problem_2 / run3 — kimi-k2.6 (attempt 1/1)

- elapsed: 167.0s
- finish_reason: stop
- usage: {}
- content_len: 1122
- reasoning_len: 9888
- total_elapsed: 167.0s
- attempt: 1
- suffix_used: 
- prior_attempts: []

---

**定点坐标：** $\boxed{(0,\,0)}$

---

### 推导思路

设椭圆上异于 $P$ 的任一点为 $A(x_1,y_1)$，它关于原点的对称点记为 $A'(-x_1,-y_1)$。  
因为椭圆 $\dfrac{x^2}{4}+y^2=1$ 关于原点中心对称，所以 $A'$ 也在椭圆上。

1. **计算两条连线的斜率之积**

   直线 $PA$ 与 $PA'$ 的斜率分别为  
   \[
   k_{PA}=\frac{y_1-\frac{\sqrt3}{2}}{x_1-1},\qquad 
   k_{PA'}=\frac{-y_1-\frac{\sqrt3}{2}}{-x_1-1}=\frac{y_1+\frac{\sqrt3}{2}}{x_1+1}.
   \]
   于是
   \[
   k_{PA}\cdot k_{PA'}
   =\frac{y_1^2-\frac34}{x_1^2-1}.
   \]

2. **利用椭圆方程化简**

   由 $A$ 在椭圆上，有 $\dfrac{x_1^2}{4}+y_1^2=1$，即 $y_1^2=1-\dfrac{x_1^2}{4}$。代入上式得
   \[
   k_{PA}\cdot k_{PA'}
   =\frac{\left(1-\frac{x_1^2}{4}\right)-\frac34}{x_1^2-1}
   =\frac{\frac14-\frac{x_1^2}{4}}{x_1^2-1}
   =-\frac14.
   \]

   这表明：**对椭圆上任意一点 $A$，连线 $PA$ 与 $P(-A)$ 的斜率之积恒为 $-\dfrac14$。**

3. **对应题设条件**

   题目中过 $P$ 的两条直线斜率分别为 $k_1,k_2$，且 $k_1k_2=-\dfrac14$，它们与椭圆的另一交点分别为 $A,B$。  
   由于给定斜率后，过 $P$ 的直线与椭圆的第二交点唯一，上述结论说明 $B$ 必然是 $A$ 关于原点的对称点，即
   \[
   B=-A\quad\Longrightarrow\quad B(-x_1,-y_1).
   \]

4. **得到定点**

   因为 $B$ 是 $A$ 关于原点的对称点，原点 $O(0,0)$ 是线段 $AB$ 的中点，故 $A,O,B$ 三点共线。  
   因此，无论 $A$（从而 $B$）如何取值，直线 $AB$ 始终经过原点。

---

**结论：** 直线 $AB$ 恒过定点 $\boxed{(0,0)}$。
