#!/usr/bin/env python3
"""
Plex Mood Curator - Erstellt stimmungsbasierte Film-Kollektionen
"""
import os
import sys
from plexapi.server import PlexServer
from openai import OpenAI

# Umgebungsvariablen laden
PLEX_URL = os.getenv('PLEX_URL')
PLEX_TOKEN = os.getenv('PLEX_TOKEN')
OPENAI_KEY = os.getenv('OPENAI_API_KEY')
LIBRARY_NAME = os.getenv('LIBRARY_NAME', 'Filme')
MOOD_PROMPT = os.getenv('MOOD_PROMPT', 'Spannende Thriller für einen düsteren Abend')
COLLECTION_NAME = os.getenv('COLLECTION_NAME', MOOD_PROMPT)
MAX_MOVIES = int(os.getenv('MAX_MOVIES', '10'))
OPENAI_MODEL = os.getenv('OPENAI_MODEL', 'gpt-3.5-turbo')

def validate_environment():
    """Prüft, ob alle erforderlichen Umgebungsvariablen gesetzt sind"""
    required_vars = {
        'PLEX_URL': PLEX_URL,
        'PLEX_TOKEN': PLEX_TOKEN,
        'OPENAI_API_KEY': OPENAI_KEY
    }
    
    missing = [key for key, value in required_vars.items() if not value]
    
    if missing:
        print(f"❌ Fehler: Folgende Umgebungsvariablen fehlen: {', '.join(missing)}")
        sys.exit(1)

def create_mood_collection():
    """Hauptfunktion: Erstellt eine stimmungsbasierte Kollektion"""
    print(f"🎬 Plex Mood Curator gestartet")
    print(f"📚 Bibliothek: {LIBRARY_NAME}")
    print(f"🎭 Stimmung: {MOOD_PROMPT}")
    print(f"📝 Kollektionsname: {COLLECTION_NAME}")
    print("-" * 50)
    
    try:
        # Mit Plex verbinden
        print(f"🔌 Verbinde mit Plex-Server...")
        plex = PlexServer(PLEX_URL, PLEX_TOKEN)
        library = plex.library.section(LIBRARY_NAME)
        
        # Alle Filme abrufen
        print(f"📥 Lade Filme aus Bibliothek...")
        all_movies = library.all()
        movie_titles = [m.title for m in all_movies]
        print(f"✅ {len(movie_titles)} Filme gefunden")
        
        if not movie_titles:
            print("⚠️  Keine Filme in der Bibliothek gefunden!")
            return
        
        # OpenAI-Client initialisieren
        print(f"🤖 Frage KI nach passenden Filmen...")
        client = OpenAI(api_key=OPENAI_KEY)
        
        # KI-Prompt erstellen
        prompt = f"""Hier ist eine Liste von Filmen: {', '.join(movie_titles)}

Wähle die {MAX_MOVIES} Filme aus, die am besten zur folgenden Stimmung/Beschreibung passen:
"{MOOD_PROMPT}"

Antworte NUR mit den exakten Filmtiteln aus der Liste, getrennt durch Kommas. Keine weiteren Erklärungen."""
        
        # KI-Anfrage
        response = client.chat.completions.create(
            model=OPENAI_MODEL,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )
        
        # Antwort verarbeiten
        recommended_titles_raw = response.choices[0].message.content
        recommended_titles = [title.strip() for title in recommended_titles_raw.split(',')]
        
        print(f"✅ KI hat {len(recommended_titles)} Filme empfohlen")
        
        # Kollektion erstellen/aktualisieren
        print(f"📌 Erstelle Kollektion '{COLLECTION_NAME}'...")
        added_count = 0
        
        for title in recommended_titles:
            try:
                # Versuche Film zu finden (exakte Übereinstimmung)
                movie = library.get(title)
                movie.addCollection(COLLECTION_NAME)
                print(f"  ✓ {title}")
                added_count += 1
            except Exception as e:
                print(f"  ⚠️  '{title}' nicht gefunden oder Fehler: {str(e)}")
                continue
        
        print("-" * 50)
        print(f"✨ Fertig! {added_count} Filme zur Kollektion '{COLLECTION_NAME}' hinzugefügt")
        
    except Exception as e:
        print(f"❌ Fehler: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    validate_environment()
    create_mood_collection()
