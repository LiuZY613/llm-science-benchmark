# Bug 定位与修复记录

## Bug 1
- **所在文件:行号**：`main.py:19-20`
- **Bug 简述**：先用 `np.zeros_like(x)` 创建了一个实数数组，再用 `psi[:]` 把复数高斯波包赋值进去，导致虚部被丢弃。
- **为何错**：`np.zeros_like(x)` 的 dtype 为 `float64`，对其切片赋值复数会触发 `ComplexWarning: Casting complex values to real discards the imaginary part`，从而丢失动量相位 `exp(1j * p0 * x)`。后续 `astype(np.complex128)` 只是把已经被截断的实数数组转成复数，无法恢复丢失的信息。
- **如何改**：直接让 `psi` 等于复数表达式：`psi = np.exp(-(x - x0)**2 / (4.0 * sigma**2)) * np.exp(1j * p0 * x)`，再统一 `astype(np.complex128)`。

## Bug 2
- **所在文件:行号**：`potentials.py:37`
- **Bug 简述**：驱动谐振子势的时间依赖项写成了 `A * np.cos(omega_drive * T_REF)`，其中 `T_REF = 0.0`。
- **为何错**：时间依赖势应随时间 `t` 变化，而 `T_REF` 是固定常数 0.0，导致驱动项被冻结在 `cos(0) = 1`，势能失去了随时间振荡的物理行为。
- **如何改**：将 `T_REF` 改为参数 `t`：`A * np.cos(omega_drive * t)`。

## Bug 3
- **所在文件:行号**：`propagator.py:21`
- **Bug 简述**：Strang 分裂算符的动能漂移（drift）步相位多除了一个 2。
- **为何错**：动能项为 `k^2 / 2`，full drift 的精确传播子应为 `exp(-i (k^2 / 2) dt)`。代码写的是 `exp(-1j * 0.5 * grid.k**2 * dt / 2.0)`，相当于只传播了 `dt/2`，破坏了二阶分裂格式的正确性，导致动力学演化失真。
- **如何改**：去掉多余的 `/ 2.0`，改为 `np.exp(-1j * 0.5 * grid.k**2 * dt)`。

## Bug 4
- **所在文件:行号**：`grid.py:20`
- **Bug 简述**：角波数 `k` 直接用了 `np.fft.fftfreq` 的输出，缺少 `2π` 因子。
- **为何错**：`np.fft.fftfreq` 返回的是普通频率 `f`（cycles per unit distance），而量子力学动能项需要角波数 `k = 2π f`。缺少 `2π` 会导致动能 `k^2/2` 整体偏小约 `(2π)^2 ≈ 39.5` 倍，从而传播步长和能量计算都严重错误。
- **如何改**：乘以 `2π`：`self.k = 2.0 * np.pi * np.fft.fftfreq(N, d=self.dx)`。

## Bug 5
- **所在文件:行号**：`observables.py:18`
- **Bug 简述**：计算 `<p>` 时导数前面的系数符号错误，用了 `+1j` 而非 `-1j`。
- **为何错**：动量算符定义为 `p̂ = -i ℏ d/dx`（ℏ = 1），期望值应为 `∫ ψ* (-i ∂ψ/∂x) dx`。代码写成了 `+1j * dpsi`，导致 `<p>` 符号取反。
- **如何改**：将 `1j` 改为 `-1j`：`np.sum(np.conj(psi) * (-1j) * dpsi) * dx`。
