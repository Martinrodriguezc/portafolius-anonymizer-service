from fastapi import FastAPI, File, UploadFile, BackgroundTasks
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import os
from anonymizer import anonymize_video, convert_to_compatible

app = FastAPI()
TEMP_DIR = "temp"
os.makedirs(TEMP_DIR, exist_ok=True)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "https://portafolius-dev.netlify.app"],
    allow_credentials=True,
    allow_methods=["*"],    
    allow_headers=["*"],    
)

@app.post("/anonimize-video")
async def anonimize_video_endpoint(
    file: UploadFile = File(...),
    background_tasks: BackgroundTasks = None
):
    input_path = os.path.join(TEMP_DIR, file.filename)
    anonymized_path = os.path.join(TEMP_DIR, "anonymized_" + file.filename)
    converted_path = os.path.join(TEMP_DIR, "converted_" + file.filename)

    print(f"[INFO] Guardando archivo subido en {input_path}")
    with open(input_path, "wb") as f:
        f.write(await file.read())

    # Anonimiza
    anonymize_video(input_path, anonymized_path)
    # Convierte a mp4 compatible
    convert_to_compatible(anonymized_path, converted_path)

    # Limpieza automática después de responder
    def cleanup_files():
        print(f"[INFO] Borrando archivos temporales: {input_path}, {anonymized_path}, {converted_path}")
        for p in [input_path, anonymized_path, converted_path]:
            try:
                os.remove(p)
            except FileNotFoundError:
                pass

    background_tasks.add_task(cleanup_files)

    # Verifica que el archivo de salida realmente exista
    if not os.path.exists(converted_path):
        print("[ERROR] El archivo convertido no se generó correctamente.")
        from fastapi import HTTPException
        raise HTTPException(status_code=500, detail="Error al procesar el video.")

    return FileResponse(converted_path, filename="converted_" + file.filename)
