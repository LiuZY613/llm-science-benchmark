# Citation review of `paper.tex` — "Statistical mechanics of the N-queens problem"

This report enumerates each `\bibitem` (and the corresponding `\cite` usage) and records what I was able to verify or could not verify. Items are grouped roughly by severity.

---

## 1. Critical: fictitious / non-existent references

### 1a. `Boyd2024` — Agrawal & Boyd, *SIAM Rev.* **66**, 312 (2024)

- **Bibitem (lines 953–956):**
  > A.~Agrawal and S.~Boyd,
  > Convex programming for entropy bounds in combinatorial constants,
  > SIAM Rev.\ \textbf{66}, 312 (2024).
- **Used at:** line 89 — `\cite{Nobel2023,Boyd2024}` ("Nobel et al subsequently refined these bounds…").
- **Problem:** No such paper appears to exist.
  - Crossref search for Agrawal/Boyd papers in 2022–2024 returns no match.
  - Akshay Agrawal's official publication list (akshayagrawal.com) lists no SIAM Review paper at all, and his only n-queens-related paper is the 2023 *Optimization Letters* article with Nobel and Boyd (i.e. `Nobel2023`).
  - The TOC of *SIAM Review* Vol. 66 (Issues 1–2 verified) contains no paper by Agrawal & Boyd on entropy bounds or combinatorial constants.
- **Likely origin:** A duplicate / fabricated companion to `Nobel2023`. The refinement to γ = 1.94400(1) is in `Nobel2023` alone.
- **Suggested fix:** Delete `Boyd2024`; the in-text claim ("Nobel et al~\cite{Nobel2023,Boyd2024} subsequently refined…") is fully covered by the single `Nobel2023` citation.

### 1b. `Reynolds2019` — Reynolds & Park, *Comput. Phys. Commun.* **241**, 38–47 (2019)

- **Bibitem (lines 980–983):**
  > J.~M.~Reynolds and S.~T.~Park,
  > Spin-glass formulation of the $N$-queens problem,
  > Comput.\ Phys.\ Commun.\ \textbf{241}, 38--47 (2019).
- **Used at:** line 122 — `\cite{Zhang2009,Polson2024,Reynolds2019}` (mapping N-queens to a lattice gas with tunable temperature).
- **Problem:** The paper does not exist.
  - Verified the actual TOC of *Computer Physics Communications* Vol. 241 (Aug 2019) via ScienceDirect: pages 33–39 are "Compressing convolutional neural networks using POD…" by Huang, Zhao, Cai; pages 40–47 are "3D full-wave computation of RF modes in magnetised plasmas" by Aleynikov & Marushchenko. There is **no** N-queens / spin-glass paper in this volume, and no paper by "Reynolds and Park."
  - General web/Google Scholar searches for "Reynolds Park N-queens spin-glass" return nothing matching.
- **Suggested fix:** Remove `Reynolds2019` from the citation triple at line 122 and drop the bibitem. The Zhang & Ma and Polson & Sokolov references already cover the lattice-gas / Monte-Carlo mapping cited in that sentence.

### 1c. `Verstraete2022` — F. Verstraete, *Adv. Phys.: X* **7**, 2098453 (2022)

- **Bibitem (lines 1023–1026):**
  > F.~Verstraete,
  > Renormalization of constraint tensor networks,
  > Adv.\ Phys.: X \textbf{7}, 2098453 (2022).
- **Used at:** line 654 — `\cite{Frowis2010,Verstraete2022}` (in support of the matrix-product-operator formalism for encoding constraints).
- **Problem:** The paper does not exist.
  - The DOI built from the article ID, `10.1080/23746149.2022.2098453`, returns HTTP 404.
  - Crossref shows no Verstraete-authored paper of this title in any journal in 2022.
  - The article ID format (7-digit identifier preceded by year) is the right shape for Adv. Phys.: X, but no actual record is present in the journal's index.
- **Suggested fix:** Replace with a real reference for constraint MPO/PEPS construction, e.g.
  - L. Vanderstraeten, B. Vanhecke, F. Verstraete (the existing `Vanderstraeten2018` already covers a similar idea), or
  - the Cirac/Verstraete review *Rev. Mod. Phys.* **93**, 045003 (2021) on MPS/PEPS, or simply remove this citation since `Frowis2010` already supports the MPO claim.

### 1d. `Tanaka2023` — Tanaka & Yamada, *Phys. Rev. Research* **5**, 023115 (2023)

- **Bibitem (lines 1039–1042):**
  > H.~Tanaka and K.~Yamada,
  > Tensor network methods for combinatorial counting,
  > Phys.\ Rev.\ Research \textbf{5}, 023115 (2023).
- **Used at:** line 791 — `\cite{Kourtis2019,Vanderstraeten2018,Tanaka2023}` (tensor-network contraction as a framework for exact counting).
- **Problem:** The paper does not exist; the (volume, article) coordinates point to an unrelated paper.
  - Crossref lookup of `10.1103/PhysRevResearch.5.023115` returns:
    "Winning strategies of a gambling demon in a Brownian particle under a squeezing potential" by J. A. C. Albay, Y. Jun, P.-Y. Lai, *Phys. Rev. Research* **5**, 023115 (22 May 2023).
    Nothing to do with tensor networks or counting; authors do not include "Tanaka" or "Yamada."
  - Crossref search for Tanaka & Yamada with this title returns no match.
- **Suggested fix:** Remove this citation. `Kourtis2019` and `Vanderstraeten2018` already substantiate the claim that tensor networks are useful for exact counting. If a third reference is wanted, Liu et al., "Computing solution space properties of combinatorial optimization problems via generic tensor networks," *SIAM J. Sci. Comput.* (2023) is a real fit.

---

## 2. Substantive errors in real references

### 2a. `Frowis2010` — Wrong volume number

- **Bibitem (lines 1017–1021):**
  > F.~Fr\"owis, V.~Nebendahl, and W.~D\"ur,
  > Tensor operators: Constructions and applications for long-range interaction systems,
  > Phys.\ Rev.\ A \textbf{82}, 062337 (2010).
- **Used at:** lines 199 and 654.
- **Problem:** The paper is real (arXiv:1003.1047) but appeared in **Phys. Rev. A 81**, 062337 (June 25, 2010), not volume 82.
  - APS DOI: `10.1103/PhysRevA.81.062337`. Volume 82 of Phys. Rev. A is a 2010 second-half volume; article 062337 of vol. 82 is a different paper.
- **Suggested fix:** Change `\textbf{82}` → `\textbf{81}`.

### 2b. `Metropolis1953` — Year typo (1955 instead of 1953)

- **Bibitem (lines 991–995):**
  > N.~Metropolis, A.~W.~Rosenbluth, M.~N.~Rosenbluth, A.~H.~Teller, and E.~Teller,
  > Equation of state calculations by fast computing machines,
  > J.~Chem.~Phys.\ \textbf{21}, 1087 (**1955**).
- **Used at:** line 203.
- **Problem:** The paper appeared in **June 1953**, not 1955. The bibitem key correctly says "Metropolis1953", but the printed year is "1955". Cross-checked with AIP and Wikipedia.
- **Suggested fix:** Change `(1955)` → `(1953)`.

### 2c. `Bezzel1848` — "Schachfreund" mis-treated as the article title

- **Bibitem (lines 929–931):**
  > M.~Bezzel,
  > Schachfreund, Berliner Schachzeitung \textbf{3}, 636 (1848).
- **Used at:** line 77.
- **Problem:** "Schachfreund" was the **pseudonym** Max Bezzel used when posing the eight-queens problem, not the title of the problem-piece. As written, the entry reads as if the article is titled "Schachfreund". The actual problem appeared without a meaningful article title (it was posed as a chess problem); standard bibliographies list it either with no title or with a descriptive title such as "Proposal of the eight queens puzzle."
  - The page number is also reported inconsistently across sources: most secondary sources cite **page 363** of vol. 3 (1848), although a few (including some of the search results for this review) report **page 636**. Without direct access to a scanned 1848 issue I cannot fully resolve this, but the **page-636 figure should be re-verified** — the inverted digit-pair "363 ↔ 636" looks like a transcription error that has propagated.
- **Suggested fix:** Reformat to something like
  `M.~Bezzel (under pseudonym ``Schachfreund''), Berliner Schachzeitung \textbf{3}, 363 (1848).`
  and double-check the page number against a primary source.

---

## 3. Minor / debatable issues

### 3a. `Bowtell2023` — bib key year doesn't match the printed year

- **Bibitem (lines 938–941):**
  > C.~Bowtell and P.~Keevash,
  > The $n$-queens problem,
  > arXiv:2109.08083 (2021).
- **Verification:** arXiv API confirms only one version (v1, 16 Sep 2021), no journal-ref. So the printed year (2021) is correct.
- **Comment:** The label `Bowtell2023` is just a key, but it is potentially confusing because the arXiv preprint is from 2021 and there is no published 2023 version. Cosmetic only.

### 3b. In-text characterization at line 81–82

- **Text:** "Simkin~\cite{Simkin2022} proved that the number of solutions $Q(N)$ satisfies $Q(N) \sim (N/e^{\gamma})^N$. **This result builds on the breakthrough of Bowtell and Keevash~\cite{Bowtell2023}** and earlier bounds by Luria and Simkin~\cite{Luria2021}."
- **Comment:** Slightly mis-attributes credit. The lower bound `Q(n) ≥ ((1+o(1))ne⁻³)ⁿ` was proved **independently and concurrently** by Bowtell-Keevash (whose main result is actually about the toroidal problem) and by Luria-Simkin. Simkin's *Adv. Math.* paper supplies the matching upper bound; saying the upper bound "builds on" Bowtell-Keevash is not quite right. This is an interpretive issue, not a citation-data issue, but worth flagging since it touches on attribution.

### 3c. In-text characterization at line 92–94 (Yao2025)

- **Text:** "exact enumeration of $Q(N)$ by exhaustive backtracking search has been pushed to $N = 27$ using massively parallel GPU computation~\cite{Yao2025}".
- **Verification:** arXiv:2511.12009 by Yao & Li (Nov 2025) is real and does describe a GPU N-queens solver for N = 27.
- **Comment:** Yao & Li themselves state they **verified** the 27-queens result, "confirming earlier results from 2016." The original push to N = 27 was Preußer & Engelhardt (2016). The current wording ("has been pushed to N=27 … \cite{Yao2025}") credits the Yao paper with the breakthrough rather than with verification. Consider citing Preußer & Engelhardt (2016) alongside, or rephrasing.

### 3d. `Knuth2022` — Section pointer is at the parent section level

- **Bibitem (lines 964–967):** `Vol.~4B (Addison-Wesley, 2022), Sec.~7.2.2.`
- **Comment:** Section 7.2.2 is the broad "Backtrack programming" section of Vol. 4B (~340 pages). The detailed n-queens treatment lives in Sec. 7.2.2.1 (dancing links / exact cover) and subsequent subsections of 7.2.2. The pointer is not wrong but is unhelpfully coarse; consider Sec. 7.2.2.1 and/or specific exercise numbers, e.g. exercises 87-ff of 7.2.2 contain the n-queens material and Knuth's bound discussion (which `Nobel2023` builds on). Also note: Vol. 4B publisher is given as Addison-Wesley, which is correct for the trade name (the imprint is Addison-Wesley Professional under Pearson).

### 3e. `Bezzel1848` page number — unresolved

- See 2c. The dueling "page 363" vs. "page 636" is unresolved by the open web sources I consulted. This is the one item I leave as **uncertain**: I could not locate a digitized scan of the 1848 *Berliner Schachzeitung* itself; multiple secondary sources disagree, with Wikipedia citing a different page from the value used in the paper. A library check of the original journal would settle it.

---

## 4. Verified-correct references (no issue found)

For each of the following I checked Crossref / publisher / arXiv as appropriate; the title, authors, journal, volume, page, and year all match.

| Key | Verified citation | How verified |
|---|---|---|
| `Simkin2022` | Simkin, *Adv. Math.* **427**, 109127 (2023) | ScienceDirect DOI 10.1016/j.aim.2023.109127; arXiv:2107.13460 |
| `Bowtell2023` | Bowtell & Keevash, arXiv:2109.08083 (2021) | arXiv API; bib data correct (see 3a for key/style note) |
| `Luria2021` | Luria & Simkin, arXiv:2105.11431 (2021) | arXiv abstract |
| `Nobel2023` | Nobel, Agrawal, Boyd, *Optim. Lett.* **17**, 1229–1240 (2023) | Springer link; arXiv:2112.03336 |
| `Yao2025` | Yao & Li, arXiv:2511.12009 (Nov 2025) | arXiv (see 3c for in-text caveat) |
| `Knuth2022` | Knuth, *TAOCP* Vol. 4B (Addison-Wesley, 2022) | Pearson/Amazon; Aug 2022 publication date (see 3d for section caveat) |
| `Zhang2009` | Zhang & Ma, *Phys. Rev. E* **79**, 016703 (2009) | APS DOI 10.1103/PhysRevE.79.016703 |
| `Polson2024` | Polson & Sokolov, arXiv:2407.08830 (2024) | arXiv abstract |
| `Kawasaki1966` | Kawasaki, *Phys. Rev.* **145**, 224 (1966) | APS DOI 10.1103/PhysRev.145.224 |
| `Efron1982` | Efron, *Jackknife, Bootstrap…*, SIAM CBMS-NSF Monograph 38 (1982) | SIAM publications (epubs.siam.org) |
| `Binder2010` | Binder & Heermann, *Monte Carlo Sim. in Stat. Phys.*, Springer 5th ed. (2010) | Springer link, ISBN 978-3-642-03162-5 |
| `Kourtis2019` | Kourtis, Chamon, Mucciolo, Ruckenstein, *SciPost Phys.* **7**, 060 (2019) | scipost.org/SciPostPhys.7.5.060 |
| `Xiang2024` | T. Xiang, *Density Matrix and Tensor Network Renormalization*, CUP (2024) | cambridge.org book page; published Jan 2024 |
| `Nishino1996` | Nishino & Okunishi, *J. Phys. Soc. Jpn.* **65**, 891–894 (1996) | DOI 10.1143/JPSJ.65.891 |
| `Vanderstraeten2018` | Vanderstraeten, Vanhecke, Verstraete, *Phys. Rev. E* **98**, 042145 (2018) | APS DOI 10.1103/PhysRevE.98.042145; arXiv:1805.10598 |
| `github_repo` | https://github.com/LiuZY613/nqueen-lattice-gas | URL resolves; repo describes the simulation code referenced in the paper |

---

## Summary

- **Fabricated / non-existent references (4):** `Boyd2024`, `Reynolds2019`, `Verstraete2022`, `Tanaka2023`. All four should be removed; the surrounding claims are still supported by the remaining real references.
- **Real references with bibliographic errors (2):** `Frowis2010` (volume should be 81, not 82) and `Metropolis1953` (year should be 1953, not 1955).
- **Citation-style / attribution issues to consider (4):** `Bezzel1848` (pseudonym treated as title; page number suspect), `Bowtell2023` (key vs. year mismatch — cosmetic), in-text "builds on the breakthrough of Bowtell and Keevash" (interpretive), and the in-text crediting of N=27 enumeration to `Yao2025` rather than to the original 2016 result.
- **Verified correct (16):** all others.
