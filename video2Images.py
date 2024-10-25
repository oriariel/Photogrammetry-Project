import cv2
import os
import argparse

def extract_frames(video_path, output_dir, step=30):
    """
    Extracts frames from a video and saves them as images in the specified output directory.

    Args:
    - video_path (str): Path to the video file.
    - output_dir (str): Directory where the extracted frames will be saved.
    - step (int): Step size for frame extraction (i.e., extract every nth frame).

    Returns:
    - None
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    cap = cv2.VideoCapture(video_path)
    count = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        if count % step == 0:
            filename = os.path.join(output_dir, f'frame_{count}.jpg')
            cv2.imwrite(filename, frame)

        count += 1

    cap.release()
    print(f"Frames saved to {output_dir}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract frames from video")
    parser.add_argument("video_path", help="")
    parser.add_argument("output_dir", help="")
    parser.add_argument("--step", type=int, default=30, help="Frame extraction step")
    args = parser.parse_args()

    extract_frames(args.video_path, args.output_dir, args.step)
