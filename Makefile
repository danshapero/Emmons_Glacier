basalsurf-32610.tif: basalsurf.tif
	rio warp $< --output $@ --dst-crs EPSG:32610

emmons.msh: make_mesh.py
	python $<

all: spin_up.py emmons.msh basalsurf-32610.tif
	python $<
