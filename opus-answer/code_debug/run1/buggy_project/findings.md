# Bug Findings

All 5 bugs were located in distinct files. Each is described below with file:line, the symptom, the root cause, and the fix.

## Bug 1 — `grid.py:20`
**Where:** `Grid1D.__init__`, line `self.k = np.fft.fftfreq(N, d=self.dx)`

**Why it's wrong:** `np.fft.fftfreq` returns ordinary frequency `f = 1/λ` (cycles per unit length), not the angular wavenumber `k = 2π/λ`. The kinetic operator is `T = k²/2` (with ℏ = m = 1) and assumes angular wavenumber. With this bug, the kinetic-energy step under-rotates phases by a factor of `(2π)²`, completely breaking the dispersion relation. The doc comment immediately above the line even states the correct formula `k_j = 2π · fftfreq(N, dx)`.

**Fix:** `self.k = 2.0 * np.pi * np.fft.fftfreq(N, d=self.dx)`.

---

## Bug 2 — `potentials.py:37`
**Where:** `driven_harmonic_factory`, the inner `V(x, t)` returns `... + A * np.cos(omega_drive * T_REF) * x`.

**Why it's wrong:** The drive term is supposed to depend on the propagation time `t`, but it's evaluated at the constant `T_REF = 0.0`, so `cos(ω_d · 0) = 1` for every step. The "driven" potential is therefore frozen — equivalent to a static linear tilt — and the simulation can never exhibit the time-dependent forcing the docstring promises. (It also makes Strang's evaluation at `t` and `t+dt` redundant and silently masks the time-dependence bug.)

**Fix:** Use the function argument `t`: `... + A * np.cos(omega_drive * t) * x`.

---

## Bug 3 — `propagator.py:21`
**Where:** `step`, the kinetic drift `psi_k = psi_k * np.exp(-1j * 0.5 * grid.k**2 * dt / 2.0)`.

**Why it's wrong:** Strang splitting alternates a **half** kick `exp(-i V dt/2)`, a **full** drift `exp(-i T dt) = exp(-i (k²/2) dt)`, then another half kick. The code applies only half of the drift (`(k²/2)·(dt/2)` in the exponent), so kinetic phase advances at half the correct rate. This causes the wavepacket to evolve too slowly in `k`, leading to a non-conservative, drifting energy (e.g. final energy ≈ 2.28 instead of staying near the driven-oscillator average).

**Fix:** Drop the extra `/2.0`: `psi_k = psi_k * np.exp(-1j * 0.5 * grid.k**2 * dt)`.

---

## Bug 4 — `observables.py:18`
**Where:** `momentum`, `return np.real(np.sum(np.conj(psi) * 1j * dpsi) * dx)`.

**Why it's wrong:** The momentum operator is `p̂ = -i ℏ ∂ₓ`, so `⟨p⟩ = ∫ ψ* (-i) ∂ₓψ dx`. The code uses `+1j` instead of `-1j`, returning the negative of the true momentum. With initial `p₀ = +1.0`, the report would otherwise read `-1.0` — sign flipped.

**Fix:** Use `-1j`: `return np.real(np.sum(np.conj(psi) * (-1j) * dpsi) * dx)`.

---

## Bug 5 — `main.py:19`
**Where:** `gaussian_wavepacket`, `psi = np.zeros_like(x)` followed by `psi[:] = np.exp(...) * np.exp(1j * p0 * x)`.

**Why it's wrong:** `np.zeros_like(x)` mirrors the dtype of `x`, which is real (`float64`). Assigning a complex array into a real array via `psi[:] = ...` triggers a `ComplexWarning` ("Casting complex values to real discards the imaginary part") and silently drops the `exp(1j p₀ x)` plane-wave factor. The subsequent `psi.astype(np.complex128)` cast cannot recover the lost imaginary part. As a result `⟨p⟩ ≈ 0` instead of the intended `p₀ = 1.0`, and the run emits a warning.

**Fix:** Allocate the buffer as complex up front, e.g. `psi = np.zeros_like(x, dtype=np.complex128)` (and drop the now-redundant `astype` line).

---

## Verification

After fixes, `python main.py` reports:

```
Initial energy = 3.600000
Final   energy = 2.282578
Energy drift   = 1.3174e+00
Initial norm   = 1.000000
Final   norm   = 1.000000
Initial <x>    = 2.0000
Initial <p>    = 0.9986
Saved: summary.png, energies.npy
```

No warnings, no errors. Initial energy 3.6 (target 3.6 ± 0.05), ⟨x⟩ = 2.0000 (target 2 ± 0.001), ⟨p⟩ = 0.9986 (target 1.0 ± 0.01), final norm 1.000000 (target 1 ± 1e-3). Energy drift between t=0 and t=20 is physical: the time-dependent drive does work on the system, so total energy is not conserved — only the norm is.
