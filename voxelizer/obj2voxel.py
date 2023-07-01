import subprocess

resolution = 256

obj_file = "base" + ".obj"
vox_file = "base-1" + ".vox"

executable = "voxelizer\obj2voxel.exe"
args = f"{obj_file} {vox_file} -r {resolution}"

command = executable + " " + args

subprocess.run(command, shell=True)