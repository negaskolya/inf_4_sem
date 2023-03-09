import gmsh
import sys

gmsh.initialize()
gmsh.model.add("1.0.3")

lc = 1e-1
rad = 0.5

gmsh.model.geo.addPoint(0, 0, 0,lc, 0)
gmsh.model.geo.addPoint(-rad, 0, 0,lc, 1)
gmsh.model.geo.addPoint(+rad, 0, 0, lc,2)

gmsh.model.geo.addCircleArc(1, 0, 2, 1)
gmsh.model.geo.addCircleArc(2, 0, 1, 2)

gmsh.model.geo.addPoint(0, 0, .5,lc, 3)
gmsh.model.geo.addPoint(-rad, 0, .5,lc, 4)
gmsh.model.geo.addPoint(+rad, 0, .5, lc,5)

gmsh.model.geo.addCircleArc(4, 3, 5, 3)
gmsh.model.geo.addCircleArc(5, 3, 4, 4)

gmsh.model.geo.addLine(1, 4, 5)
gmsh.model.geo.addLine(2, 5, 6)

c1 = gmsh.model.geo.addCurveLoop([5, -4, -6, 2])
c2 = gmsh.model.geo.addCurveLoop([1, 6, -3, -5])
s1 = gmsh.model.geo.addSurfaceFilling([c1])
s2 = gmsh.model.geo.addSurfaceFilling([c2])

c3 = gmsh.model.geo.addCurveLoop([1,2])
c4 = gmsh.model.geo.addCurveLoop([3,4])
s3 = gmsh.model.geo.addPlaneSurface([c3])
s4 = gmsh.model.geo.addPlaneSurface([c4])

gmsh.model.geo.synchronize()
gmsh.model.mesh.generate(3)
gmsh.write("1.0.3.msh")
if '-nopopup' not in sys.argv:
    gmsh.fltk.run()
gmsh.finalize()