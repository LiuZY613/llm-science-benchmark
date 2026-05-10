# problem_5 / run1 — opus (claude-opus-4-7)

- elapsed: 33.7s
- exit_code: 0
- turns: 1
- stop_reason: end_turn
- usage: {'input_tokens': 5, 'cache_creation_input_tokens': 7339, 'cache_read_input_tokens': 19826, 'output_tokens': 3685, 'server_tool_use': {'web_search_requests': 0, 'web_fetch_requests': 0}, 'service_tier': 'standard', 'cache_creation': {'ephemeral_1h_input_tokens': 7339, 'ephemeral_5m_input_tokens': 0}, 'inference_geo': '', 'iterations': [{'input_tokens': 5, 'output_tokens': 3685, 'cache_read_input_tokens': 19826, 'cache_creation_input_tokens': 7339, 'cache_creation': {'ephemeral_5m_input_tokens': 0, 'ephemeral_1h_input_tokens': 7339}, 'type': 'message'}], 'speed': 'standard'}

---

# 解答

设 $I_n = \int_0^1 \frac{dx}{1+x^n}$。作代换 $u = x^n$，得

$$
I_n = \frac{1}{n}\int_0^1 \frac{u^{1/n-1}}{1+u}\,du.
$$

记 $\alpha = 1/n$，并展开 $\frac{1}{1+u} = \sum_{k\ge 0}(-1)^k u^k$，逐项积分：

$$
\int_0^1 \frac{u^{\alpha-1}}{1+u}\,du = \sum_{k=0}^\infty \frac{(-1)^k}{\alpha+k} = \frac{1}{\alpha} + f(\alpha),
\qquad f(\alpha)=\sum_{k=1}^\infty \frac{(-1)^k}{\alpha+k}.
$$

对 $f$ 在 $\alpha=0$ 处展开：

- $f(0) = \sum_{k\ge 1}\frac{(-1)^k}{k} = -\ln 2$
- $f'(0) = -\sum_{k\ge 1}\frac{(-1)^k}{k^2} = \eta(2) = \dfrac{\pi^2}{12}$
- $f''(0) = 2\sum_{k\ge 1}\frac{(-1)^k}{k^3} = -2\eta(3) = -\dfrac{3}{2}\zeta(3)$

故

$$
f(\alpha) = -\ln 2 + \frac{\pi^2}{12}\alpha - \frac{3\zeta(3)}{4}\alpha^2 + O(\alpha^3).
$$

带回 $I_n$：

$$
I_n = \alpha\left[\frac{1}{\alpha} + f(\alpha)\right] = 1 - \frac{\ln 2}{n} + \frac{\pi^2}{12 n^2} - \frac{3\zeta(3)}{4 n^3} + O\!\left(\frac{1}{n^4}\right).
$$

因此

$$
n^2\!\left(I_n - 1 + \frac{\ln 2}{n}\right) = \frac{\pi^2}{12} - \frac{3\zeta(3)}{4n} + O\!\left(\frac{1}{n^2}\right) \;\longrightarrow\; \boxed{\dfrac{\pi^2}{12}}.
$$
