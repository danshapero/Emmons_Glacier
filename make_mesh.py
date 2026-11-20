import geojson
import icepack

outline_filename = "emmons_1896.geojson"
with open(outline_filename, "r") as outline_file:
    outline = geojson.load(outline_file)

gmsh_mesh = icepack.meshing.collection_to_gmsh(outline)
gmsh_mesh.write("emmons.msh", verbose=False)


