# 引用核查报告：Statistical mechanics of the $N$-queens problem

## 核查方法
- WebSearch / WebFetch（搜索引擎、Crossref、arXiv、期刊官网）
- Crossref REST API（通过 Bash curl 调用）
- arXiv API / 官网（arxiv.org/abs/...）

---

## 确认存在问题的引用

### 1. `\bibitem{Metropolis1953}` — 年份错误
**位置：** `thebibliography` 第 991–995 行（`\bibitem{Metropolis1953}`）

**论文中的写法：**
> N. Metropolis, A. W. Rosenbluth, M. N. Rosenbluth, A. H. Teller, and E. Teller, Equation of state calculations by fast computing machines, J. Chem. Phys. **21**, 1087 (**1955**).

**查到的真实信息：**
- 该经典论文发表于 **1953** 年，而非 1955 年。
- 正确引用：*J. Chem. Phys.* **21**, 1087 (1953). DOI: 10.1063/1.1699114
- 这是 MCMC（Metropolis 算法）的奠基论文，广泛收录于各类数据库，年份明确为 1953。

**证据来源：**
- WebSearch 确认 "Equation of state calculations by fast computing machines" 发表于 J. Chem. Phys. **21**, 1087 (**1953**)。
- 美国物理联合会（AIP）官方记录。

**修复建议：** 将 `(1955)` 改为 `(1953)`。

---

### 2. `\bibitem{Frowis2010}` — 期刊卷号错误
**位置：** `thebibliography` 第 1017–1021 行（`\bibitem{Frowis2010}`）

**论文中的写法：**
> F. Fr\"owis, V. Nebendahl, and W. D\"ur, Tensor operators: Constructions and applications for long-range interaction systems, Phys. Rev. A **82**, 062337 (2010).

**查到的真实信息：**
- 该论文实际发表于 *Physical Review A* **81**, 062337 (2010)。
- DOI: 10.1103/PhysRevA.81.062337
- arXiv 与 APS 官网均显示卷号为 **81**，而非 82。

**证据来源：**
- WebSearch 结果直接指出 "The paper was actually published in Physical Review A, volume **81**, not 82"。
- APS 官网记录：Phys. Rev. A **81**, 062337 (2010)。

**修复建议：** 将 `\textbf{82}` 改为 `\textbf{81}`。

---

### 3. `\bibitem{Boyd2024}` — 论文疑似不存在
**位置：** `thebibliography` 第 953–956 行（`\bibitem{Boyd2024}`）

**论文中的写法：**
> A. Agrawal and S. Boyd, Convex programming for entropy bounds in combinatorial constants, SIAM Rev. **66**, 312 (2024).

**查到的真实信息：**
- 通过 WebSearch、Crossref、Google Scholar 等多渠道搜索，**均未找到**该标题、作者组合、期刊、年份的论文。
- Akshay Agrawal 与 Stephen Boyd 确有大量合作（如 Disciplined Geometric Programming、Differentiable Convex Optimization Layers 等），但 **无此标题的论文**。
- SIAM Review 2024 年卷 66 的目录中亦未检索到该文。
- 最接近的相关工作是 Nobel、Agrawal、Boyd 合著的 *Computing Tighter Bounds on the n-Queens Constant via Newton's Method* (Optim. Lett. 2023)。

**证据来源：**
- WebSearch: "I could not find a specific paper with the exact title 'Convex programming for entropy bounds in combinatorial constants' published in SIAM Review in 2024."
- Stanford Boyd 组论文列表 (stanford.edu/~boyd/papers.html) 无此记录。

**修复建议：**
- 若作者本意是引用 **Nobel, Agrawal, Boyd (2023)** 的 n-queens constant 工作，则应改为该文；
- 若确有此预印本/在审稿件，建议提供 arXiv 号或 DOI 以核实。

---

### 4. `\bibitem{Tanaka2023}` — 论文疑似不存在
**位置：** `thebibliography` 第 1039–1042 行（`\bibitem{Tanaka2023}`）

**论文中的写法：**
> H. Tanaka and K. Yamada, Tensor network methods for combinatorial counting, Phys. Rev. Research **5**, 023115 (2023).

**查到的真实信息：**
- 通过 WebSearch、Crossref、APS 官网搜索，**均未找到**作者为 "H. Tanaka" 与 "K. Yamada"、发表于 *Physical Review Research* **5**, 023115 (2023) 的论文。
- *Phys. Rev. Research* 5, 023115 (2023) 这一编号无法对应到已发表的论文。
- 相关领域最接近的论文是：
  - Kourtis et al., *Fast counting with tensor networks*, SciPost Phys. **7**, 060 (2019) [arXiv:1805.00475]
  - Wang et al., *Counting the number of solutions in satisfiability problems with tensor-network message passing*, Phys. Rev. E **110**, 034126 (2024)
  - Nakada, Tanahashi, Tanaka, *Quick design of feasible tensor networks for constrained combinatorial optimization*, Quantum **9**, 1799 (2025) [arXiv:2409.01699]

**证据来源：**
- WebSearch: "the exact paper you described does not appear to exist with those specific author names and citation details."
- APS 期刊数据库无此记录。

**修复建议：**
- 核实是否为 **Kourtis et al. (2019)** 或其他已知论文的误写；
- 或提供 arXiv 号 / DOI 进一步确认。

---

### 5. `\bibitem{Verstraete2022}` — 论文疑似不存在
**位置：** `thebibliography` 第 1023–1026 行（`\bibitem{Verstraete2022}`）

**论文中的写法：**
> F. Verstraete, Renormalization of constraint tensor networks, Adv. Phys.: X **7**, 2098453 (2022).

**查到的真实信息：**
- 通过 WebSearch、Taylor & Francis（Advances in Physics: X 出版商）、arXiv 等多渠道搜索，**均未找到**该标题、该作者单独署名、发表于 *Advances in Physics: X* **7**, 2098453 (2022) 的论文。
- Frank Verstraete 最著名的综述是 **Verstraete, Murg & Cirac (2008)**：*Matrix product states, projected entangled pair states, and variational renormalization group methods for quantum spin systems*, Advances in Physics **57**, 143 (2008)。
- 2022 年 Verstraete 参与的合作论文（如 Vanderstraeten  et al., Phys. Rev. B 105, 195140 (2022)）均非该标题，亦非单独署名。

**证据来源：**
- WebSearch: "There does not appear to be a 2022 paper by Verstraete with the exact title 'Renormalization of constraint tensor networks' published in Advances in Physics X."
- Taylor & Francis Online 无此记录。

**修复建议：**
- 若本意引用 Verstraete 的经典综述，应为 **Verstraete, Murg & Cirac, Adv. Phys. 57, 143 (2008)**；
- 若引用其他近期预印本，请提供 arXiv 号核实。

---

### 6. `\bibitem{Reynolds2019}` — 论文疑似不存在
**位置：** `thebibliography` 第 980–983 行（`\bibitem{Reynolds2019}`）

**论文中的写法：**
> J. M. Reynolds and S. T. Park, Spin-glass formulation of the N-queens problem, Comput. Phys. Commun. **241**, 38–47 (2019).

**查到的真实信息：**
- 通过 WebSearch、Crossref API、Google Scholar、Elsevier (Computer Physics Communications) 官网等多渠道搜索，**均未找到**作者为 "J. M. Reynolds" 与 "S. T. Park"、标题为 "Spin-glass formulation of the N-queens problem"、发表于 *Computer Physics Communications* **241**, 38–47 (2019) 的论文。
- Crossref 以 "Reynolds" + "Park" + 2019 为条件检索，返回结果中无此文。
- 2019 年 *Computer Physics Communications* 第 241 卷确实存在，但无法对应到该作者与标题。

**证据来源：**
- WebSearch: "the search results do not show a paper by 'Reynolds Park' about N-queens in Computer Physics Communications 241, 38 (2019)."
- Crossref API 检索无匹配。

**修复建议：**
- 核实该引用的真实来源；若为预印本，请提供 arXiv 号；
- 或替换为已确认的相关文献（如 Zhang & Ma 2009、Polson & Sokolov 2024 等关于 N-queens 的统计力学 / 蒙特卡洛工作）。

---

## 需要作者注意的引用（潜在不一致）

### 7. `\bibitem{Simkin2022}` — Bibitem key 与期刊发表年份不一致
**位置：** `thebibliography` 第 933–936 行（`\bibitem{Simkin2022}`）

**论文中的写法：**
> M. Simkin, The number of $n$-queens configurations, Adv. Math. **427**, 109127 (**2023**).

**正文引用：** `\cite{Simkin2022}`（第 78 行等）

**查到的真实信息：**
- arXiv 预印本：arXiv:2107.13460 [math.CO] (2021)
- 期刊正式发表：*Advances in Mathematics* **427**, 109127 (2023)

**说明：**
- Bibitem key 为 `Simkin2022`，但期刊发表年份是 **2023**，arXiv 预印本年份是 **2021**。
- 这在 LaTeX 中 **不是严格错误**（bibitem key 仅为标签），但会给读者造成混淆：正文提到 "Simkin~\cite{Simkin2022} proved..."，而 bibitem 中实际年份为 2023。
- 若作者本意是将该工作标记为 2022 年（可能当时引用的是 arXiv v2 或新闻报道年份），建议统一为期刊发表年份 2023，或改用 `Simkin2023` 作为 key。

**修复建议：** 将 `\bibitem{Simkin2022}` 改为 `\bibitem{Simkin2023}`，并同步修改正文中所有 `\cite{Simkin2022}`。

---

### 8. `\bibitem{Bowtell2023}` — 仅 arXiv 预印本，未见正式发表
**位置：** `thebibliography` 第 938–941 行（`\bibitem{Bowtell2023}`）

**论文中的写法：**
> C. Bowtell and P. Keevash, The $n$-queens problem, arXiv:2109.08083 (**2021**).

**正文引用：** `\cite{Bowtell2023}`（第 81 行）

**查到的真实信息：**
- arXiv:2109.08083，提交日期：**2021 年 9 月 16 日**。
- 截至核查日期（2026/05/10），WebSearch 与 arXiv 页面均 **未显示该论文已在同行评审期刊正式发表**。

**说明：**
- Bibitem key 为 `Bowtell2023`，但 bibitem 内年份写的是 2021，且该文目前仅为 arXiv 预印本。
- 若该论文截至投稿时仍未正式发表，建议将引用方式统一为 arXiv 预印本格式，并确认正文 "Bowtell and Keevash~\cite{Bowtell2023}" 的语境是否恰当（不应暗示其为已发表的期刊论文）。
- 若该论文后续已发表于某期刊，则 bibitem 中缺少期刊信息。

**修复建议：**
- 若确为未发表预印本，建议将 bibitem key 改为 `Bowtell2021` 以匹配 arXiv 年份；
- 若已有期刊发表信息，请补充期刊名、卷号、页码和发表年份。

---

## 引用格式与作者信息的小问题

### 9. `\bibitem{Yao2025}` — 作者名缩写可能造成歧义
**位置：** `thebibliography` 第 958–962 行（`\bibitem{Yao2025}`）

**论文中的写法：**
> G. Yao and Y. Li, High-performance $N$-queens solver on GPU: iterative DFS with zero bank conflicts, arXiv:2511.12009 (2025).

**查到的真实信息：**
- arXiv:2511.12009 的真实作者为 **Guangchao Yao** 和 **Yali Li**。
- "G. Yao" 缩写正确（Guangchao），但 "Y. Li" 对应的是 **Yali Li**（而非其他常见的 "Y. Li"，如 Yong Li、Yi Li 等）。

**说明：**
- 这不是严格错误，但 "Y. Li" 是极为常见的缩写组合。若该论文被广泛引用，建议保留全名或在首次出现时注明，以避免与同名作者混淆。

---

## 经核查确认无误的引用（部分列举）

以下引用经 Crossref / WebSearch / 期刊官网核实，信息准确无误：

| Bibitem key | 核实结果 |
|---|---|
| `Bezzel1848` | Bezzel 于 1848 年在 *Berliner Schachzeitung* 发表，历史记录无误。 |
| `Luria2021` | arXiv:2105.11431 (2021)，标题、作者均正确。 |
| `Nobel2023` | *Optimization Letters* **17**, 1229–1240 (2023)，DOI: 10.1007/s11590-022-01933-2，正确。 |
| `Zhang2009` | *Phys. Rev. E* **79**, 016703 (2009)，作者 Cheng Zhang & Jianpeng Ma，正确。 |
| `Polson2024` | arXiv:2407.08830 (2024)，作者 Nick Polson & Vadim Sokolov，正确。 |
| `Kawasaki1966` | *Phys. Rev.* **145**, 224 (1966)，正确。 |
| `Efron1982` | SIAM, Philadelphia, 1982（CBMS-NSF Monograph 38），正确。 |
| `Binder2010` | Springer, 5th ed., 2010，正确。 |
| `Kourtis2019` | *SciPost Phys.* **7**, 060 (2019)，DOI: 10.21468/SciPostPhys.7.5.060，正确。 |
| `Nishino1996` | *J. Phys. Soc. Jpn.* **65**, 891–894 (1996)，DOI: 10.1143/JPSJ.65.891，正确。 |
| `Vanderstraeten2018` | *Phys. Rev. E* **98**, 042145 (2018)，DOI: 10.1103/PhysRevE.98.042145，正确。 |
| `Knuth2022` | *The Art of Computer Programming*, Vol. 4B, Addison-Wesley, 2022，Sec. 7.2.2 确实讨论 N-queens 问题，正确。 |
| `Xiang2024` | *Density Matrix and Tensor Network Renormalization*, Cambridge University Press, 2024，ISBN 978-1-009-39867-1，正确。 |

---

## 总结

| 问题等级 | 数量 | 涉及 Bibitem |
|---|---|---|
| **明确错误** | 2 | `Metropolis1953`（年份 1955→1953）、`Frowis2010`（卷号 82→81） |
| **疑似不存在** | 4 | `Boyd2024`、`Tanaka2023`、`Verstraete2022`、`Reynolds2019` |
| **潜在不一致** | 2 | `Simkin2022`（key 与年份不匹配）、`Bowtell2023`（仅预印本，key 与年份不匹配） |
| **建议优化** | 1 | `Yao2025`（作者缩写歧义） |

**总计：6 处需修正/核实的问题引用，2 处建议优化。**
