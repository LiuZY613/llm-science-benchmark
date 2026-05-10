# Bug Report — buggy_project

## Bug 1: Angular wavenumber missing 2π factor

- **File**: `grid.py:20`
- **Bug**: `self.k = np.fft.fftfreq(N, d=self.dx)` returns frequencies (cycles per unit length), not angular wavenumbers. The angular wavenumber is `k_j = 2π · f_j`.
- **Why wrong**: All downstream computations (kinetic energy, propagator drift phase) treat `k` as the angular wavenumber. Using `fftfreq` directly makes `k²` smaller by a factor of `(2π)² ≈ 39.5`, causing the kinetic energy and kinetic phase to be severely underestimated. The docstring on line 9 even states the correct definition but the code never multiplies by `2π`.
- **Fix**: `self.k = 2.0 * np.pi * np.fft.fftfreq(N, d=self.dx)`

---

## Bug 2: Kinetic drift phase has extra factor of 1/2

- **File**: `propagator.py:21`
- **Bug**: The Strang-split drift step uses `np.exp(-1j * 0.5 * grid.k**2 * dt / 2.0)`. The factor `0.5 * k²` is already the kinetic energy `T(k) = k²/2`. The full drift should be `exp(-i T dt) = exp(-i · k²/2 · dt)`, but the extra `/2.0` turns this into `exp(-i · k²/4 · dt)` — half the correct phase.
- **Why wrong**: The drift step under-rotates the momentum-space wavefunction, causing incorrect kinetic propagation. Combined with Bug 1, the effective kinetic phase is off by a factor of ~1/79, which explains the severe energy drift.
- **Fix**: remove the extra `/2.0` → `np.exp(-1j * 0.5 * grid.k**2 * dt)`

---

## Bug 3: Time dependence broken in `driven_harmonic_factory`

- **File**: `potentials.py:37`
- **Bug**: The drive term uses `T_REF` (defined as `0.0` on line 5) instead of the function parameter `t`: `A * np.cos(omega_drive * T_REF) * x`. Since `cos(0) = 1`, the drive is always `A * x` regardless of time.
- **Why wrong**: The potential should be `V(x, t) = ½ ω² x² + A cos(ω_d t) x`. Using `T_REF` strips all time dependence from the drive, making it a static linear perturbation. The harmonic drive cannot do physical work on the wavepacket. (Note: `driven_morse_factory` on line 24 correctly uses `t`.)
- **Fix**: `A * np.cos(omega_drive * t) * x`

---

## Bug 4: Wrong sign in momentum expectation

- **File**: `observables.py:18`
- **Bug**: The momentum operator is `p̂ = −i ∂/∂x`. The expectation should be `⟨p⟩ = Re(∫ ψ* (−i ∂ψ/∂x) dx)`, but the code computes `Re(∑ ψ* · (+i) · dψ · dx)` — the sign is flipped.
- **Why wrong**: For a wavepacket with `p₀ = 1.0`, the code reports `⟨p⟩ ≈ −1.0` instead of `+1.0` (before Bug 5 masked this by zeroing out the imaginary part). The sign convention is a direct mathematical error: `+i` in place of `−i`.
- **Fix**: `np.real(np.sum(np.conj(psi) * (-1j) * dpsi) * dx)`

---

## Bug 5: Wavepacket constructed in a real array, discarding imaginary part

- **File**: `main.py:20`
- **Bug**: `psi = np.zeros_like(x)` creates a `float64` array (since `x` is float64). Assigning the complex Gaussian `exp(−(x−x₀)²/(4σ²)) · exp(i p₀ x)` into this real array silently discards the imaginary part, producing a `ComplexWarning`.
- **Why wrong**: The momentum phase `exp(i p₀ x)` is purely imaginary in the exponent, so the entire wavepacket collapses to a real-valued function with zero momentum. This is why `⟨p⟩` was `0.0000` before the fix.
- **Fix**: Compute `psi` directly as a complex array: `psi = np.exp(−(x − x0)**2 / (4.0 * sigma**2)) * np.exp(1j * p0 * x)`
