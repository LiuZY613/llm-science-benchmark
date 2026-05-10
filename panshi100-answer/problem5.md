 为了计算极限

  $$
  \lim_{n \to \infty} n^2 \left( \int_0^1 \frac{1}{1+x^n}  dx - 1 + \frac{\ln 2}{n} \right)
  $$

  的精确封闭形式，我们首先考虑积分 ( I_n = \int_0^1 \frac{1}{1+x^n}  dx )。通过变量替换 ( t = x^n )，得到 ( I_n =
  \frac{1}{n} \int_0^1 \frac{t^{\frac{1}{n} - 1}}{1 + t}  dt )。令 ( a = \frac{1}{n} )，则 ( I_n = \frac{1}{n} J(a) )
  其中 ( J(a) = \int_0^1 \frac{t^{a-1}}{1+t}  dt )。

  利用关系式 ( J(a) + J(1-a) = \pi \csc(\pi a) ) 和渐近展开，当 ( a \to 0 )（即 ( n \to \infty )) 时，有：

  $$
  J(a) = \frac{1}{a} - \ln 2 + \frac{\pi^2}{12} a - \frac{3}{

✻ Crunched for 12m 33s