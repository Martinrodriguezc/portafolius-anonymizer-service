from fastapi import FastAPI, File, UploadFile, BackgroundTasks
from fastapi.responses import FileResponse
import os
from anonymizer import anonymize_video

app = FastAPI()
TEMP_DIR = "temp"
os.makedirs(TEMP_DIR, exist_ok=True)

@app.post("/anonimize-video")
async def anonimize_video_endpoint(
    file: UploadFile = File(...),
    background_tasks: BackgroundTasks = None
):
    input_path = os.path.join(TEMP_DIR, file.filename)
    output_filename = "anonymized_" + file.filename
    output_path = os.path.join(TEMP_DIR, output_filename)

    print(f"[INFO] Guardando archivo subido en {input_path}")
    with open(input_path, "wb") as f:
        f.write(await file.read())

    anonymize_video(input_path, output_path)

    # Limpieza automática después de responder
    def cleanup_files():
        print(f"[INFO] Borrando archivos temporales: {input_path}, {output_path}")
        try:
            os.remove(input_path)
        except FileNotFoundError:
            pass
        try:
            os.remove(output_path)
        except FileNotFoundError:
            pass

    background_tasks.add_task(cleanup_files)

    # Verifica que el archivo de salida realmente exista
    if not os.path.exists(output_path):
        print("[ERROR] El archivo anonimizado no se generó correctamente.")
        from fastapi import HTTPException
        raise HTTPException(status_code=500, detail="Error al procesar el video.")

    return FileResponse(output_path, filename=output_filename)
