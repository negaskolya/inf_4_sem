import gmsh
import sys
import math

gmsh.initialize()
gmsh.model.add("thor")
r = 1
R = 3
lc = 0.3

for i in range(0, 6):
    phi = [0, math.pi/2, math.pi, 3*math.pi/2, 2 * math.pi, 5 * math.pi / 2][i]
    j = 10 * i

    # Центры дуг
    gmsh.model.geo.addPoint(0, 0, 0, lc, 1 + j)
    gmsh.model.geo.addPoint(0, 0, r, lc, 2 + j)
    gmsh.model.geo.addPoint(0, 0, -r, lc, 3 + j)
    gmsh.model.geo.addPoint(R * math.cos(phi), R * math.sin(phi), 0, lc, 5 + j)

    # крайние точки для дуг
    gmsh.model.geo.addPoint((R + r) * math.cos(phi), (R + r) * math.sin(phi), 0, lc, 6 + j)
    gmsh.model.geo.addPoint((R) * math.cos(phi), (R) * math.sin(phi), r, lc, 7 + j)
    gmsh.model.geo.addPoint((R - r) * math.cos(phi), (R - r) * math.sin(phi), 0, lc, 8 + j)
    gmsh.model.geo.addPoint((R) * math.cos(phi), (R) * math.sin(phi), -r, lc, 9 + j)

for i in range(0, 5):
    j = 10 * i
    gmsh.model.geo.addCircleArc(7 + j, 2, 17 + j, 1 + j)
    gmsh.model.geo.addCircleArc(6 + j, 1, 16 + j, 2 + j)
    gmsh.model.geo.addCircleArc(8 + j, 1, 18 + j, 3 + j)
    gmsh.model.geo.addCircleArc(9 + j, 3, 19 + j, 4 + j)

    gmsh.model.geo.addCircleArc(6 + j, 5 + j, 7 + j, 5 + j)
    gmsh.model.geo.addCircleArc(7 + j, 5 + j, 8 + j, 6 + j)
    gmsh.model.geo.addCircleArc(8 + j, 5 + j, 9 + j, 7 + j)
    gmsh.model.geo.addCircleArc(9 + j, 5 + j, 6 + j, 8 + j)

c = []
s = []
for i in range(0, 4):
    j = 10 * i
    k = 4 * i
    c.append(gmsh.model.geo.addCurveLoop([1 + j, 16 + j, -(3 + j), -(6 + j)]))
    s.append(gmsh.model.geo.addSurfaceFilling([c[0 + k]]))
    c.append(gmsh.model.geo.addCurveLoop([2 + j, 15 + j, -(1 + j), -(5 + j)]))
    s.append(gmsh.model.geo.addSurfaceFilling([c[1 + k]]))
    c.append(gmsh.model.geo.addCurveLoop([4 + j, 18 + j, -(2 + j), -(8 + j)]))
    s.append(gmsh.model.geo.addSurfaceFilling([c[2 + k]]))
    c.append(gmsh.model.geo.addCurveLoop([3 + j, 17 + j, -(4 + j), -(7 + j)]))
    s.append(gmsh.model.geo.addSurfaceFilling([c[3 + k]]))

sl1 = gmsh.model.geo.addSurfaceLoop(s)
gmsh.model.geo.addVolume([sl1])

gmsh.model.geo.removeAllDuplicates()
gmsh.model.geo.synchronize()
gmsh.model.mesh.generate(3)
gmsh.write("thor.msh")
if '-nopopup' not in sys.argv:
    gmsh.fltk.run()
gmsh.finalize()