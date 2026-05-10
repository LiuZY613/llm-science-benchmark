# 8 处引用错误的标准答案（评分员用）

> 此文档**不要**给被测 AI 看。仅供对照其 `findings.md` 评分。
> 源文件：`03_citation_check/paper_buggy.tex`（基于 `eassy/eassy_v3.tex`，作者已人工核过的 18 条真实引用 + 8 处人为注入错误）。

---

## 类 1：完全捏造（× 2）

### E1 · Reynolds2019
- **类型**：完全捏造（fabricated paper, fabricated authors）
- **bibitem 位置**：thebibliography 中插入于 `Polson2024` 之后、`Kawasaki1966` 之前
- **正文 cite 位置**：line ~122（讨论 lattice gas mapping），原 `\cite{Zhang2009,Polson2024}` 被改为 `\cite{Zhang2009,Polson2024,Reynolds2019}`
- **bibitem 内容**：
  > J. M. Reynolds and S. T. Park, "Spin-glass formulation of the N-queens problem", Comput. Phys. Commun. **241**, 38–47 (2019).
- **为什么是错的**：作者 Reynolds/Park 在统计物理界没有这种合作记录；该论文不存在；卷号 241 (2019) 是 CPC 的真实卷号但其中无此 paper
- **模型可用的验证手段**：Crossref `/works?query=...`、CPC arXiv 搜索、Google Scholar

### E2 · Tanaka2023
- **类型**：完全捏造
- **bibitem 位置**：thebibliography 中插入于 `Vanderstraeten2018` 之后、`github_repo` 之前
- **正文 cite 位置**：line ~791（tensor network 一节论及 CSP），原 `\cite{Kourtis2019,Vanderstraeten2018}` 被改为 `\cite{Kourtis2019,Vanderstraeten2018,Tanaka2023}`
- **bibitem 内容**：
  > H. Tanaka and K. Yamada, "Tensor network methods for combinatorial counting", Phys. Rev. Research **5**, 023115 (2023).
- **为什么是错的**：作者名常见但 Tanaka/Yamada 在 PR Research 上没有此论文；DOI 风格刻意做得真实但实际不存在
- **模型可用的验证手段**：APS 网站 / Crossref / arXiv

---

## 类 2：字段篡改（× 2，真实论文，单字段错）

### E3 · Metropolis1953（年份错）
- **类型**：字段篡改 — 年份
- **bibitem 位置**：原 `Metropolis1953`（thebibliography 中位置不变）
- **改动**：年份 `1953` → `1955`
- **真实信息**：Metropolis et al, J. Chem. Phys. **21**, 1087 (**1953**) — 物理化学经典论文，1953 年发表
- **bibitem 现状**：作者、标题、卷号、页码都对，只有年份错
- **难度**：经典论文，年份记忆稳固；模型纯凭记忆即可识别

### E4 · Frowis2010（卷号错）
- **类型**：字段篡改 — 卷号
- **bibitem 位置**：原 `Frowis2010`（thebibliography 中位置不变）
- **改动**：Phys. Rev. A 卷号 `81` → `82`
- **真实信息**：Frowis, Nebendahl, Dur, Phys. Rev. A **81**, 062337 (2010) — DOI 10.1103/PhysRevA.81.062337
- **bibitem 现状**：作者、标题、文章号 062337、年份 2010 都对，只有卷号错
- **难度**：卷号比年份难记，更考验"真懂"还是"瞎说"

---

## 类 3：领域伪造（× 2，真实作者 + 合理领域，但具体论文不存在）

### E5 · Boyd2024
- **类型**：领域伪造（real authors, plausible topic, fake paper）
- **bibitem 位置**：thebibliography 中插入于 `Nobel2023` 之后、`Yao2025` 之前
- **正文 cite 位置**：line ~89（Section 1 讨论 Nobel et al 凸优化精化 γ 处），原 `\cite{Nobel2023}` 被改为 `\cite{Nobel2023,Boyd2024}`
- **bibitem 内容**：
  > A. Agrawal and S. Boyd, "Convex programming for entropy bounds in combinatorial constants", SIAM Rev. **66**, 312 (2024).
- **为什么是错的**：Akshay Agrawal 与 Stephen Boyd 真合作做 CVXPY/cvxgrp，确实出现在 Nobel2023 的合著者中；但他们没发过这篇 SIAM Rev. 综述
- **难度**：高 — 模型需查 SIAM Rev. 2024 卷 66 实际目录，或 Boyd / Agrawal 个人 publication list

### E6 · Verstraete2022
- **类型**：领域伪造
- **bibitem 位置**：thebibliography 中插入于 `Frowis2010` 之后、`Nishino1996` 之前
- **正文 cite 位置**：line ~654（tensor network 一节讨论 MPO formalism），原 `\cite{Frowis2010}` 被改为 `\cite{Frowis2010,Verstraete2022}`
- **bibitem 内容**：
  > F. Verstraete, "Renormalization of constraint tensor networks", Adv. Phys.: X **7**, 2098453 (2022).
- **为什么是错的**：Frank Verstraete 真做 tensor networks（且作为合著者出现在真引用 Vanderstraeten2018 中），但他没发过这篇 Adv Phys: X 单作者综述
- **难度**：高 — 期刊真实存在，单作者综述风格也合理

---

## 类 4：位置错误（× 2，cite 内容真实但用在不匹配的位置）

### E7 · line ~199 — Frowis2010 错位添加
- **类型**：位置错误 — 添加型
- **位置**：line ~199，原 `Kawasaki dynamics~\cite{Kawasaki1966}` 被改为 `Kawasaki dynamics~\cite{Kawasaki1966,Frowis2010}`
- **为什么是错的**：Frowis2010 是关于 long-range interaction systems 的 MPO 算子构造（参 bibitem），与 Kawasaki dynamics（粒子交换型 MCMC 动力学）毫无关联；这个 cite 不应该出现在这个位置
- **真实状态**：Frowis2010 在论文 line ~654 仍有正确的引用（讨论 MPO formalism），所以它本身没消失、bibitem 也没 unused
- **模型识别要点**：对比 cite 的语义内容（Kawasaki dynamics）与所引 bibitem 的内容（MPO operators）

### E8 · line ~111 — Vanderstraeten2018 错位添加
- **类型**：位置错误 — 添加型
- **位置**：line ~111，原 `hierarchy of increasingly stringent geometric constraints~\cite{Knuth2022}` 被改为 `~\cite{Knuth2022,Vanderstraeten2018}`
- **为什么是错的**：Vanderstraeten2018 是关于 3D frustrated spin systems 的 residual entropies + tensor network 计算（参 bibitem），与 N-queens entropy 的几何约束分解 hierarchy（行 → 列 → 对角线 entropy 阶梯）没有直接关联
- **真实状态**：Vanderstraeten2018 在 line ~791 仍有正确的引用（CSP / tensor network），bibitem 没 unused
- **模型识别要点**：同上，对比 cite 的语义内容与 bibitem 内容

---

## 评分细则（满分 10）

每处错误：
- **正确指出存在错误（true positive，定位到具体 cite/bibitem）+ 0.625 分**（共 5 分）
- **正确分类错误类型（捏造 / 字段篡改 / 领域伪造 / 位置错误）+ 0.625 分**（共 5 分）

惩罚：
- 真实条目误判为假（false positive）：–0.5 分 / 条
- 上限不低于 0

满分 10 分。

## 真实条目（不应判为错的）

剩余 18 条原 bibitem（含 github_repo）以及它们的真实正文 cite 位置都是正确的（除上述 8 处人为注入外）。模型若把以下任意一条判为"假"或"错"将扣分：

```
Bezzel1848, Simkin2022, Bowtell2023, Luria2021, Nobel2023,
Yao2025, Knuth2022, Zhang2009, Polson2024, Kawasaki1966,
Metropolis1953*, Efron1982, Binder2010, Kourtis2019, Xiang2024,
Frowis2010**, Nishino1996, Vanderstraeten2018, github_repo
```
（带 * 的 Metropolis1953 仅年份错，bibitem 其余字段对；带 ** 的 Frowis2010 仅卷号错，其余字段对——模型若判为"全错"则错误分类，按"字段篡改"识别才正确）
