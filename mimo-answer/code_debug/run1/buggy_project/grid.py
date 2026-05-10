"""Spatial and momentum grids for FFT-based propagation."""
import numpy as np


class Grid1D:
    """Periodic 1D grid compatible with numpy.fft conventions.

    x: equally spaced points on [-L/2, L/2) with N samples (endpoint excluded).
    k: angular wavenumbers in fft order (matching np.fft.fft output).
    """

    def __init__(self, N: int, L: float):
        if N % 2 != 0:
            raise ValueError("N must be even for symmetric grid")
        self.N = N
        self.L = L
        self.dx = L / N
        self.x = -L / 2 + self.dx * np.arange(N)
        # Angular wavenumber: k_j = 2 pi * fftfreq(N, dx)
        self.k = 2 * np.pi * np.fft.fftfreq(N, d=self.dx)

    def __repr__(self):
        return f"Grid1D(N={self.N}, L={self.L}, dx={self.dx:.4f})"
