# 🎬 Plex Mood Curator

Ein KI-gesteuerter Docker-Container, der automatisch stimmungsbasierte Film-Kollektionen in deinem Plex Media Server erstellt. Mit ChatGPT analysiert er deine Filmsammlung und erstellt kuratierte Listen wie "Düstere Cyberpunk-Thriller", "Wohlfühlfilme für Sonntage" oder "Actionreiche Blockbuster".

## ✨ Features

- 🤖 **KI-gesteuert**: Nutzt OpenAI (GPT-3.5/4) zur intelligenten Film-Auswahl
- 🎭 **Flexibel**: Definiere beliebige Stimmungen und Themen
- 🐳 **Containerisiert**: Läuft isoliert in Docker
- 📚 **Multi-Collection**: Erstelle mehrere Kollektionen gleichzeitig
- ⚡ **Leichtgewichtig**: Schlankes Python-Image mit minimalen Abhängigkeiten

## 📋 Voraussetzungen

- Docker & Docker Compose
- Plex Media Server mit API-Zugriff
- OpenAI API-Key ([hier erstellen](https://platform.openai.com/api-keys))
- Plex Authentication Token ([Anleitung](https://support.plex.tv/articles/204059436-finding-an-authentication-token-x-plex-token/))

## 🚀 Schnellstart

```bash
git clone https://github.com/mutenroshi90/plex-mood-curator.git
cd plex-mood-curator

# .env erstellen
cp .env.example .env
# Bearbeite .env mit deinen Daten

# Container starten (lädt Image von GitHub oder baut lokal)
docker compose up
```

## ⚙️ Konfiguration

### Eigene Stimmungen hinzufügen

Bearbeite die `docker-compose.yml` und füge neue Services hinzu:

```yaml
plex-mood-horror:
  build: .
  container_name: plex-mood-horror
  environment:
    - PLEX_URL=${PLEX_URL}
    - PLEX_TOKEN=${PLEX_TOKEN}
    - OPENAI_API_KEY=${OPENAI_API_KEY}
    - LIBRARY_NAME=${LIBRARY_NAME:-Filme}
    - MOOD_PROMPT=Erschreckende Horror-Filme für Halloween
    - COLLECTION_NAME=🎃 Halloween Horror
    - MAX_MOVIES=15
  restart: "no"
```

### Umgebungsvariablen

| Variable | Beschreibung | Standard | Pflicht |
|----------|--------------|----------|---------|
| `PLEX_URL` | URL deines Plex-Servers | - | ✅ |
| `PLEX_TOKEN` | Plex Authentication Token | - | ✅ |
| `OPENAI_API_KEY` | OpenAI API-Schlüssel | - | ✅ |
| `LIBRARY_NAME` | Name der Plex-Bibliothek | `Filme` | ❌ |
| `MOOD_PROMPT` | Beschreibung der gewünschten Stimmung | - | ✅ |
| `COLLECTION_NAME` | Name der Kollektion in Plex | `MOOD_PROMPT` | ❌ |
| `MAX_MOVIES` | Maximale Anzahl Filme | `10` | ❌ |
| `OPENAI_MODEL` | GPT-Modell | `gpt-3.5-turbo` | ❌ |

## 🔄 Automatisierung

### Cronjob (Linux/macOS)

```bash
# Jeden Freitag um 18:00 Uhr ausführen
0 18 * * 5 cd /pfad/zu/plex-mood-curator && docker compose up --build
```

### Task Scheduler (Windows)

1. Öffne Task Scheduler
2. Erstelle neue Aufgabe
3. Trigger: Wöchentlich, Freitag 18:00
4. Aktion: `docker compose up --build`
5. Startverzeichnis: `C:\pfad\zu\plex-mood-curator`

## 🐳 Von GitHub Registry verwenden

Sobald du Code zu GitHub pushst, baut GitHub Actions automatisch ein Docker-Image und lädt es in die GitHub Container Registry (GHCR) hoch.

**Auf deinem Server:**

```yaml
services:
  plex-mood-thriller:
    image: ghcr.io/mutenroshi90/plex-mood-curator:latest
    environment:
      - PLEX_URL=${PLEX_URL}
      # ... restliche Konfiguration
```

Das Image ist **privat** - nur du hast Zugriff darauf!

## 🛠️ Entwicklung

### Lokales Testen

```bash
# Dependencies installieren
pip install -r requirements.txt

# Umgebungsvariablen setzen (Linux/macOS)
export PLEX_URL="http://localhost:32400"
export PLEX_TOKEN="dein-token"
export OPENAI_API_KEY="dein-key"
export MOOD_PROMPT="Testlauf"

# Skript ausführen
python mood_curator.py
```

### Eigene Modifikationen

Das Projekt ist bewusst einfach gehalten. Du kannst:
- Das OpenAI-Modell wechseln (GPT-4 für bessere Ergebnisse)
- Weitere Filtermethoden hinzufügen (z.B. nach Jahr, Genre)
- Mehrsprachigkeit implementieren
- Logging erweitern

## 📝 Lizenz

MIT License - siehe [LICENSE](LICENSE)

## 🤝 Beitragen

Pull Requests sind willkommen! Für größere Änderungen öffne bitte zuerst ein Issue.

## ⚠️ Hinweise

- **API-Kosten**: OpenAI berechnet pro API-Aufruf. GPT-3.5-turbo ist günstig (~$0.002/1K tokens)
- **Rate Limits**: OpenAI hat Rate-Limits. Für große Bibliotheken (>1000 Filme) eventuell Batching implementieren
- **Plex-Token**: Behandle deinen Token wie ein Passwort! Committe **niemals** die `.env` zu Git

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/dein-username/plex-mood-curator/issues)
- **Diskussionen**: [GitHub Discussions](https://github.com/dein-username/plex-mood-curator/discussions)

## 🙏 Credits

Inspiriert von [PlexAutoSkip](https://github.com/mdhiggins/PlexAutoSkip) und [Kometa](https://github.com/Kometa-Team/Kometa)

---

**Made with ❤️ for the Plex Community**
