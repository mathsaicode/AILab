# Projects

*Created: 2026-11-23 · Last updated: 2026-11-23*

This is where the projects I can **show** live: written so that someone who does not know me understands what I built, why, and what result I got.

> Projects are not improvised. Each one appears **when I have the knowledge to do it well**, at the end of a unit of the study route. Weeks are approximate (they assume about 10 hours per week) and will be adjusted to my real pace. Target dates come from the [calendar](../docs/ruta/calendario.md) (in Spanish), counting from November 23, 2026.

## Project plan

| # | Project | When | Target date | What I build | What it shows |
|---|---|---|---|---|---|
| 1 | **Neural network from scratch** | End of Unit 6 (≈ week 13) | Feb 21, 2027 | A small NumPy library (layers, activations, loss, optimizers, a `Model` class) trained on a real dataset | That I understand the mechanics inside, not only how to use a library |
| 2 | **From NumPy to PyTorch** | End of Unit 7 (≈ week 17) | Mar 21, 2027 | The same network in PyTorch, with a rigorous comparison: `autograd` gradients against my own, loss curves, timings | Experimental rigor and command of PyTorch |
| 3 | **Image classifier** | End of Unit 8 (≈ week 22) | Apr 25, 2027 | A CNN with data augmentation and error analysis; optionally, a small transformer | Command of modern architectures and critical analysis of results |
| 4 | **Perception for robotics, deployed** | End of Unit 9 (≈ week 28) | Jun 6, 2027 | A perception model (detection or segmentation) on robotics data, served as an API and packaged with Docker | My professional goal: applied AI for robotics and MLOps |

Projects 3 and 4 are proposals: the exact topic is decided when we get there, according to my interests at that moment.

## How each project is organized

```
projects/NN-project-name/
├── README.md        # project write-up (see structure below)
├── notebooks/       # experiments and analysis
├── src/             # reusable project code
├── data/            # small datasets or download instructions (never large files)
└── results/         # final plots and tables
```

## Structure of each project's `README.md`

1. **Problem:** what is being solved and why it matters.
2. **Data:** where it comes from and what it contains.
3. **Method:** which model was used and why, with the necessary mathematics.
4. **Results:** numbers and plots, with an honest reading of them.
5. **How to reproduce:** exact commands.
6. **Limitations and what I learned:** what did not work and what I would improve.
