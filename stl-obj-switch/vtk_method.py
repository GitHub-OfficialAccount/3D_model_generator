import vtk

# Set paths to input/output files
input_file = "test_vox.vl32"
output_file = "test_vox2.stl"

# Read in the input VL32 file
reader = vtk.vtkVL32Reader()
reader.SetFileName(input_file)
reader.Update()

# Convert to polydata
surface_filter = vtk.vtkDataSetSurfaceFilter()
surface_filter.SetInputData(reader.GetOutput())
surface_filter.Update()

# Write output STL file
writer = vtk.vtkSTLWriter()
writer.SetFileName(output_file)
writer.SetInputData(surface_filter.GetOutput())
writer.Write()