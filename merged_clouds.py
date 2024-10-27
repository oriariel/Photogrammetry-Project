import subprocess
import os
import sys

# Define the paths to the input files from command line arguments
if len(sys.argv) != 4:
    print("Usage: python merge_clouds.py <point_cloud1.ply> <point_cloud2.ply> <merged_clouds.ply>")
    sys.exit(1)

p1_path = sys.argv[1]
p2_path = sys.argv[2]
output_path = sys.argv[3]

# Ensure the input files exist
if not os.path.isfile(p1_path):
    raise FileNotFoundError(f"File not found: {p1_path}")
if not os.path.isfile(p2_path):
    raise FileNotFoundError(f"File not found: {p2_path}")

# Define the command as a list
command = [
    "cloudcompare",
    "-o", p1_path,
    "-o", p2_path,
    "-ICP",
    "-MERGE_CLOUDS",
    "-C_EXPORT_FMT", "PLY",
    "-PLY_EXPORT_FMT", "ASCII",
    "-SAVE_CLOUDS", "FILE", output_path
]

try:
    subprocess.run(command, check=True)
    print(f"Clouds merged successfully into {output_path}")
except subprocess.CalledProcessError as e:
    print(f"An error occurred: {e}")
