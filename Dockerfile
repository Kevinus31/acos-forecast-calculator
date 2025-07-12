# Użyj oficjalnego obrazu Python 3.11 slim
FROM python:3.11-slim

# Ustaw zmienne środowiskowe
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Ustaw katalog roboczy
WORKDIR /code

# Skopiuj plik requirements.txt
COPY requirements.txt .

# Zainstaluj zależności
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Skopiuj kod aplikacji
COPY app/ ./app/

# Ustaw port
EXPOSE 8000

# Komenda uruchomienia aplikacji
CMD ["sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000}"] 