# problem_1 / run1 — kimi-k2.6 (attempt 1/1)

- elapsed: 398.4s
- finish_reason: stop
- usage: {}
- content_len: 2043
- reasoning_len: 25344
- total_elapsed: 398.4s
- attempt: 1
- suffix_used: 
- prior_attempts: []

---

**答案**：最小值为 \(\displaystyle \frac34\)，当且仅当 \(a=b=c=1\) 时取得。

---

### 证明

记
\[
S=\frac{a^3}{(1+b)(1+c)}+\frac{b^3}{(1+c)(1+a)}+\frac{c^3}{(1+a)(1+b)}.
\]

因为 \(abc=1\)，可把每一项的分子、分母同乘以相应的 \(a,b,c\)，写成
\[
S=\frac{a^4}{a(1+b)(1+c)}+\frac{b^4}{b(1+c)(1+a)}+\frac{c^4}{c(1+a)(1+b)}.
\]

**第一步：应用 Cauchy（Engel 形式）**

\[
S\ge
\frac{(a^2+b^2+c^2)^2}
{a(1+b)(1+c)+b(1+c)(1+a)+c(1+a)(1+b)}.
\tag{1}
\]

计算分母：
\[
\begin{aligned}
&a(1+b)(1+c)+b(1+c)(1+a)+c(1+a)(1+b)  \\
&= \sum_{\text{cyc}} a(1+b+c+bc) \\
&= (a+b+c)+2(ab+bc+ca)+3abc.
\end{aligned}
\]

设
\[
p=a+b+c,\qquad q=ab+bc+ca,\qquad r=abc=1.
\]
则分母为 \(p+2q+3\)，而
\[
a^2+b^2+c^2=p^2-2q.
\]

于是 (1) 化为
\[
S\ge \frac{(p^2-2q)^2}{p+2q+3}.
\tag{2}
\]

**第二步：证明下界不小于 \(\frac34\)**

我们要证
\[
\frac{(p^2-2q)^2}{p+2q+3}\ge\frac34
\quad\Longleftrightarrow\quad
4(p^2-2q)^2\ge 3(p+2q+3).
\tag{3}
\]

令 \(s=p^2-2q=a^2+b^2+c^2\)。由熟知的不等式 \((a+b+c)^2\ge 3(ab+bc+ca)\) 得
\[
q\le\frac{p^2}{3}\quad\Longrightarrow\quad
s=p^2-2q\ge p^2-\frac{2p^2}{3}=\frac{p^2}{3}>0.
\]

把 \(q=\dfrac{p^2-s}{2}\) 代入 (3)，左边只含 \(s\)，右边只含 \(p\)：
\[
4s^2\ge 3\!\left(p+p^2-s+3\right)
\quad\Longleftrightarrow\quad
4s^2+3s-3(p^2+p+3)\ge0.
\tag{4}
\]

对固定的 \(p\)，(4) 的左端是关于 \(s\) 的开口向上的二次函数，且对称轴 \(s=-\frac38<0\)，故在 \(s>0\) 时单调递增。因此它的最小值在 \(s\) 的最小值 \(s=\dfrac{p^2}{3}\) 处取得。只需验证此时 (4) 成立：

\[
4\!\left(\frac{p^2}{3}\right)^2+3\cdot\frac{p^2}{3}-3(p^2+p+3)\ge0
\;\Longleftrightarrow\;
\frac{4p^4}{9}-2p^2-3p-9\ge0.
\]

两边同乘 9，得
\[
4p^4-18p^2-27p-81\ge0.
\]

因式分解：
\[
4p^4-18p^2-27p-81=(p-3)(4p^3+12p^2+18p+27).
\]

由 AM–GM，\(p=a+b+c\ge 3\sqrt[3]{abc}=3\)，于是 \(p-3\ge0\)，且显然 \(4p^3+12p^2+18p+27>0\)。故上式非负，(3) 得证。

**第三步：等号条件**

在 (3) 的推导中，等号成立需要同时满足：

1. \(p=3\) 且 \(s=\dfrac{p^2}{3}\)。这等价于 \(a+b+c=3\) 且 \(ab+bc+ca=3\)。在 \(abc=1\) 的条件下，由 \((a+b+c)^2=3(ab+bc+ca)\) 可知 \(a=b=c\)，于是 \(a=b=c=1\)。

2. Cauchy（Engel）不等式取等，要求
\[
\frac{a}{(1+b)(1+c)}=\frac{b}{(1+c)(1+a)}=\frac{c}{(1+a)(1+b)}.
\]
当 \(a=b=c=1\) 时，三项均为 \(\frac14\)，等号成立。

因此
\[
S_{\min}=\frac34,
\]
且仅在 \(a=b=c=1\) 时取得。

\[
\boxed{\,\min S=\dfrac34\,}
\] 

取等条件：\(\boxed{a=b=c=1}\)。
