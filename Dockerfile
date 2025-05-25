FROM python:3.10-slim

# Instala dependencias del sistema (descomenta la línea siguiente si necesitas OCR)
# RUN apt-get update && apt-get install -y tesseract-ocr && apt-get clean

WORKDIR /app

# Copia los archivos de dependencias primero
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del código
COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
