# 5 个 Bug 的标准答案（评分员用）

> 此文档**不要**给被测 AI 看。仅供你对照其 `findings.md` 评分。

---

## Bug 1：`grid.py:20` — 动量网格缺 `2π` 因子

**Buggy**:
```python
self.k = np.fft.fftfreq(N, d=self.dx)
```

**Correct**:
```python
self.k = 2.0 * np.pi * np.fft.fftfreq(N, d=self.dx)
```

**性质**：`np.fft.fftfreq` 返回 `1/wavelength`（普通频率），不是角波数 `k = 2π/λ`。漏 `2π` 后所有 k 都缩小 $2\pi$ 倍，动能算符 $k^2/2$ 被低估约 $40$ 倍。注释明确写着 "Angular wavenumber: k_j = 2 pi * fftfreq"，与代码不一致 — 这是关键线索。

**症状**：动能期望值远低于真实，色散变得很慢，能量大幅漂移。

---

## Bug 2：`propagator.py:21` — Strang kinetic step 多了 `/2.0`

**Buggy**:
```python
psi_k = psi_k * np.exp(-1j * 0.5 * grid.k**2 * dt / 2.0)
```

**Correct**:
```python
psi_k = psi_k * np.exp(-1j * 0.5 * grid.k**2 * dt)
```

**性质**：Strang 是 V(dt/2) → T(dt) → V(dt/2)，中间的动能算符应作用整个 `dt`，但代码写成 `dt/2`。整个传播效率减半，物理时间被偷偷压缩。注释写 "Full drift in k-space" 与代码冲突 — 关键线索。

**症状**：振荡频率约为预期的一半，最终时刻波包位置 / 能量与参考严重不符。

---

## Bug 3：`observables.py:18` — 动量算符符号错

**Buggy**:
```python
return np.real(np.sum(np.conj(psi) * 1j * dpsi) * dx)
```

**Correct**:
```python
return np.real(np.sum(np.conj(psi) * (-1j) * dpsi) * dx)
```

**性质**：$\hat p = -i\hbar\partial_x$。代码用了 `+1j`，符号反了。Docstring 仍写 `-i d/dx`，是关键线索。

**症状**：所有 ⟨p⟩ 数值的符号反转。初始动量 `p0=1.0` 报告为 `≈ -1.0`（在 buggy 联动下还会因 bug 5 变成 0）。

---

## Bug 4：`potentials.py` — `driven_harmonic_factory` 用了 `T_REF` 而非参数 `t`

**Buggy**:
```python
# 文件顶部新增了一个看似无害的常量
T_REF = 0.0

def driven_harmonic_factory(omega=1.0, A=0.3, omega_drive=1.7):
    def V(x, t):
        return 0.5 * omega**2 * x**2 + A * np.cos(omega_drive * T_REF) * x
    return V
```

**Correct**:
```python
def V(x, t):
    return 0.5 * omega**2 * x**2 + A * np.cos(omega_drive * t) * x
```

**性质**：模块级 `T_REF=0.0` 看起来像配置常量，被错用进 driver 的时间项。参数 `t` 接收了正确的时间，但完全不被使用。Docstring 仍写 `cos(omega_drive t) x`。

**症状**：驱动项变成了静态线性势 `A·1·x = 0.3 x`，整个驱动失效。能量不再随时间被泵入泵出；演化退化为非驱动谐振子 + 线性偏置。

---

## Bug 5：`main.py:19-20` — `np.zeros_like(x)` 静默丢虚部

**Buggy**:
```python
psi = np.zeros_like(x)            # x 是 float64 → psi 也是 float64
psi[:] = np.exp(-(x - x0)**2 / (4.0 * sigma**2)) * np.exp(1j * p0 * x)
psi = psi.astype(np.complex128)   # 红鲱鱼：此时虚部已经丢了
```

**Correct**:
```python
psi = np.exp(-(x - x0)**2 / (4.0 * sigma**2)) * np.exp(1j * p0 * x)
psi = psi.astype(np.complex128)
```

**性质**：`np.zeros_like(x)` 沿用 `x` 的 dtype（float64）。下一行复数赋值给 float 数组，numpy 发出 `ComplexWarning` 并**静默丢弃虚部**。后面的 `astype(complex128)` 是个红鲱鱼，看似在补救，实际无效（虚部早没了）。

**症状**：运行时 `ComplexWarning`，初始 `<p>` 接近 0 而非 `1.0`，初始 `<x>` 也偏离 `2.0`（因为 `cos(p0·x)` 调制使重心偏移）。

---

## 评分对照（满分 10）

| 评分项 | 满分 | 实得 |
|--------|------|------|
| Bug 1 修复 + 写入 findings.md | 1.5 |  |
| Bug 2 修复 + 写入 findings.md | 1.5 |  |
| Bug 3 修复 + 写入 findings.md | 1.5 |  |
| Bug 4 修复 + 写入 findings.md | 1.5 |  |
| Bug 5 修复 + 写入 findings.md | 1.5 |  |
| `python main.py` 运行无 warning/error | 1.0 |  |
| 4 项物理判据全部满足 | 1.5 |  |
| **合计** | **10** |  |

### 部分分规则

- 修复了 bug 但 findings.md 没写 → 该 bug 扣 0.5
- findings.md 写到了 bug 但实际没修对 → 该 bug 扣 1.0
- 把"两个 bug 合并描述为一个"算一个 bug
- "意外修对了 bug 但描述错误（如把 bug 1 描述成 broadcasting 问题）" → 该 bug 扣 0.5

## 用于自动化判定的检查脚本

见 `auto_grade.py`（在本目录下）。
