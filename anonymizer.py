import cv2
import subprocess

def anonymize_video(input_path, output_path):
    cap = cv2.VideoCapture(input_path)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, fps if fps > 0 else 20.0, (width, height))
    
    franja_alta = 80  # px, puedes aumentar o disminuir
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame[0:franja_alta, :] = 0  # negro en la franja de arriba

        out.write(frame)
    cap.release()
    out.release()

def convert_to_compatible(input_path, output_path):
    # Convierte a mp4 universal (video H.264, audio AAC)
    cmd = [
        "ffmpeg", "-y", "-i", input_path,
        "-c:v", "libx264", "-preset", "veryfast", "-crf", "23",
        "-c:a", "aac", "-b:a", "128k",
        "-movflags", "+faststart",
        output_path
    ]
    subprocess.run(cmd, check=True)
