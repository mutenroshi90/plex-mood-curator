# Schlankes Python-Image als Basis
FROM python:3.11-slim

# Metadata
LABEL maintainer="Plex Mood Curator"
LABEL description="Erstellt KI-basierte, stimmungsabhängige Film-Kollektionen in Plex"

# Arbeitsverzeichnis im Container
WORKDIR /app

# Requirements-Datei kopieren und Abhängigkeiten installieren
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Skript kopieren
COPY mood_curator.py .

# Skript ausführbar machen
RUN chmod +x mood_curator.py

# Beim Start ausführen
CMD ["python", "mood_curator.py"]
