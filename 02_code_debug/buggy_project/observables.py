"""Observables for a 1D wavefunction sampled on a grid (hbar = m = 1)."""
import numpy as np


def norm(psi, dx):
    """∫ |ψ|² dx"""
    return np.real(np.sum(np.conj(psi) * psi) * dx)


def position(psi, x, dx):
    """⟨x⟩ = ∫ ψ* x ψ dx"""
    return np.real(np.sum(np.conj(psi) * x * psi) * dx)


def momentum(psi, dx):
    """⟨p⟩ = ∫ ψ* (-i d/dx) ψ dx, computed in real space via central differences."""
    dpsi = np.gradient(psi, dx)
    return np.real(np.sum(np.conj(psi) * 1j * dpsi) * dx)


def kinetic_energy(psi, k, dx):
    """⟨T⟩ = ⟨ψ| p²/2 |ψ⟩ via FFT.
    Use Parseval: ∫|ψ|² dx = (1/N) Σ|ψ̃|² (with numpy fft normalization),
    so ⟨T⟩ = (dx/N) * Σ (k²/2) |ψ̃|².
    Equivalently dx * sum_in_k / N, which equals dx/N * Σ ... .
    """
    psi_k = np.fft.fft(psi)
    N = psi.shape[0]
    return np.real(np.sum(0.5 * k**2 * np.abs(psi_k)**2)) * dx / N


def potential_energy(psi, V_x, dx):
    """⟨V⟩ = ∫ ψ* V(x) ψ dx (V_x is V evaluated on the grid at the relevant time)."""
    return np.real(np.sum(np.conj(psi) * V_x * psi) * dx)


def total_energy(psi, V_x, k, dx):
    return kinetic_energy(psi, k, dx) + potential_energy(psi, V_x, dx)
