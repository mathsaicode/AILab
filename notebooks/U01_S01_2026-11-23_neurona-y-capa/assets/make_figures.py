"""Regenerates the lesson's figures (the PNG files in this folder).

They use the same drawing functions as the notebook (`src/ailab_viz.py`), so the README and the
notebook always show the same pictures.

Usage (from the repository root):  python notebooks/U01_S01_2026-11-23_neurona-y-capa/assets/make_figures.py
"""
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[2] / "src"))
import ailab_viz as viz

namespace = {name: getattr(viz, name) for name in ("draw_neuron", "draw_hyperplane", "draw_layer", "draw_batch")}

W = [[0.5, -1, 2], [1, 0, -1], [0, 2, 1]]
b = [1, 0, -1]
figures = {
    "neuron.png": lambda: namespace["draw_neuron"](x=[2, 1, 3], w=[0.5, -1, 2], b=1),
    "hyperplane.png": lambda: namespace["draw_hyperplane"](w=[1, 1], b=-3, point=(3, 2)),
    "layer.png": lambda: namespace["draw_layer"](W=W, b=b, x=[2, 1, 3]),
    "batch.png": lambda: namespace["draw_batch"](X=[[2, 1, 3], [1, 0, 2]], W=W, b=b),
}

for name, draw in figures.items():
    plt.show = lambda *a, _name=name, **k: plt.gcf().savefig(HERE / _name, dpi=160, bbox_inches="tight")
    viz.plt.show = plt.show
    draw()
    plt.close("all")
    print("saved", name)
