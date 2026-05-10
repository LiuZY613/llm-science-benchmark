# problem_1 / run2 — opus (claude-opus-4-7)

- elapsed: 202.1s
- exit_code: 0
- turns: 1
- stop_reason: end_turn
- usage: {'input_tokens': 26747, 'cache_creation_input_tokens': 0, 'cache_read_input_tokens': 2048, 'output_tokens': 12506, 'server_tool_use': {'web_search_requests': 0, 'web_fetch_requests': 0}, 'service_tier': 'standard', 'cache_creation': {'ephemeral_1h_input_tokens': 0, 'ephemeral_5m_input_tokens': 0}, 'inference_geo': '', 'iterations': [], 'speed': 'standard'}

---

# 求解最小值

## 设定与展开

设 $p = a+b+c$，$q = ab+bc+ca$，$r = abc = 1$。通分后：

$$S = \frac{N}{D}, \quad D = (1+a)(1+b)(1+c) = 2+p+q$$

**分子展开**：$N = a^3(1+a) + b^3(1+b) + c^3(1+c) = s_4 + s_3$，其中 $s_k = a^k+b^k+c^k$。

利用 Newton 恒等式（$r=1$）：
- $s_3 = p^3 - 3pq + 3$
- $s_4 = p^4 - 4p^2q + 2q^2 + 4p$

得 $N = p^4 - 4p^2q + 2q^2 + p^3 - 3pq + 4p + 3$。

## 化简为多项式不等式

需证 $S \geq \tfrac{3}{4}$，即 $4N \geq 3D$，等价于：

$$\boxed{f(p,q) = 4p^4 - 16p^2q + 8q^2 + p^2 + 13p - 11q + 6 \geq 0}$$

约束条件：$p \geq 3$，$q \geq 3$（AM-GM），$p^2 \geq 3q$。

## 证明 $f \geq 0$

**关于 $q$ 的凸性**：$f = 8q^2 - (16p^2+11)q + (\cdots)$，顶点 $q_0 = p^2 - \tfrac{11}{16}$。因 $p^2/3 < q_0$（$p \geq 3$），$f$ 在可行域 $q \in [3,\, p^2/3]$ 上**单调递减**。故只需验证两端非负。

**左端点** $q = 3$：
$$f(p,3) = 4p^4 - 47p^2 + 13p - 21 = (p-3)\underbrace{(4p^3 + 12p^2 - 11p + 7)}_{>0\;\text{for}\;p\geq 3} \geq 0$$

**右端点** $q = p^2/3$：
$$f(p,\, p^2/3) = \tfrac{1}{9}(4p^4 - 30p^2 + 117p + 54)$$

代入 $p = 3+t$（$t \geq 0$）得：

$$= \frac{(t+3)(4t^3 + 36t^2 + 78t + 54)}{9}$$

对 $g(t) = 4t^3+36t^2+78t+54$：$g'(t) = 12t^2+72t+78 > 0$，且 $g(0)=54>0$，故 $g(t)>0$。

从而 $f(p, p^2/3) \geq 0$，等号仅在 $p=3$（即 $t=0$）时成立。

**结论**：$f(p,q) \geq 0$ 在整个可行域成立，等号当且仅当 $p=q=3$，即 $a=b=c=1$。

## 结果

$$\min \left[\frac{a^3}{(1+b)(1+c)} + \frac{b^3}{(1+c)(1+a)} + \frac{c^3}{(1+a)(1+b)}\right] = \boxed{\dfrac{3}{4}}$$

**取等条件**：$a = b = c = 1$。
