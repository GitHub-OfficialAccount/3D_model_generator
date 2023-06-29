import meshio

# Convert OBJ to STL
mesh = meshio.read('input.obj')
meshio.write('output.stl', mesh, file_format='stl')