import meshio

# Convert STL to OBJ
mesh = meshio.read("3D-models/Chess/WCC_King.stl")
meshio.write('chess.obj', mesh, file_format='obj')