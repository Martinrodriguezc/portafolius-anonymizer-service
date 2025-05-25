import cv2

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
