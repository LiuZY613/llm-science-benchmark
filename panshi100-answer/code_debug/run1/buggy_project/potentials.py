"""Potential energy functions V(x) and V(x,t)."""
import numpy as np

# Reference time used by some time-dependent potentials.
T_REF = 0.0


def harmonic(x, omega=1.0):
    """V(x) = 0.5 * omega^2 * x^2"""
    return 0.5 * omega**2 * x**2


def morse(x, D=8.0, alpha=0.5, x_eq=0.0):
    """Morse potential: V(x) = D (1 - exp(-alpha (x - x_eq)))^2"""
    return D * (1.0 - np.exp(-alpha * (x - x_eq)))**2


def driven_morse_factory(D=8.0, alpha=0.5, x_eq=0.0, A=0.3, omega_drive=1.5):
    """Return a callable V(x, t) for a Morse potential with a sinusoidal dipole drive.

    V(x, t) = D (1 - exp(-alpha (x-x_eq)))^2  +  A cos(omega_drive * t) * x
    """
    def V(x, t):
        return morse(x, D=D, alpha=alpha, x_eq=x_eq) + A * np.cos(omega_drive * t) * x
    return V


def driven_harmonic_factory(omega=1.0, A=0.3, omega_drive=1.7):
    """Return a callable V(x, t) for a driven harmonic oscillator.

    V(x, t) = 0.5 omega^2 x^2  +  A cos(omega_drive t) x

    Bounded on both sides (no leakage), and an exact analytical reference
    exists for the classical mean-trajectory of a coherent state.
    """
    def V(x, t):
        return 0.5 * omega**2 * x**2 + A * np.cos(omega_drive * T_REF) * x
    return V
