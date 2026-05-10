"""Entry point: simulate a Gaussian wavepacket in a driven Morse potential.

Run:  python main.py
Outputs:
  - summary.png  (4-panel diagnostic plot)
  - energies.npy (energy time series, for automated checks)
"""
import numpy as np

from grid import Grid1D
from potentials import driven_harmonic_factory
from propagator import propagate
from observables import norm, position, momentum, total_energy
from plotting import plot_summary


def gaussian_wavepacket(x, x0=2.0, sigma=0.5, p0=1.5):
    """Normalized Gaussian wavepacket with mean position x0 and mean momentum p0."""
    psi = np.exp(-(x - x0)**2 / (4.0 * sigma**2), dtype=np.complex128) * np.exp(1j * p0 * x)
    # normalize: ∫|psi|^2 dx = 1
    dx = x[1] - x[0]
    psi /= np.sqrt(np.sum(np.abs(psi)**2) * dx)
    return psi


def main():
    # --- Setup: driven harmonic oscillator (omega=1, drive omega_d=1.7) ---
    grid = Grid1D(N=512, L=30.0)
    V_func = driven_harmonic_factory(omega=1.0, A=0.3, omega_drive=1.7)
    psi0 = gaussian_wavepacket(grid.x, x0=2.0, sigma=0.7071, p0=1.0)

    dt = 0.01
    nsteps = 2000        # total time T = 20
    save_every = 10      # save 200 frames

    # --- Run propagation ---
    times, psi_traj = propagate(psi0, V_func, grid, dt, nsteps,
                                save_every=save_every, t0=0.0)

    # --- Compute observables on saved frames ---
    energies = np.zeros_like(times)
    x_exp = np.zeros_like(times)
    p_exp = np.zeros_like(times)
    norms = np.zeros_like(times)
    for i, (t, psi) in enumerate(zip(times, psi_traj)):
        V_x = V_func(grid.x, t)
        energies[i] = total_energy(psi, V_x, grid.k, grid.dx)
        x_exp[i] = position(psi, grid.x, grid.dx)
        p_exp[i] = momentum(psi, grid.dx)
        norms[i] = norm(psi, grid.dx)

    # --- Report ---
    print(f"Initial energy = {energies[0]:.6f}")
    print(f"Final   energy = {energies[-1]:.6f}")
    print(f"Energy drift   = {abs(energies[-1] - energies[0]):.4e}")
    print(f"Initial norm   = {norms[0]:.6f}")
    print(f"Final   norm   = {norms[-1]:.6f}")
    print(f"Initial <x>    = {x_exp[0]:.4f}")
    print(f"Initial <p>    = {p_exp[0]:.4f}")

    # --- Plot ---
    V_x_static = V_func(grid.x, 0.0)
    plot_summary(times, psi_traj, grid.x,
                 energies, x_exp, p_exp, norms, V_x_static,
                 out_path="summary.png")
    np.save("energies.npy", energies)
    print("Saved: summary.png, energies.npy")


if __name__ == "__main__":
    main()
