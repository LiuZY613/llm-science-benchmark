# problem_5 / run2 — opus (claude-opus-4-7)

- elapsed: 30.0s
- exit_code: 0
- turns: 1
- stop_reason: end_turn
- usage: {'input_tokens': 5, 'cache_creation_input_tokens': 7339, 'cache_read_input_tokens': 19826, 'output_tokens': 3149, 'server_tool_use': {'web_search_requests': 0, 'web_fetch_requests': 0}, 'service_tier': 'standard', 'cache_creation': {'ephemeral_1h_input_tokens': 7339, 'ephemeral_5m_input_tokens': 0}, 'inference_geo': '', 'iterations': [{'input_tokens': 5, 'output_tokens': 3149, 'cache_read_input_tokens': 19826, 'cache_creation_input_tokens': 7339, 'cache_creation': {'ephemeral_5m_input_tokens': 0, 'ephemeral_1h_input_tokens': 7339}, 'type': 'message'}], 'speed': 'standard'}

---

# 解答

设 $I_n = \displaystyle\int_0^1 \frac{1}{1+x^n}\,dx$。考虑

$$1 - I_n = \int_0^1 \frac{x^n}{1+x^n}\,dx.$$

作代换 $t = x^n$，即 $x = t^{1/n}$，$dx = \frac{1}{n}t^{1/n-1}\,dt$：

$$1 - I_n = \frac{1}{n}\int_0^1 \frac{t^{1/n}}{1+t}\,dt.$$

记 $\epsilon = 1/n$，定义 $J(\epsilon) = \displaystyle\int_0^1 \frac{t^{\epsilon}}{1+t}\,dt$。在 $\epsilon=0$ 处展开：

$$J(\epsilon) = J(0) + \epsilon J'(0) + O(\epsilon^2),$$

其中

- $J(0) = \displaystyle\int_0^1 \frac{dt}{1+t} = \ln 2$,
- $J'(0) = \displaystyle\int_0^1 \frac{\ln t}{1+t}\,dt = -\frac{\pi^2}{12}$.

（最后一式由 $\sum_{k\ge 0}(-1)^k \int_0^1 t^k\ln t\,dt = -\sum_{k\ge 0}\frac{(-1)^k}{(k+1)^2} = -\eta(2) = -\frac{\pi^2}{12}$ 得到。）

因此

$$1 - I_n \;=\; \frac{1}{n}\!\left(\ln 2 - \frac{\pi^2}{12n} + O\!\left(\tfrac{1}{n^2}\right)\right) \;=\; \frac{\ln 2}{n} - \frac{\pi^2}{12n^2} + O\!\left(\tfrac{1}{n^3}\right),$$

进而

$$I_n - 1 + \frac{\ln 2}{n} = \frac{\pi^2}{12n^2} + O\!\left(\tfrac{1}{n^3}\right).$$

# 极限值

$$\boxed{\,\dfrac{\pi^2}{12}\,}.$$
