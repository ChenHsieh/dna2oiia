import subprocess
import sys

def mp4_to_gif(input_mp4, output_gif, fps=10, scale=500):
    """
    Converts an MP4 file to a GIF.
    
    Parameters:
    - input_mp4 (str): Path to the input MP4 file.
    - output_gif (str): Path to save the output GIF file.
    - fps (int): Frames per second for the GIF (lower means smaller file).
    - scale (int): Width of the GIF (height adjusts to keep aspect ratio).
    """
    command = [
        "ffmpeg",
        "-i", input_mp4,
        "-vf", f"fps={fps},scale={scale}:-1:flags=lanczos",
        "-c:v", "gif",
        output_gif
    ]
    subprocess.run(command, check=True)
    print(f"🎥 Converted {input_mp4} → {output_gif}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python convert_mp4_to_gif.py input.mp4 output.gif")
        sys.exit(1)
    
    mp4_to_gif(sys.argv[1], sys.argv[2])