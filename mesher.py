from firedrake import *
import matplotlib.pylab as plt
import pygmsh
import gmsh

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

    return None
        
        
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

    return None



# pygmsh doesn't want to label boundaries, easiest option is to use gmsh directly
def gmsh_mesher(h=0.1, h_refine = 0.01, refine_point = None):
    gmsh.initialize()
    gmsh.option.setNumber("General.Terminal", 1)
    gm = gmsh.model

    gm.add("square mesh") #just a label

    #define points (x,y,z, maxrefine, point label)
    gm.geo.addPoint(0,0,0, h, 1)
    gm.geo.addPoint(1,0,0, h, 2)
    gm.geo.addPoint(1,1,0, h, 3)
    gm.geo.addPoint(0,1,0, h, 4)
    
    #define lines (p1,p2, line label)
    gm.geo.addLine(1,2, 11)
    gm.geo.addLine(2,3, 12)
    gm.geo.addLine(3,4, 13)
    gm.geo.addLine(4,1, 14)
    
    #Create a surface (info, label)
    gm.geo.addCurveLoop([11,12,13,14], 101)
    gm.geo.addPlaneSurface([101], 102)

    #Define boundaries (here each line gets its own label)
    # (dimension, list of lines, label)
    gm.addPhysicalGroup(1, [11], 2)
    gm.addPhysicalGroup(1, [12], 7)
    gm.addPhysicalGroup(1, [13], 1)
    gm.addPhysicalGroup(1, [14], 8)
    
    #Redefine surface as a physical surface
    # (dimension, list of surfaces, label)
    gm.addPhysicalGroup(2, [102], 1001)

    #Define refinement points
    if refine_point is not None:
        gm.geo.addPoint(refine_point[0],refine_point[1],0, h_refine, 5)
    
    #sync mesh (needed before embedding extra points)
    gm.geo.synchronize()

    #If refining, embed points in mesh
    # (point dimension, list of points, surface dimension, surface)
    if refine_point is not None:
        gm.mesh.embed(0, [5], 2, 102)
        
    #Generate mesh
    gm.mesh.generate(2)
    
    #write to file
    gmsh.write("test.msh")
    gmsh.finalize()
    
    return None

if __name__=="__main__":
    gmsh_mesher()
    mesh = Mesh("test.msh")
    
    fig, axes = plt.subplots()
    triplot(mesh, axes=axes)
    axes.legend()
    plt.show()
