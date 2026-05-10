# Bug Findings

## Bug 1: `potentials.py:37` — Driven harmonic potential uses constant `T_REF` instead of time `t`

**File & line:** `potentials.py`, line 37

**Description:** The `driven_harmonic_factory` returns a closure `V(x, t)` where the drive term uses the module-level constant `T_REF = 0.0` instead of the argument `t`.

**Why it's wrong:** The time-dependent drive `A cos(omega_drive * t) * x` is evaluated as `A cos(omega_drive * 0.0) * x = A * x` for all time, making the potential effectively time-independent. The wavepacket evolves under a static potential, so the physical driving effect is completely absent. This causes incorrect energy evolution.

**Fix:** Replace `T_REF` with `t` on line 37:
```python
# Before:
return 0.5 * omega**2 * x**2 + A * np.cos(omega_drive * T_REF) * x
# After:
return 0.5 * omega**2 * x**2 + A * np.cos(omega_drive * t) * x
```

---

## Bug 2: `grid.py:20` — Missing `2*pi` factor in wavenumber grid

**File & line:** `grid.py`, line 20

**Description:** The angular wavenumber array is computed as `self.k = np.fft.fftfreq(N, d=self.dx)`, but `np.fft.fftfreq` returns frequencies in cycles per unit length, not angular wavenumbers.

**Why it's wrong:** The split-operator propagator uses `exp(-i * k^2/2 * dt)` for the kinetic drift. Without the `2*pi` factor, `k` values are too small by a factor of `2*pi`, so the kinetic energy is underestimated by `(2*pi)^2 ≈ 39.5x`. This makes the initial energy far too low and causes incorrect wavepacket dynamics.

**Fix:** Multiply by `2 * np.pi`:
```python
# Before:
self.k = np.fft.fftfreq(N, d=self.dx)
# After:
self.k = 2 * np.pi * np.fft.fftfreq(N, d=self.dx)
```

---

## Bug 3: `propagator.py:21` — Extra `/2.0` in kinetic drift exponent

**File & line:** `propagator.py`, line 21

**Description:** The kinetic drift step reads `exp(-1j * 0.5 * grid.k**2 * dt / 2.0)`. The factor `0.5` is the correct `1/(2m)` with `m=1`, but the trailing `/2.0` divides the exponent by an extra factor of 2.

**Why it's wrong:** The Strang split-operator scheme applies a full kinetic step `exp(-i * (k^2/2m) * dt)` in k-space. With the extra `/2.0`, the effective drift is only half of what it should be, breaking the unitarity/symmetry of the splitting scheme and causing incorrect time evolution (wavepacket spreads too slowly, norm may drift over long times).

**Fix:** Remove the `/2.0`:
```python
# Before:
psi_k = psi_k * np.exp(-1j * 0.5 * grid.k**2 * dt / 2.0)
# After:
psi_k = psi_k * np.exp(-1j * 0.5 * grid.k**2 * dt)
```

---

## Bug 4: `observables.py:18` — Wrong sign in momentum operator

**File & line:** `observables.py`, line 18

**Description:** The momentum expectation value is computed as `Re(∫ ψ* (1j) (dψ/dx) dx)` but the correct quantum mechanical momentum operator is `p̂ = -i d/dx` (with `ℏ=1`).

**Why it's wrong:** Using `+1j` instead of `-1j` computes `-⟨p⟩` instead of `⟨p⟩`. For a wavepacket initialized with `p0 = 1.0`, this gives `⟨p⟩ ≈ -1.0` instead of `+1.0`, violating the physical expectation that the initial momentum matches `p0`.

**Fix:** Change `1j` to `-1j`:
```python
# Before:
return np.real(np.sum(np.conj(psi) * 1j * dpsi) * dx)
# After:
return np.real(np.sum(np.conj(psi) * (-1j) * dpsi) * dx)
```

---

## Bug 5: `main.py:19` — `np.zeros_like(x)` creates a real array, discarding the complex wavefunction

**File & line:** `main.py`, line 19–21

**Description:** `psi = np.zeros_like(x)` creates a real-valued array (since `x` is real). The subsequent `psi[:] = np.exp(...) * np.exp(1j * p0 * x)` tries to assign complex values into a real array, triggering a `ComplexWarning` and silently discarding the imaginary part (the momentum-carrying phase factor `exp(1j * p0 * x)`). The later `psi.astype(np.complex128)` converts to complex but the imaginary data is already lost.

**Why it's wrong:** The wavefunction becomes a real Gaussian `exp(-(x-x0)^2/(4σ^2)) * cos(p0*x)` instead of the intended complex Gaussian `exp(-(x-x0)^2/(4σ^2)) * exp(i*p0*x)`. This means:
- `⟨p⟩ ≈ 0` (real wavefunction has zero expected momentum)
- `⟨x⟩` is shifted from `x0` because `cos(p0*x)` modulates the density
- A `ComplexWarning` is emitted

**Fix:** Construct `psi` directly as a complex array:
```python
# Before:
psi = np.zeros_like(x)
psi[:] = np.exp(-(x - x0)**2 / (4.0 * sigma**2)) * np.exp(1j * p0 * x)
psi = psi.astype(np.complex128)
# After:
psi = np.exp(-(x - x0)**2 / (4.0 * sigma**2), dtype=np.complex128) * np.exp(1j * p0 * x)
```
