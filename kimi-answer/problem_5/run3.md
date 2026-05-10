# problem_5 / run3 — kimi-k2.6

- elapsed: 105.7s
- exit_code: 0
- turns: 1
- stop_reason: end_turn
- usage: {'input_tokens': 3960, 'cache_creation_input_tokens': 0, 'cache_read_input_tokens': 21760, 'output_tokens': 5366, 'server_tool_use': {'web_search_requests': 0, 'web_fetch_requests': 0}, 'service_tier': 'standard', 'cache_creation': {'ephemeral_1h_input_tokens': 0, 'ephemeral_5m_input_tokens': 0}, 'inference_geo': '', 'iterations': [], 'speed': 'standard'}

---

记
\[
I_n=\int_0^1\frac{1}{1+x^n}\,dx .
\]

先把它改写成
\[
I_n=1-\int_0^1\frac{x^n}{1+x^n}\,dx .
\]

对后一个积分作换元 \(x=e^{-t/n}\)（即 \(t=-n\ln x\)），则 \(x^n=e^{-t}\)，\(dx=\frac{1}{n}e^{-t/n}\,dt\)，当 \(x:0\to1\) 时 \(t:\infty\to0\)，于是
\[
\int_0^1\frac{x^n}{1+x^n}\,dx
=\frac1n\int_0^\infty\frac{e^{-t}}{1+e^{-t}}\,e^{-t/n}\,dt
=\frac1n\int_0^\infty\frac{e^{-t}}{1+e^{-t}}\left(1-\frac{t}{n}+O\!\left(\frac1{n^2}\right)\right)dt .
\]

计算零阶项：
\[
\int_0^\infty\frac{e^{-t}}{1+e^{-t}}\,dt
=\int_0^\infty\frac{1}{e^t+1}\,dt
=\Bigl[-\ln(1+e^{-t})\Bigr]_0^\infty=\ln2 .
\]

因此
\[
\int_0^1\frac{x^n}{1+x^n}\,dx
=\frac{\ln2}{n}-\frac{1}{n^2}\int_0^\infty\frac{t\,e^{-t}}{1+e^{-t}}\,dt+O\!\left(\frac1{n^3}\right).
\]

代回 \(I_n\) 的表达式得
\[
I_n-1+\frac{\ln2}{n}
=\frac{1}{n^2}\int_0^\infty\frac{t\,e^{-t}}{1+e^{-t}}\,dt+O\!\left(\frac1{n^3}\right).
\]

乘以 \(n^2\) 并令 \(n\to\infty\)，极限化为
\[
L=\int_0^\infty\frac{t}{e^t+1}\,dt .
\]

把被积函数展开为几何级数：
\[
\frac{1}{e^t+1}=\sum_{k=1}^{\infty}(-1)^{k-1}e^{-kt},
\qquad t>0,
\]
逐项积分（收敛性保证）：
\[
L=\sum_{k=1}^{\infty}(-1)^{k-1}\int_0^\infty t\,e^{-kt}\,dt
=\sum_{k=1}^{\infty}\frac{(-1)^{k-1}}{k^2}
=\eta(2),
\]
其中 \(\eta(s)\) 为 Dirichlet eta 函数。利用 \(\eta(s)=(1-2^{1-s})\zeta(s)\) 得
\[
L=(1-2^{-1})\zeta(2)=\frac12\cdot\frac{\pi^2}{6}=\frac{\pi^2}{12}.
\]

\[
\boxed{\dfrac{\pi^2}{12}}
\]
