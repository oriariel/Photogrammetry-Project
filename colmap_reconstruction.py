import subprocess
import os
import argparse

def run_colmap(command):
    """Run a COLMAP command."""
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

def colmap_reconstruction(project_path, image_path):
    """Run the COLMAP reconstruction pipeline."""
    # Ensure the project path exists
    os.makedirs(project_path, exist_ok=True)

    # Define paths
    database_path = os.path.join(project_path, "database.db")
    sparse_model_path = os.path.join(project_path, "sparse")
    dense_model_path = os.path.join(project_path, "dense")

    # Create directories for models
    os.makedirs(sparse_model_path, exist_ok=True)
    os.makedirs(dense_model_path, exist_ok=True)

    # 1. Feature extraction
    print("Extracting features...")
    run_colmap(f"colmap feature_extractor --database_path {database_path} --image_path {image_path}")

    # 2. Feature matching
    print("Matching features...")
    run_colmap(f"colmap exhaustive_matcher --database_path {database_path}")

    # 3. Sparse reconstruction (mapping)
    print("Running sparse mapper...")
    run_colmap(f"colmap mapper --database_path {database_path} --image_path {image_path} --output_path {sparse_model_path}")

    # 4. Dense reconstruction (optional)
    print("Running dense reconstruction...")
    run_colmap(f"colmap image_undistorter --image_path {image_path} --input_path {sparse_model_path} --output_path {dense_model_path} --output_type COLMAP")

    print("Reconstruction completed.")
    print(f"Sparse model saved in: {sparse_model_path}")
    print(f"Dense model saved in: {dense_model_path}")
    print(f"Database saved in: {database_path}")

if __name__ == "__main__":
    # Set up argument parsing
    parser = argparse.ArgumentParser(description='Run COLMAP reconstruction pipeline.')
    parser.add_argument('project_path', type=str, help='Path to the project directory.')
    parser.add_argument('image_path', type=str, help='Path to the directory containing images.')

    args = parser.parse_args()

    colmap_reconstruction(args.project_path, args.image_path)
