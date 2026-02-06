# 🎯 Integration in bestehende docker-compose.yml

Du hast bereits eine docker-compose.yml? Kein Problem! Kopiere einfach die Services aus `docker-compose.production.yml` in deine bestehende Datei.

## Beispiel-Integration

```yaml
services:
  # Deine bestehenden Services
  plex:
    image: plexinc/pms-docker
    # ... deine Config

  # Füge die Plex Mood Curator Services hinzu:
  plex-mood-acclaimed:
    image: ghcr.io/mutenroshi90/plex-mood-curator:latest
    container_name: plex-mood-acclaimed
    env_file:
      - .env
    environment:
      - MOOD_PROMPT=Von der Kritik hochgelobte Meisterwerke
      - COLLECTION_NAME=🏆 Von der Kritik gelobte Filme
      - MAX_MOVIES=20
    restart: "no"

  # ... restliche Mood Curator Services
```

## Eigene Stimmungen hinzufügen

Kopiere einen Service-Block und passe an:

```yaml
  plex-mood-horror:
    image: ghcr.io/mutenroshi90/plex-mood-curator:latest
    container_name: plex-mood-horror
    env_file:
      - .env
    environment:
      - MOOD_PROMPT=Gruselige Horror-Filme für Halloween
      - COLLECTION_NAME=🎃 Halloween Horror
      - MAX_MOVIES=15
    restart: "no"
```

## .env Datei

Stelle sicher, dass deine `.env` diese Werte enthält:

```env
PLEX_URL=http://192.168.1.100:32400
PLEX_TOKEN=dein-plex-token
OPENAI_API_KEY=sk-dein-openai-key
OPENAI_MODEL=gpt-3.5-turbo
LIBRARY_NAME=Filme
```

## Updates

Image aktualisieren:
```bash
docker compose pull plex-mood-acclaimed
docker compose up -d plex-mood-acclaimed
```

Alle Mood Curator Services neu starten:
```bash
docker compose pull
docker compose up -d plex-mood-acclaimed plex-mood-dystopian plex-mood-action plex-mood-short plex-mood-date plex-mood-animation plex-mood-feelgood plex-mood-trending
```
