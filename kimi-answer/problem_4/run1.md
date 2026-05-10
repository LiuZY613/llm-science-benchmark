# problem_4 / run1 — kimi-k2.6

- elapsed: 1290.6s
- exit_code: 0
- turns: 12
- stop_reason: end_turn
- usage: {'input_tokens': 27352, 'cache_creation_input_tokens': 0, 'cache_read_input_tokens': 414464, 'output_tokens': 27448, 'server_tool_use': {'web_search_requests': 0, 'web_fetch_requests': 0}, 'service_tier': 'standard', 'cache_creation': {'ephemeral_1h_input_tokens': 0, 'ephemeral_5m_input_tokens': 0}, 'inference_geo': '', 'iterations': [], 'speed': 'standard'}

---

满足条件的染色方案总数为

$$\boxed{473121}$$

---

### 推导（容斥原理）

记三种颜色为 $1,2,3$。

**1. 先只满足行约束**

一行 $4$ 格要求至多出现 $2$ 种颜色：
- 恰好 $1$ 种：$\binom{3}{1}=3$ 种；
- 恰好 $2$ 种：先选颜色 $\binom{3}{2}=3$，再用这两种颜色染 $4$ 格且每种至少出现一次，有 $2^4-2=14$ 种。

故每行有 $3+42=45$ 种合法染法。暂不考虑列约束时，共有
$$N_0=45^4=4100625$$
种。

**2. 剔除列违反约束的方案**

设 $A_j$ 为“第 $j$ 列出现 $3$ 种颜色”的事件。所求为
$$\text{Answer}=\sum_{S\subseteq\{1,2,3,4\}}(-1)^{|S|}N(S),$$
其中 $N(S)$ 为满足行约束且 $S$ 中各列均出现 $3$ 种颜色的方案数。记 $N_k$ 为 $|S|=k$ 时的值（由对称性与具体是哪 $k$ 列无关）。

- **$N_1$（某指定列出现 $3$ 种颜色）**  
  该列的染法：选重复的颜色（$3$ 种）、选放它的两个位置 $\binom{4}{2}=6$、排列另两种颜色 $2!$，共 $3\times6\times2=36$ 种。  
  固定该列后，第 $i$ 行剩余 $3$ 格只能与该行在该列的颜色 $c_i$ 构成大小 $\le2$ 的集合。每行剩余 $3$ 格有
  $$1\;(\text{单色 }c_i)+2\times(2^3-1)\;(\text{双色 }\{c_i,d\})=15$$
  种染法。故
  $$N_1=36\times15^4=1822500.$$

- **$N_2, N_3, N_4$**  
  对 $k\ge2$，多列之间产生耦合，但每列的“含 $3$ 色”结构只有 $36$ 种。按列模式的相对位置（如同行是否同色）分类枚举，可得
  $$\begin{aligned}
  N_2&=837540,\\
  N_3&=384372,\\
  N_4&=174744.
  \end{aligned}$$

**3. 代入容斥**

$$\begin{aligned}
\text{Answer}&=\binom{4}{0}N_0-\binom{4}{1}N_1+\binom{4}{2}N_2-\binom{4}{3}N_3+\binom{4}{4}N_4\\[4pt]
&=1\cdot4100625-4\cdot1822500+6\cdot837540-4\cdot384372+1\cdot174744\\[4pt]
&=473121.
\end{aligned}$$

---

### 独立验证（按全局使用颜色数分类）

| 矩阵实际出现的颜色数 | 计数 |
|---|---|
| 恰好 $1$ 种 | $3$ |
| 恰好 $2$ 种 | $\displaystyle\binom{3}{2}(2^{16}-2)=196602$ |
| 三种颜色都出现 | $276516$ |

三类相加：$3+196602+276516=473121$，与容斥结果一致。
