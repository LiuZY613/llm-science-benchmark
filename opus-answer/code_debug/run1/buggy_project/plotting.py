"""Plot routines for simulation diagnostics."""
import numpy as np
import matplotlib
matplotlib.use("Agg")  # non-interactive backend (works headless)
import matplotlib.pyplot as plt


def plot_summary(times, psi_traj, x, energies, x_exp, p_exp, norms, V_x_static, out_path):
    """4-panel summary: |psi|^2 heatmap, energy(t), <x>(t), <p>(t) + norm(t)."""
    fig, axes = plt.subplots(2, 2, figsize=(11, 7))

    ax = axes[0, 0]
    density = np.abs(psi_traj)**2  # shape (nsave, N)
    im = ax.imshow(
        density.T, aspect="auto", origin="lower",
        extent=[times[0], times[-1], x[0], x[-1]], cmap="viridis",
    )
    ax.set_xlabel("t"); ax.set_ylabel("x"); ax.set_title("|ψ(x,t)|²")
    plt.colorbar(im, ax=ax)

    ax = axes[0, 1]
    ax.plot(times, energies, label="⟨H(t)⟩")
    ax.set_xlabel("t"); ax.set_ylabel("E"); ax.set_title("Total energy")
    ax.grid(True); ax.legend()

    ax = axes[1, 0]
    ax.plot(times, x_exp, label="⟨x⟩")
    ax.set_xlabel("t"); ax.set_ylabel("⟨x⟩"); ax.set_title("Position expectation")
    ax.grid(True)

    ax = axes[1, 1]
    ax.plot(times, p_exp, label="⟨p⟩", color="C1")
    ax.plot(times, norms, label="⟨ψ|ψ⟩", color="C2", linestyle="--")
    ax.set_xlabel("t"); ax.set_title("Momentum & norm")
    ax.grid(True); ax.legend()

    fig.tight_layout()
    fig.savefig(out_path, dpi=110)
    plt.close(fig)
