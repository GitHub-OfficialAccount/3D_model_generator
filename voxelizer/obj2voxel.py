import subprocess

resolution = 32

obj_file = "chess" + ".obj"
vox_file = "chess-1" + ".vox"

executable = "voxelizer\obj2voxel.exe"
args = f"{obj_file} {vox_file} -r {resolution}"

command = executable + " " + args

subprocess.run(command, shell=True)