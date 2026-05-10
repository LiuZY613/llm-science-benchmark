"""Strang split-operator propagator for the 1D time-dependent Schroedinger equation.

Units: hbar = 1, m = 1.
Strang scheme (second order in dt):
    psi -> exp(-i V(t) dt/2) psi
    psi -> F^{-1} exp(-i (k^2 / 2) dt) F psi
    psi -> exp(-i V(t+dt) dt/2) psi
We evaluate V at t and t+dt for the two half-kicks (equivalent to the
standard "kick-drift-kick" form when V is time-independent, and gives a
proper second-order scheme when V is time-dependent).
"""
import numpy as np


def step(psi, V_func, t, dt, grid):
    """One Strang step from t to t+dt. Returns updated psi."""
    # Half kick at time t
    psi = psi * np.exp(-1j * V_func(grid.x, t) * dt / 2.0)
    # Full drift in k-space
    psi_k = np.fft.fft(psi)
    psi_k = psi_k * np.exp(-1j * 0.5 * grid.k**2 * dt / 2.0)
    psi = np.fft.ifft(psi_k)
    # Half kick at time t+dt
    psi = psi * np.exp(-1j * V_func(grid.x, t + dt) * dt / 2.0)
    return psi


def propagate(psi0, V_func, grid, dt, nsteps, save_every=1, t0=0.0):
    """Evolve psi0 for nsteps. Returns (times_saved, psi_traj) with shape (nsave, N)."""
    psi = psi0.astype(np.complex128).copy()
    saved_psi = [psi.copy()]
    saved_t = [t0]
    t = t0
    for i in range(nsteps):
        psi = step(psi, V_func, t, dt, grid)
        t = t0 + (i + 1) * dt
        if (i + 1) % save_every == 0:
            saved_psi.append(psi.copy())
            saved_t.append(t)
    return np.array(saved_t), np.array(saved_psi)
