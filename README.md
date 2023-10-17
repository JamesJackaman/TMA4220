This repository contains some pieces of code which might prove useful for the [second project of TMA4220](https://wiki.math.ntnu.no/tma4220/2023h/project) for the academic year 2023/2024.

## Firedrake demo

- `helmholtz.ipynb` provides a notebook (which runs in Google colab) solving the Helmholtz equation following the [Firedrake tutorial](https://www.firedrakeproject.org/demos/helmholtz.py.html). 

## A posteriori project (option 2)

- `mesher.py` uses `pygmsh` to build and locally refine meshes. This script depends on `pymsh` (which can be pip installed) and Firedrake (for mesh plotting).