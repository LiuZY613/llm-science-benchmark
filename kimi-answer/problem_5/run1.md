# problem_5 / run1 — kimi-k2.6

- elapsed: 103.5s
- exit_code: 0
- turns: 1
- stop_reason: end_turn
- usage: {'input_tokens': 3960, 'cache_creation_input_tokens': 0, 'cache_read_input_tokens': 21760, 'output_tokens': 5167, 'server_tool_use': {'web_search_requests': 0, 'web_fetch_requests': 0}, 'service_tier': 'standard', 'cache_creation': {'ephemeral_1h_input_tokens': 0, 'ephemeral_5m_input_tokens': 0}, 'inference_geo': '', 'iterations': [], 'speed': 'standard'}

---

记
$$I_n=\int_0^1\frac{1}{1+x^n}\,dx.$$

先把积分改写：
$$I_n=\int_0^1\Bigl(1-\frac{x^n}{1+x^n}\Bigr)\,dx=1-J_n,\qquad 
J_n:=\int_0^1\frac{x^n}{1+x^n}\,dx.$$

于是待求极限化为
$$\lim_{n\to\infty}n^2\Bigl(I_n-1+\frac{\ln2}{n}\Bigr)
=\lim_{n\to\infty}\Bigl(n\ln2-n^2J_n\Bigr).$$

---

**对 $J_n$ 做渐近展开**

令换元 $x=e^{-t/n}$（即 $t=-n\ln x$），则 $dx=-\frac1n e^{-t/n}dt$，积分区间 $x\in[0,1]$ 对应 $t\in[0,\infty)$：

$$
J_n=\frac1n\int_0^{\infty}\frac{e^{-t}}{1+e^{-t}}\,e^{-t/n}\,dt
    =\frac1n\int_0^{\infty}\frac{e^{-t}}{1+e^{-t}}
      \Bigl(1-\frac{t}{n}+\frac{t^2}{2n^2}+O(n^{-3})\Bigr)\,dt.
$$

逐项积分：

- 首项：
  $$\int_0^{\infty}\frac{e^{-t}}{1+e^{-t}}\,dt
    =\int_0^{\infty}\frac{dt}{e^{t}+1}
    =\Bigl[\ln\frac{e^{t}}{e^{t}+1}\Bigr]_0^{\infty}=\ln2.$$

- 次项：
  $$\int_0^{\infty}\frac{t\,e^{-t}}{1+e^{-t}}\,dt
    =\int_0^{\infty}\frac{t}{e^{t}+1}\,dt.$$

  利用已知公式
  $$\int_0^{\infty}\frac{t^{s-1}}{e^{t}+1}\,dt=(1-2^{1-s})\Gamma(s)\zeta(s)\qquad(\operatorname{Re}s>0),$$
  取 $s=2$ 得
  $$\int_0^{\infty}\frac{t}{e^{t}+1}\,dt
    =(1-2^{-1})\Gamma(2)\zeta(2)
    =\frac12\cdot1\cdot\frac{\pi^{2}}{6}
    =\frac{\pi^{2}}{12}.$$

因此
$$
J_n=\frac{\ln2}{n}-\frac{1}{n^{2}}\cdot\frac{\pi^{2}}{12}+O(n^{-3}).
$$

---

**回代求极限**

$$
I_n=1-J_n
=1-\frac{\ln2}{n}+\frac{\pi^{2}}{12n^{2}}+O(n^{-3}),
$$

故
$$
n^{2}\Bigl(I_n-1+\frac{\ln2}{n}\Bigr)
=\frac{\pi^{2}}{12}+O(n^{-1})\xrightarrow[n\to\infty]{}\boxed{\frac{\pi^{2}}{12}}.
$$

---

**结果**

$$\displaystyle\lim_{n\to\infty}n^{2}\left(\int_{0}^{1}\frac{1}{1+x^{n}}\,dx-1+\frac{\ln2}{n}\right)=\frac{\pi^{2}}{12}.$$
