已知椭圆 (\frac{x^2}{4} + y^2 = 1) 和点 (P\left(1, \frac{\sqrt{3}}{2}\right))。过点 (P) 作两条直线，斜率分别为 (k_1)
  和 (k_2)，且满足 (k_1 k_2 = -\frac{1}{4})。这两条直线分别交椭圆于另一点 (A) 和 (B)。需要求直线 (AB) 所过的定点的坐标。

  推导思路：

  1. 验证点 (P) 在椭圆上：
  [
  \frac{1^2}{4} + \left(\frac{\sqrt{3}}{2}\right)^2 = \frac{1}{4} + \frac{3}{4} = 1
  ]
  点 (P) 满足椭圆方程，在椭圆上。
  2. 过点 (P) 的直线方程：
  斜率为 (k) 的直线方程为：
  [
  y - \frac{\sqrt{3}}{2} = k (x - 1)
  ]
  代入椭圆方程求交点：
  [
  \frac{x^2}{4} + \left(k(x - 1) + \frac{\sqrt{3}}{2}\right)^2 = 1
  ]
  整理得二次方程（已知 (x = 1) 是根，对应点 (P)）：
  [
  \left(\frac{1}{4} + k^2\right) x^2 + \left(-2k^2 + \sqrt{3}k\right) x + \left(k^2 - \sqrt{3}k - \frac{1}{4}\right) = 0
  ]
  3. 求另一交点横坐标：
  设另一根为 (x_A)（对应点 (A)），由韦达定理：
  [
  x_A = \frac{k^2 - \sqrt{3}k - \frac{1}{4}}{k^2 + \frac{1}{4}} = \frac{4k^2 - 4\sqrt{3}k - 1}{4k^2 + 1}
  ]
  纵坐标：
  [
  y_A = k(x_A - 1) + \frac{\sqrt{3}}{2}
  ]
  4. 利用条件 (k_1 k_2 = -\frac{1}{4})：
  设 (k_1 = k)，则 (k_2 = -\frac{1}{4k})。点 (B) 的横坐标：
  [
  x_B = \frac{\left(-\frac{1}{4k}\right)^2 - \sqrt{3}\left(-\frac{1}{4k}\right) -
  \frac{1}{4}}{\left(-\frac{1}{4k}\right)^2 + \frac{1}{4}} = \frac{-4k^2 + 4\sqrt{3}k + 1}{4k^2 + 1}
  ]
  纵坐标：
  [
  y_B = -\frac{1}{4k}(x_B - 1) + \frac{\sqrt{3}}{2}
  ]
  5. 分析点 (A) 和 (B) 的对称性：
  比较 (x_A) 和 (x_B)：
  [
  x_B = \frac{-4k^2 + 4\sqrt{3}k + 1}{4k^2 + 1} = - \left( \frac{4k^2 - 4\sqrt{3}k - 1}{4k^2 + 1} \right) = -x_A
  ]
  计算 (y_A + y_B)：
  [
  y_A + y_B = k(x_A - 1) + \frac{\sqrt{3}}{2} + \frac{1}{4k}(x_A + 1) + \frac{\sqrt{3}}{2} = x_A \left(k +
  \frac{1}{4k}\right) + \left(-k + \frac{1}{4k}\right) + \sqrt{3}
  ]
  代入 (x_A) 和化简：
  [
  y_A + y_B = \frac{4k^2 - 4\sqrt{3}k - 1}{4k^2 + 1} \cdot \frac{4k^2 + 1}{4k} + \frac{-4k^2 + 1}{4k} + \sqrt{3} =
  \frac{-4\sqrt{3}k}{4k} + \sqrt{3} = 0
  ]
  即 (y_B = -y_A)。因此，点 (B(-x_A, -y_A)) 是点 (A(x_A, y_A)) 关于原点的对称点。
  6. 直线 (AB) 过定点：
  点 (A(x_A, y_A)) 和点 (B(-x_A, -y_A)) 的连线过原点 ((0, 0))，因为：
  [
  \frac{y_A - (-y_A)}{x_A - (-x_A)} = \frac{2y

✻ Sautéed for 14m 9s