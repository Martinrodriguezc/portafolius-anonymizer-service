<# Video Anonymizer Microservice

Microservicio en Python para **anonimizar videos médicos** (ej: ecografías), eliminando datos sensibles como nombres, RUT, fechas y otros identificadores visuales, mediante censura de áreas predefinidas en los videos.

## Características

- Recibe videos por API y devuelve una versión anonimizada.
- Censura automática de la franja superior donde aparecen los datos sensibles.
- Implementado en **FastAPI** para endpoints rápidos y documentados.
- Procesamiento de video con **OpenCV**.
- Compatible con integración a sistemas frontend y backend en Node.js, Express, etc.

## Requisitos

- Python 3.8 o superior
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) instalado en el sistema (solo si usas OCR, opcional en la versión de franjas fijas)
- Dependencias Python (ver más abajo)

## Instalación

1. **Clona este repositorio:**
    ```bash
    git clone https://github.com/Martinrodriguezc/portafolius-anonymizer-service.git
    cd portafolius-anonymizer-service
    ```

2. **Crea y activa un entorno virtual:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Instala dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

4. **(Opcional, solo si usas OCR) Instala Tesseract OCR:**

    - En MacOS: `brew install tesseract`
    - En Ubuntu/Debian: `sudo apt-get install tesseract-ocr`
    - En Windows: [Descarga aquí](https://github.com/tesseract-ocr/tesseract/wiki)

## Uso

1. **Corre el microservicio:**
    ```bash
    uvicorn main:app --reload
    ```

2. **Accede a la documentación automática:**
    - [http://localhost:8000/docs](http://localhost:8000/docs)

3. **Sube un video usando el endpoint `/anonimize-video`** y descarga el video anonimizado.

### Ejemplo de request con `curl`:

```bash
curl -X POST "http://localhost:8000/anonimize-video" \
  -F "file=@/ruta/al/video.mp4" \
  --output anonimizado.mp4
