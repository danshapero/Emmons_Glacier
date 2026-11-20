import rasterio
import firedrake
import icepack

# Read the mesh
mesh = firedrake.Mesh("emmons.msh")

# Make function spaces
dg1 = firedrake.FiniteElement("DG", "triangle", 1)
cg1 = firedrake.FiniteElement("CG", "triangle", 1)

S = firedrake.FunctionSpace(mesh, cg1)
Q = firedrake.FunctionSpace(mesh, dg1)
V = firedrake.VectorFunctionSpace(mesh, cg1)

# Read in the bed data
bed_filename = "basalsurf-32610.tif"
with rasterio.open(bed_filename, "r") as bed_file:
    b = icepack.interpolate(bed_file, S)

import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.set_aspect("equal")
ax.set_axis_off()
colors = firedrake.tripcolor(b, cmap="Blues_r", axes=ax)
fig.colorbar(colors)
plt.show()
