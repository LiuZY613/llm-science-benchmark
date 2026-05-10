# 1D Driven Quantum Wavepacket Simulation

This project simulates the time evolution of a Gaussian wavepacket in a
**driven harmonic oscillator** potential

$$V(x, t) = \tfrac{1}{2}\omega^2 x^2 + A\,\cos(\omega_d t)\,x$$

using a Strang split-operator FFT scheme (second-order accurate in `dt`).
Units: $\hbar = m = 1$.

## Files

| File | Purpose |
|------|---------|
| `grid.py` | Periodic 1D spatial / momentum grid (FFT-compatible) |
| `potentials.py` | Static (`harmonic`, `morse`) and time-dependent (`driven_*_factory`) potentials |
| `propagator.py` | Strang split-operator step + outer time loop |
| `observables.py` | $\langle x\rangle$, $\langle p\rangle$, kinetic / potential / total energy, norm |
| `plotting.py` | 4-panel diagnostic plot |
| `main.py` | Entry point: setup, run, observables, plot |

## How to run

```bash
python main.py
```

Outputs:
- `summary.png` — 4-panel diagnostic plot
- `energies.npy` — total energy time series
- console: initial/final energy, norm, ⟨x⟩, ⟨p⟩

## Expected physical behaviour (correct version)

- Norm conserved to machine precision throughout.
- For a Gaussian wavepacket initialized at $x_0=2$, $\sigma=1/\sqrt{2}$, $p_0=1$ in $V(x,t)$ with
  $\omega=1$, $A=0.3$, $\omega_d=1.7$: initial $\langle H\rangle \approx 3.6$, oscillating
  but bounded between roughly $2.2$ and $3.7$ over $T=20$.
- $\langle x\rangle(t)$ executes near-harmonic oscillation around 0 with the drive perturbation;
  $\langle p\rangle(t)$ correspondingly oscillates around 0.
