FROM python:3.10-slim

# Instala ffmpeg junto con las otras dependencias del sistema
RUN apt-get update \
 && apt-get install -y --no-install-recommends \
      gcc \
      libgl1 \
      libglib2.0-0 \
      libsm6 \
      libxrender1 \
      libxext6 \
      ffmpeg \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
