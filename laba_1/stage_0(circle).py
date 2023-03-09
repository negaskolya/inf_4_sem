import gmsh
import sys

gmsh.initialize()

gmsh.model.add("t2")

lc = 1e-2
gmsh.model.geo.addPoint(0, 0, 0, lc, 1)
gmsh.model.geo.addPoint(0.1, 0, 0, lc, 2)
gmsh.model.geo.addPoint(0, 0.1, 0, lc, 3)
gmsh.model.geo.addPoint(-0.1, 0, 0, lc, 4)
gmsh.model.geo.addPoint(0, -0.1, 0, lc, 5)

a1 = gmsh.model.geo.addCircleArc(2, 1, 3)
a2 = gmsh.model.geo.addCircleArc(3, 1, 4)
a3 = gmsh.model.geo.addCircleArc(4, 1, 5)
a4 = gmsh.model.geo.addCircleArc(5, 1, 2)

gmsh.model.geo.addCurveLoop([a1, a2, a3, a4], 1)
gmsh.model.geo.addPlaneSurface([1], 1)

gmsh.model.geo.synchronize()

gmsh.model.mesh.generate(3)

gmsh.write("t2.msh")
gmsh.write("t2.geo_unrolled")

if '-nopopup' not in sys.argv:
    gmsh.fltk.run()

gmsh.finalize()