import subprocess
import sys

def video_to_gif(input_video, output_gif, fps=10, scale=500):
    """
    Converts a video file (MP4 or MOV) to a GIF.
    
    Parameters:
    - input_video (str): Path to the input video file (MP4 or MOV).
    - output_gif (str): Path to save the output GIF file.
    - fps (int): Frames per second for the GIF (lower means smaller file).
    - scale (int): Width of the GIF (height adjusts to keep aspect ratio).
    """
    command = [
        "ffmpeg",
        "-i", input_video,
        "-vf", f"fps={fps},scale={scale}:-1:flags=lanczos",
        "-c:v", "gif",
        output_gif
    ]
    subprocess.run(command, check=True)
    print(f"🎥 Converted {input_video} → {output_gif}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python convert_video_to_gif.py input.mp4|input.mov output.gif")
        sys.exit(1)
    
    video_to_gif(sys.argv[1], sys.argv[2])