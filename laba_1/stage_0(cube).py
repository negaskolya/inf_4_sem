import gmsh
import sys

gmsh.initialize()

gmsh.model.add("t2")

lc = 1e-2
gmsh.model.geo.addPoint(0, 0, 0, lc, 1)
gmsh.model.geo.addPoint(.1, 0, 0, lc, 2)
gmsh.model.geo.addPoint(0, .1, 0, lc, 3)
gmsh.model.geo.addPoint(0, 0, .1, lc, 4)
gmsh.model.geo.addPoint(.1, .1, 0, lc, 5)
gmsh.model.geo.addPoint(.1, 0, .1, lc, 6)
gmsh.model.geo.addPoint(0, .1, .1, lc, 7)
gmsh.model.geo.addPoint(.1, .1, .1, lc, 8)

for i in range(3):
    gmsh.model.geo.addLine(1, i + 2, i + 1)
    gmsh.model.geo.addLine(i + 5, 8, i + 4)


gmsh.model.geo.addLine(2, 5, 7)
gmsh.model.geo.addLine(2, 6, 8)

gmsh.model.geo.addLine(3, 5, 9)
gmsh.model.geo.addLine(3, 7, 10)

gmsh.model.geo.addLine(4, 6, 11)
gmsh.model.geo.addLine(4, 7, 12)

gmsh.model.geo.addCurveLoop([1, 8, -11, -3], 1)
gmsh.model.geo.addPlaneSurface([1], 1)

gmsh.model.geo.addCurveLoop([2, 9, -7, -1], 2)
gmsh.model.geo.addPlaneSurface([2], 2)

gmsh.model.geo.addCurveLoop([2, 10, -12, -3], 3)
gmsh.model.geo.addPlaneSurface([3], 3)

gmsh.model.geo.addCurveLoop([10, 6, -4, -9], 4)
gmsh.model.geo.addPlaneSurface([4], 4)

gmsh.model.geo.addCurveLoop([12, 6, -5, -11], 5)
gmsh.model.geo.addPlaneSurface([5], 5)

gmsh.model.geo.addCurveLoop([5, -4, -7, 8], 6)
gmsh.model.geo.addPlaneSurface([6], 6)

l = gmsh.model.geo.addSurfaceLoop([i + 1 for i in range(6)])
gmsh.model.geo.addVolume([l])

gmsh.model.geo.synchronize()

gmsh.model.mesh.generate(3)

gmsh.write("t2.msh")
gmsh.write("t2.geo_unrolled")

if '-nopopup' not in sys.argv:
    gmsh.fltk.run()

gmsh.finalize()