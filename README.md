This repository contains some pieces of code which might prove useful for the [second project of TMA4220](https://wiki.math.ntnu.no/tma4220/2023h/project) for the academic year 2023/2024.

## Firedrake demo

- `helmholtz.ipynb` provides a notebook (which runs in Google colab) solving the Helmholtz equation following the [Firedrake tutorial](https://www.firedrakeproject.org/demos/helmholtz.py.html). 

## Mesh generator for the unit square (option 1)
- `getPlate.py` generates a Delaunay triangulation of $[0,1]^2$ using the library `scipy.spatial`.
- By running the script a test example with $n=10$ elements per edge will be generated.
- The method outputs three arrays:
  - $p$ : representing the coordinates of the mesh nodes
  - $tri$ : which is the matrix collecting in the $i-$th row the indices of the three vertices of the $i-$triangle of the mesh
  - $edge$ : does the same but for the edges, so in the $i-$th row you find the indices of the nodes delimiting such edge.

## A posteriori project (option 2)

- `mesher.py` uses `pygmsh` to build and locally refine meshes. This script depends on `pymsh` (which can be pip installed) and Firedrake (for mesh plotting).