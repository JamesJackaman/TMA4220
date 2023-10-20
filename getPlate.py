# Description:
#   Generate a mesh triangulation of the reference square (0,1)^2.
#
# Arguments:
#   e       Number of elements in each spatial direction ((e+1)^2 total nodes).
#
# Returns:
#   p		Nodal points, (x,y)-coordinates for point i given in row i.
#   tri   	Elements. Index to the three corners of element i given in row i.
#   edge  	Index list of all nodal points on the outer edge (r=1).
#
#   Modified version of the original one written by:
#   Authors: Kjetil A. Johannessen, Abdullah Abdulhaque


import numpy as np
import scipy.spatial as spsa
import matplotlib.tri as triP
import matplotlib.pyplot as plt

# Description:
#   Generate a mesh triangulation of the reference square (0,1)^2.
#
# Arguments:
#   e       Number of elements in each spatial direction ((e+1)^2 total nodes).
#
# Returns:
#   p		Nodal points, (x,y)-coordinates for point i given in row i.
#   tri   	Elements. Index to the three corners of element i given in row i.
#
#   Modified version of the original one written by:
#   Authors: Kjetil A. Johannessen, Abdullah Abdulhaque


import numpy as np
import scipy.spatial as spsa


def getPlate(e):
    # Defining auxiliary variables.
    #e is the number of elements on one edge
    N = e+1 #N is the number of nodes on one edge
    
    L = np.linspace(0,1,N)
    Y,X = np.meshgrid(L,L)
    x = np.ravel(np.transpose(X))
    y = np.ravel(np.transpose(Y))

    # Generating nodal points.
    p = np.zeros((N**2,2))
    for i in range(0,N**2):
        p[i,0] = x[i]
        p[i,1] = y[i]

    # Generating elements.
    mesh = spsa.Delaunay(p)
    tri = mesh.simplices

    return p,tri

if __name__=="__main__":
    num_edges = 10
    p,tri = getPlate(num_edges) #creates the mesh arrays
    triangulation = triP.Triangulation(p[:,0], p[:,1], tri) #creates a triangulation given the vertices and the tri matrix
    fig = plt.figure(figsize=(10,10))
    plt.triplot(triangulation)
    plt.title(f"Mesh with {num_edges} elements on each side of the domain",fontsize=20)
    plt.show()