import meshio

# Convert PLY to STL
mesh = meshio.read('test_vox.ply')
meshio.write('test1.stl', mesh, file_format='stl')