## Project Overview

This project aims to create a detailed and accurate 3D point cloud model using video footage. The process involves extracting frames from videos, generating point clouds using COLMAP, and merging these clouds using CloudCompare’s CLI. This workflow is optimized for efficient photogrammetry and enables the creation of comprehensive 3D representations.

## Objectives

1. **Video Frame Extraction**: Extract frames from video files to generate images optimized for 3D point cloud creation.
2. **Point Cloud Generation**: Use COLMAP to create point clouds from the extracted frames.
3. **Point Cloud Merging**: Merge the generated point clouds into a single unified cloud using CloudCompare's CLI.

## Prerequisites

- **Python** with OpenCV library for frame extraction.
- **COLMAP** for point cloud creation.
- **CloudCompare** CLI for merging point clouds.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/oriariel/Photogrammetry-Project.git
   ```
2. Install the required Python packages:
   ```bash
   pip install opencv-python
   ```
3. Ensure COLMAP and CloudCompare CLI are installed on your system.

## Usage

### Step 1: Frame Extraction from Video

Run the `video2Images.py` tool to extract frames:
   ```bash
   python video2Images.py <video_path> <output_dir> --step <frame_step>
   ```
   - `<video_path>`: Path to the input video file.
   - `<output_dir>`: Directory to save extracted frames.
   - `--step`: Interval between frames (e.g., every 50th frame).

Example:
   ```bash
   python video2Images.py ./input/video.mp4 ./output/images --step 50
   ```

### Step 2: Generate Point Clouds with COLMAP

1. Import the extracted frames into COLMAP.
2. Run COLMAP’s pipeline for Structure-from-Motion (SfM) and Multi-View Stereo (MVS) to create point clouds from images.

Save the point clouds as `.ply` files (e.g., `p1.ply`, `p2.ply`).

### Step 3: Merge Point Clouds using CloudCompare CLI

Use the following command to merge the point clouds:
   ```bash
   CloudCompare -O p1.ply -O p2.ply -ICP -MERGE_CLOUDS -C_EXPORT_FMT PLY -PLY_EXPORT_FMT ASCII -SAVE_CLOUDS FILE merged_cloud.ply
   ```
   This merges the clouds generated from each video set into a unified cloud, which is saved as `merged_cloud.ply`.
  or run the `merged_clouds.py` using the following command in your terminal:
   ```bash
   python merge_clouds.py <p1.ply> <p2.ply> <output.ply>
   ```
   Parameters
   <p1.ply>: Path to the first input point cloud file.
   <p2.ply>: Path to the second input point cloud file.
   <output.ply>: Path where the merged point cloud will be saved.

## Results

- Successfully generated and merged 3D point clouds for further analysis and visualization.
- Verified alignment accuracy using CloudCompare's GUI and eliminated any outliers for a cleaner model.

Project Report in Overleaf:
https://www.overleaf.com/read/dqjdqzsbnmbf#246981
