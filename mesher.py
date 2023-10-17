from firedrake import *
import matplotlib.pylab as plt
import pygmsh

def mesher(h=0.1):
    with pygmsh.geo.Geometry() as geom:
        #define points
        p1 = geom.add_point([0,0], h)
        p2 = geom.add_point([1,0], h)
        p3 = geom.add_point([1,1], h)
        p4 = geom.add_point([0,1], h)
    
        #define lines
        l1 = geom.add_line(p1,p2)
        l2 = geom.add_line(p2,p3)
        l3 = geom.add_line(p3,p4)
        l4 = geom.add_line(p4,p1)

        #define mesh boundary
        boundary = geom.add_curve_loop([l1,l2,l3,l4])
        #define mesh surface
        plane1 = geom.add_plane_surface(boundary)

        #generate mesh
        mesh = geom.generate_mesh()

        #write to file
        pygmsh.write("test.msh")
        
def mesher_refine(h=0.1, h_refine = 0.01, refine_point = [0.5,0.5]):
    with pygmsh.geo.Geometry() as geom:
        #define points
        p1 = geom.add_point([0,0], h)
        p2 = geom.add_point([1,0], h)
        p3 = geom.add_point([1,1], h)
        p4 = geom.add_point([0,1], h)
        
        #define lines
        l1 = geom.add_line(p1,p2)
        l2 = geom.add_line(p2,p3)
        l3 = geom.add_line(p3,p4)
        l4 = geom.add_line(p4,p1)

        #define mesh boundary
        boundary = geom.add_curve_loop([l1,l2,l3,l4])
        #define mesh surface
        surface = geom.add_plane_surface(boundary)

        #Refine around a point
        p5 = geom.add_point(refine_point, h_refine)
        geom.in_surface(p5,surface)

        #generate mesh
        mesh = geom.generate_mesh()

        #write to file
        pygmsh.write("test.msh")
    

if __name__=="__main__":
    mesher_refine()
    mesh = Mesh("test.msh")

    triplot(mesh)
    plt.show()
