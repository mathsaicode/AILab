"""Drawing helpers for the AILab lessons.

Small matplotlib functions that draw the ideas of each lesson (a list, a neuron, a hyperplane,
a layer, a batch). They only draw: no lesson logic lives here.

Created: 2026-11-23 · Last updated: 2026-11-23
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle, Rectangle

INK, MUTED = "#1E293B", "#64748B"
BLUE, TEAL, AMBER, ROSE = "#4F46E5", "#0D9488", "#F59E0B", "#E11D48"
BLUE_BG, AMBER_BG = "#EEF2FF", "#FEF3C7"

plt.rcParams.update({
    "figure.dpi": 110, "figure.facecolor": "white", "font.size": 11,
    "text.color": INK, "axes.edgecolor": MUTED, "axes.labelcolor": INK,
    "axes.spines.top": False, "axes.spines.right": False,
})

def draw_list(x, name="x"):
    """A list as boxes: math index (starts at 1) above, Python index (starts at 0) below."""
    n = len(x)
    fig, ax = plt.subplots(figsize=(1.15 * n + 1.8, 2.1))
    ax.axis("off")
    for i, v in enumerate(x):
        x0 = i * 1.15
        ax.add_patch(FancyBboxPatch((x0, 0.55), 0.95, 0.85, boxstyle="round,pad=0.02,rounding_size=0.14",
                                    fc=BLUE_BG, ec=BLUE, lw=2))
        ax.text(x0 + 0.475, 0.975, f"{v:g}", ha="center", va="center", fontsize=17, weight="bold")
        ax.text(x0 + 0.475, 1.75, f"${name}_{{{i+1}}}$", ha="center", va="center", fontsize=12, color=MUTED)
        ax.text(x0 + 0.475, 0.2, f"{name}[{i}]", ha="center", va="center", fontsize=12, color=BLUE, family="monospace")
    ax.text(-0.15, 1.75, "math", ha="right", va="center", fontsize=10, color=MUTED, style="italic")
    ax.text(-0.15, 0.2, "Python", ha="right", va="center", fontsize=10, color=BLUE, style="italic")
    ax.set_xlim(-1.1, n * 1.15)
    ax.set_ylim(0, 2.0)
    plt.show()

def draw_neuron(x, w, b):
    """One neuron: inputs, weighted arrows, sum plus bias, output."""
    x, w = np.asarray(x, float), np.asarray(w, float)
    n, y = len(x), float(w @ x + b)
    fig, ax = plt.subplots(figsize=(8.4, 0.95 * n + 1.5))
    ax.axis("off")
    ys = (n - 1) - np.arange(n)
    cx, cy = 5.2, (n - 1) / 2
    wmax = np.abs(w).max()
    for i in range(n):
        col = TEAL if w[i] >= 0 else ROSE
        ax.add_patch(FancyArrowPatch((0.95, ys[i]), (cx - 0.68, cy), arrowstyle="-|>", mutation_scale=15,
                                     lw=1.2 + 2.4 * abs(w[i]) / wmax, color=col, zorder=1))
        px, py = 0.95 + (cx - 0.68 - 0.95) * 0.4, ys[i] + (cy - ys[i]) * 0.4
        ax.text(px, py + 0.2, f"$w_{i+1}={w[i]:g}$", color=col, fontsize=11.5, weight="bold", ha="center",
                bbox=dict(fc="white", ec="none", pad=1.5), zorder=3)
        ax.add_patch(Circle((0.6, ys[i]), 0.33, fc=BLUE_BG, ec=BLUE, lw=2, zorder=2))
        ax.text(0.6, ys[i], f"{x[i]:g}", ha="center", va="center", fontsize=13, weight="bold", zorder=3)
        ax.text(0.1, ys[i], f"$x_{i+1}$", ha="right", va="center", fontsize=13, color=MUTED)
    ax.add_patch(Circle((cx, cy), 0.66, fc=AMBER_BG, ec=AMBER, lw=2.2, zorder=2))
    ax.text(cx, cy, r"$\Sigma$", ha="center", va="center", fontsize=24, zorder=3)
    ax.text(cx, cy - 1.0, f"+ bias  $b={b:g}$", ha="center", va="center", fontsize=12, color="#B45309", weight="bold")
    ax.add_patch(FancyArrowPatch((cx + 0.7, cy), (cx + 2.1, cy), arrowstyle="-|>", mutation_scale=16, lw=2.2, color=INK))
    ax.text(cx + 2.25, cy, f"$y={y:g}$", ha="left", va="center", fontsize=17, weight="bold")
    ax.text(0.0, -0.95, "teal arrow: positive weight (pushes up)    rose arrow: negative weight (pushes down)    thickness: |w|",
            fontsize=9.5, color=MUTED, ha="left")
    ax.set_xlim(-0.6, cx + 3.4)
    ax.set_ylim(-1.3, n - 0.4)
    plt.show()

def draw_hyperplane(w, b, point=None, lim=(-1, 6)):
    """A neuron in 2D: the line w.x + b = 0 splits the plane; b slides the line."""
    w = np.asarray(w, float)
    xs = np.linspace(*lim, 200)
    line = lambda bb: -(w[0] * xs + bb) / w[1]
    fig, ax = plt.subplots(figsize=(5.8, 5.2))
    ax.fill_between(xs, line(b), lim[1], color=TEAL, alpha=0.10)
    ax.fill_between(xs, lim[0], line(b), color=ROSE, alpha=0.10)
    ax.plot(xs, line(0), color=MUTED, lw=1.6, ls="--", label="same $w$ with $b=0$ (through the origin)")
    ax.plot(xs, line(b), color=BLUE, lw=2.8, label=f"$w^\\top x + b = 0$  (here $b={b:g}$)")
    u = w / np.linalg.norm(w)
    p0 = -b * w / (w @ w)
    ax.annotate("", xy=p0 + 1.6 * u, xytext=p0, arrowprops=dict(arrowstyle="-|>", lw=2.4, color=AMBER))
    ax.text(*(p0 + 1.85 * u), "$w$", color="#B45309", fontsize=15, weight="bold", ha="center", va="center")
    ax.text(lim[1] - 0.15, lim[1] - 0.55, r"$w^\top x + b > 0$", color=TEAL, fontsize=12.5, weight="bold", ha="right")
    ax.text(lim[0] + 0.15, line(b)[0] - 1.1, r"$w^\top x + b < 0$", color=ROSE, fontsize=12.5, weight="bold", ha="left")
    if point is not None:
        pt = np.asarray(point, float)
        z = float(w @ pt + b)
        foot = pt - (z / (w @ w)) * w
        ax.plot(*zip(pt, foot), color=INK, lw=1.4, ls=":")
        ax.scatter(*pt, s=90, color=TEAL if z >= 0 else ROSE, edgecolor=INK, zorder=5)
        ax.annotate(f"  $x=({pt[0]:g},{pt[1]:g})$\n  signed distance = {z / np.linalg.norm(w):.2f}", pt,
                    xytext=(pt[0] + 0.25, pt[1] - 0.1), fontsize=10.5, va="top")
    ax.set_xlim(lim); ax.set_ylim(lim); ax.set_aspect("equal")
    ax.grid(color="#E2E8F0", lw=0.8); ax.set_axisbelow(True)
    ax.set_xlabel("$x_1$"); ax.set_ylabel("$x_2$")
    ax.set_title("A neuron cuts the plane in two", weight="bold", fontsize=13)
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.13), fontsize=9.5, frameon=False)
    plt.show()

def draw_layer(W, b, x):
    """A layer: every input is connected to every neuron; row j of W holds the weights of neuron j."""
    W, b, x = np.asarray(W, float), np.asarray(b, float), np.asarray(x, float)
    m, n = W.shape
    y = W @ x + b
    fig, ax = plt.subplots(figsize=(8.6, 0.95 * max(m, n) + 1.5))
    ax.axis("off")
    yi, yo = (n - 1) / 2 - np.arange(n), (m - 1) / 2 - np.arange(m)
    wmax = np.abs(W).max()
    for j in range(m):
        for i in range(n):
            ax.plot([0.7, 5.0], [yi[i], yo[j]], color=TEAL if W[j, i] >= 0 else ROSE,
                    lw=0.5 + 3.0 * abs(W[j, i]) / wmax, alpha=0.6, zorder=1, solid_capstyle="round")
    for i in range(n):
        ax.add_patch(Circle((0.7, yi[i]), 0.33, fc=BLUE_BG, ec=BLUE, lw=2, zorder=2))
        ax.text(0.7, yi[i], f"{x[i]:g}", ha="center", va="center", fontsize=13, weight="bold", zorder=3)
        ax.text(0.2, yi[i], f"$x_{i+1}$", ha="right", va="center", fontsize=13, color=MUTED)
    for j in range(m):
        ax.add_patch(Circle((5.0, yo[j]), 0.4, fc=AMBER_BG, ec=AMBER, lw=2.2, zorder=2))
        ax.text(5.0, yo[j], f"$b={b[j]:g}$", ha="center", va="center", fontsize=9.5, color="#B45309", zorder=3)
        ax.text(5.6, yo[j], f"$y_{j+1}={y[j]:g}$", ha="left", va="center", fontsize=14, weight="bold")
        ax.text(2.85, yo[j] + 0.0, "", ha="center")
    ax.text(5.0, yo[0] + 0.85, "neurons (rows of $W$)", ha="center", fontsize=10.5, color=MUTED)
    ax.text(0.7, yi[0] + 0.7, "inputs", ha="center", fontsize=10.5, color=MUTED)
    ax.text(0.0, yo[-1] - 1.0, "teal: positive weight    rose: negative weight    thickness: |w|", fontsize=9.5, color=MUTED)
    ax.set_xlim(-0.6, 7.6)
    ax.set_ylim(yo[-1] - 1.4, max(yi[0], yo[0]) + 1.2)
    plt.show()

def _grid(ax, M, x0, y0, fc, title, shape, hl_row=None, s=0.66):
    M = np.atleast_2d(M)
    r, c = M.shape
    for i in range(r):
        for j in range(c):
            ax.add_patch(Rectangle((x0 + j * s, y0 - (i + 1) * s), s, s, fc=AMBER_BG if hl_row == i else fc,
                                   ec="white", lw=2.5))
            ax.text(x0 + (j + 0.5) * s, y0 - (i + 0.5) * s, f"{M[i, j]:g}", ha="center", va="center", fontsize=11.5)
    ax.text(x0 + c * s / 2, y0 + 0.15, title, ha="center", va="bottom", fontsize=14, weight="bold")
    ax.text(x0 + c * s / 2, y0 - r * s - 0.12, shape, ha="center", va="top", fontsize=10.5, color=MUTED, family="monospace")
    return x0 + c * s

def draw_batch(X, W, b):
    """The batch formula Y = X W^T + b drawn as matrices, with their shapes."""
    X, W, b = np.asarray(X, float), np.asarray(W, float), np.asarray(b, float)
    Y = X @ W.T + b
    s, gap = 0.66, 0.85
    mats = [(X, BLUE_BG, "$X$", 0), (W.T, "#CCFBF1", r"$W^{\top}$", None), (b, "#FFE4E6", "$b$", None), (Y, "#E0E7FF", "$Y$", 0)]
    width = sum(np.atleast_2d(M).shape[1] * s for M, *_ in mats) + 3 * gap
    top = max(np.atleast_2d(M).shape[0] for M, *_ in mats) * s
    scale = 0.9                                   # inches per data unit, the same on both axes
    fig, ax = plt.subplots(figsize=((width + 0.6) * scale, (top + 1.9) * scale))
    ax.axis("off")
    x, ops = 0.0, ["@", "+", "="]
    for k, (M, fc, title, hl) in enumerate(mats):
        end = _grid(ax, M, x, 0.0, fc, title, f"{np.atleast_2d(M).shape if np.ndim(M) > 1 else M.shape}", hl)
        if k < 3:
            ax.text(end + gap / 2, -np.atleast_2d(mats[1][0]).shape[0] * s / 2 + 0.05, ops[k], ha="center", va="center",
                    fontsize=22, color=MUTED)
        x = end + gap
    ax.text((x - gap) / 2, -top - 0.62, "one row per example   ·   one column per neuron   ·   the bias is repeated on every row (broadcasting)",
            ha="center", fontsize=10.5, color=MUTED)
    ax.set_xlim(-0.3, x - gap + 0.3)
    ax.set_ylim(-top - 0.9, 0.95)
    ax.set_aspect("equal")
    plt.show()
