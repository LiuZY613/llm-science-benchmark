# problem_5 / run2 — deepseek-v4-pro

- elapsed: 122.8s
- finish_reason: stop
- usage: {'prompt_tokens': 83, 'completion_tokens': 4231, 'total_tokens': 4314, 'prompt_tokens_details': {'cached_tokens': 0}, 'completion_tokens_details': {'reasoning_tokens': 3252}, 'prompt_cache_hit_tokens': 0, 'prompt_cache_miss_tokens': 83}
- content_len: 1858
- reasoning_len: 6030

---

要计算极限
\[
\lim_{n \to \infty} n^2 \left( \int_0^1 \frac{1}{1+x^n}\,\mathrm{d}x - 1 + \frac{\ln 2}{n} \right),
\]
我们先将积分写成级数形式。利用展开式 \(\frac{1}{1+x^n} = \sum_{k=0}^{\infty} (-1)^k x^{kn}\)（对 \(0\le x<1\)），并逐项积分：
\[
\int_0^1 \frac{1}{1+x^n}\,\mathrm{d}x = \sum_{k=0}^{\infty} \frac{(-1)^k}{kn+1}.
\]
令 \(a = \frac{1}{n}\)，则上式可写为
\[
I_n = a \sum_{k=0}^{\infty} \frac{(-1)^k}{k+a} = a \left( \frac{1}{a} + \sum_{k=1}^{\infty} \frac{(-1)^k}{k+a} \right).
\]
将求和中的项重新组合，使其出现 \(\ln 2\) 和更高阶项：
\[
\sum_{k=1}^{\infty} \frac{(-1)^k}{k+a} = \sum_{k=1}^{\infty} (-1)^k \left( \frac{1}{k+a} - \frac{1}{k} \right) + \sum_{k=1}^{\infty} \frac{(-1)^k}{k}.
\]
已知 \(\sum_{k=1}^{\infty} \frac{(-1)^k}{k} = -\ln 2\)。对另一部分进行渐近展开：
\[
\frac{1}{k+a} - \frac{1}{k} = -\frac{a}{k(k+a)} = -\frac{a}{k^2} + \frac{a^2}{k^3} - \frac{a^3}{k^4} + \cdots,
\]
所以
\[
\sum_{k=1}^{\infty} (-1)^k \left( \frac{1}{k+a} - \frac{1}{k} \right) = -a \sum_{k=1}^{\infty} \frac{(-1)^k}{k^2} + a^2 \sum_{k=1}^{\infty} \frac{(-1)^k}{k^3} - a^3 \sum_{k=1}^{\infty} \frac{(-1)^k}{k^4} + \cdots.
\]
利用已知级数和：
\[
\sum_{k=1}^{\infty} \frac{(-1)^k}{k^2} = -\frac{\pi^2}{12}, \qquad
\sum_{k=1}^{\infty} \frac{(-1)^k}{k^3} = -\frac{3}{4}\zeta(3),
\]
得到
\[
\sum_{k=1}^{\infty} (-1)^k \left( \frac{1}{k+a} - \frac{1}{k} \right) = \frac{\pi^2}{12}a - \frac{3}{4}\zeta(3)a^2 + O(a^3).
\]
代回 \(I_n\)：
\[
I_n = a\left( \frac{1}{a} - \ln 2 + \frac{\pi^2}{12}a - \frac{3}{4}\zeta(3)a^2 + O(a^3) \right) = 1 - \frac{\ln 2}{n} + \frac{\pi^2}{12n^2} - \frac{3\zeta(3)}{4n^3} + O\!\left(\frac{1}{n^4}\right).
\]
于是
\[
n^2 \left( I_n - 1 + \frac{\ln 2}{n} \right) = n^2 \left( \frac{\pi^2}{12n^2} - \frac{3\zeta(3)}{4n^3} + \cdots \right) = \frac{\pi^2}{12} - \frac{3\zeta(3)}{4n} + O\!\left(\frac{1}{n^2}\right).
\]
取极限 \(n \to \infty\)，所有包含 \(1/n\) 及更高阶的项趋于零，最终得到精确的封闭形式为 \(\frac{\pi^2}{12}\)。

\[
\boxed{\dfrac{\pi^2}{12}}
\]
