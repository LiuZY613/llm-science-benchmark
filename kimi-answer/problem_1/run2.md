# problem_1 / run2 — kimi-k2.6 (attempt 1/1)

- elapsed: 298.3s
- finish_reason: stop
- usage: {}
- content_len: 1314
- reasoning_len: 19089
- total_elapsed: 298.3s
- attempt: 1
- suffix_used: 
- prior_attempts: []

---

**最小值：** \(\displaystyle \frac34\)

**取等条件：** 当且仅当 \(a=b=c=1\) 时取得最小值。

---

### 证明

记
\[
S=\frac{a^3}{(1+b)(1+c)}+\frac{b^3}{(1+c)(1+a)}+\frac{c^3}{(1+a)(1+b)} .
\]

对每个循环项使用算术–几何平均不等式（AM–GM）：

\[
\frac{a^3}{(1+b)(1+c)}+\frac{1+b}{8}+\frac{1+c}{8}
\ge 3\sqrt[3]{\frac{a^3}{(1+b)(1+c)}\cdot\frac{1+b}{8}\cdot\frac{1+c}{8}}
=3\sqrt[3]{\frac{a^3}{64}}
=\frac{3a}{4}.
\]

同理可得

\[
\frac{b^3}{(1+c)(1+a)}+\frac{1+c}{8}+\frac{1+a}{8}\ge\frac{3b}{4},
\qquad
\frac{c^3}{(1+a)(1+b)}+\frac{1+a}{8}+\frac{1+b}{8}\ge\frac{3c}{4}.
\]

将三式相加，左边多余的常数项共出现：

\[
\frac{1}{8}\bigl[(1+b)+(1+c)+(1+c)+(1+a)+(1+a)+(1+b)\bigr]
=\frac14\bigl[(1+a)+(1+b)+(1+c)\bigr]
=\frac14(3+a+b+c).
\]

于是得到

\[
S+\frac14(3+a+b+c)\ge\frac34(a+b+c),
\]

即

\[
S\ge\frac{a+b+c}{2}-\frac34.
\]

由于 \(a,b,c>0\) 且 \(abc=1\)，由 AM–GM 有

\[
a+b+c\ge 3\sqrt[3]{abc}=3.
\]

代入上式得

\[
S\ge\frac{3}{2}-\frac34=\frac34.
\]

---

### 取等条件

在上述三个 AM–GM 不等式中，等号成立当且仅当

\[
\frac{a^3}{(1+b)(1+c)}=\frac{1+b}{8}=\frac{1+c}{8},
\quad
\frac{b^3}{(1+c)(1+a)}=\frac{1+c}{8}=\frac{1+a}{8},
\quad
\frac{c^3}{(1+a)(1+b)}=\frac{1+a}{8}=\frac{1+b}{8}.
\]

由 \(\frac{1+b}{8}=\frac{1+c}{8}\) 得 \(b=c\)，同理得 \(c=a\)，故 \(a=b=c\)。再结合约束 \(abc=1\)，得唯一解

\[
a=b=c=1.
\]

此时
\[
S=3\cdot\frac{1^3}{(1+1)(1+1)}=3\cdot\frac14=\frac34.
\]

因此，表达式的最小值为 \(\boxed{\dfrac34}\)，且仅在 \(a=b=c=1\) 时取得。
