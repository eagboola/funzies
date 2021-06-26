# inputs: domain/min & max
# outputs: coordinates to a linze that is horizontal to reference frame

import math
import random as rdm
import Rhino
import Grasshopper as gh
import rhinoscriptsyntax as rs
import ghpythonlib.components as ghcomp



ranodLs = []

# X-axis line coordinates
Xls = [] # list of lines moving in X direction
Xpts0 = [] # list of starting points for X lines
Xpts1 = [] # list of endpoints for X lines

# Y-axis line coordinates
Yls = [] # list of lines moving in Y direction
Ypts0 = [] # list of starting points for Y lines
Ypts1 = [] # list of endpoints for Y lines

# Z-axis line coordinates
Zls = [] # list of line moving in Z
Zpts0 = [] # list of starting points for Z lines
Zpts1 = [] # list of endpoints for Z lines

# Planes
pls = []

# Rectangles
recs = []

# X-AXIS PERPENDICULAR LINES
for i in range(int(min), int(n)):
    # random number between 0 and input 'max'
    x0 = int(rdm.uniform(0, max))
    y0 = int(rdm.uniform(0, max))
    z0 = int(rdm.uniform(0, max))
    
    
    x1 = x0 + int(rdm.uniform(minLength, maxLength))
    y1 = y0
    z1 = z0
    
    start = Rhino.Geometry.Point3d(x0, y0, z0)
    Xpts0.append(start)
    stop = Rhino.Geometry.Point3d(x1, y1, z1)
    Xpts1.append(stop)
    
    l = Rhino.Geometry.Line(start, stop)
    Xls.append(l)
    



# move through x0s and x1s as pairs and create new random number between the pair for Yline(s)
m = int(rdm.uniform(int(n*.1), int(n*.42)))


# Y-AXIS PERPENDICULAR LINES

for i in range(int(min), int(n)):
    # random x coordinate number between x0 and x1 of previous line
    x0 = int(rdm.uniform(Xpts0[i].X, Xpts1[i].X))
    y0 = int(rdm.uniform(Xpts0[i].Y, Xpts1[i].Y))
    z0 = int(rdm.uniform(Xpts0[i].Z, Xpts1[i].Z))
    
    
    x1 = x0
    y1 = y0 + int(rdm.uniform(minLength, maxLength))
    z1 = z0
    
    start = Rhino.Geometry.Point3d(x0, y0, z0)
    Ypts0.append(start)
    stop = Rhino.Geometry.Point3d(x1, y1, z1)
    Ypts1.append(stop)
    l = Rhino.Geometry.Line(start, stop)
    Yls.append(l)


# Z-AXIS PERPENDICULAR LINES

for i in range(int(min), int(n)):
    x0 = int(rdm.uniform(Ypts0[i].X, Ypts1[i].X))
    y0 = int(rdm.uniform(Ypts0[i].Y, Ypts1[i].Y))
    z0 = int(rdm.uniform(Ypts0[i].Z, Ypts1[i].Z))
    
    x1 = x0
    y1 = y0
    z1 = z0 + int(rdm.uniform(minLength, maxLength))
    
    start = Rhino.Geometry.Point3d(x0, y0, z0)
    Zpts0.append(start)
    stop = Rhino.Geometry.Point3d(x1, y1, z1)
    Zpts1.append(stop)
    l = Rhino.Geometry.Line(start, stop)
    Zls.append(l)
    

vs= []
for i in range(0, len(Xls)):
    v = Rhino.Geometry.Vector3d(Xpts1[i].X, Xpts1[i].Y-30, Xpts1[i].Z)
    vs.append(v)
    #Rhino.Geometry.Vector3d(
    #Rhino.Geometry.Plane(
    r = rs.AddRectangle(Rhino.Geometry.Plane(Xpts0[i], v), 2, 1)
    # ghcomp.Area(r)
    # Rhino.RhinoApp.GetType(r)
    recs.append(r)
    # print(str(Xpts1[1].X))
