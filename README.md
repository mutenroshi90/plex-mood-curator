# 🎬 Plex Mood Curator

An AI-powered Docker container that automatically creates mood-based movie collections in your Plex Media Server. Using ChatGPT, it analyzes your movie library and creates curated lists like "Dark Cyberpunk Thrillers", "Feel-Good Sunday Movies", or "Action-Packed Blockbusters".

## 📜 Disclaimer

**This tool is for personal use only.** By using Plex Mood Curator, you agree to:

- Use your own Plex and OpenAI API credentials
- Comply with [Plex Terms of Service](https://www.plex.tv/about/privacy-legal/plex-terms-of-service/) and [OpenAI Terms of Use](https://openai.com/policies/terms-of-use)
- Use this tool solely for organizing your personal media library
- Not use this for commercial purposes without proper licensing
- Be responsible for any API costs incurred through OpenAI

**No warranty:** This software is provided "as is" without warranty of any kind. The authors are not responsible for any damages or issues arising from its use.

## ✨ Features

- 🤖 **AI-Powered**: Uses OpenAI (GPT-3.5/4) for intelligent movie selection
- 🎭 **Flexible**: Define any mood or theme you want
- 🐳 **Containerized**: Runs isolated in Docker
- 📚 **Multi-Collection**: Create multiple collections simultaneously
- ⚡ **Lightweight**: Slim Python image with minimal dependencies

## 📋 Prerequisites

- Docker & Docker Compose
- Plex Media Server with API access
- OpenAI API Key ([create here](https://platform.openai.com/api-keys))
- Plex Authentication Token ([guide](https://support.plex.tv/articles/204059436-finding-an-authentication-token-x-plex-token/))

## 🚀 Quick Start

```bash
git clone https://github.com/mutenroshi90/plex-mood-curator.git
cd plex-mood-curator

# Create .env file
cp .env.example .env
# Edit .env with your credentials

# Start containers (pulls image from GitHub or builds locally)
docker compose up
```

## ⚙️ Configuration

### Adding Custom Moods

Edit `docker-compose.yml` and add new services:

```yaml
plex-mood-horror:
  image: ghcr.io/mutenroshi90/plex-mood-curator:latest
  build: .
  container_name: plex-mood-horror
  env_file:
    - .env
  environment:
    - MOOD_PROMPT=Terrifying horror movies perfect for Halloween
    - COLLECTION_NAME=🎃 Halloween Horror
    - MAX_MOVIES=15
  restart: "no"
```

### Environment Variables

| Variable | Description | Default | Required |
|----------|-------------|---------|----------|
| `PLEX_URL` | Your Plex server URL | - | ✅ |
| `PLEX_TOKEN` | Plex Authentication Token | - | ✅ |
| `OPENAI_API_KEY` | OpenAI API Key | - | ✅ |
| `LIBRARY_NAME` | Plex library name | `Movies` | ❌ |
| `MOOD_PROMPT` | Description of desired mood | - | ✅ |
| `COLLECTION_NAME` | Collection name in Plex | `MOOD_PROMPT` | ❌ |
| `MAX_MOVIES` | Maximum number of movies | `10` | ❌ |
| `OPENAI_MODEL` | GPT model to use | `gpt-3.5-turbo` | ❌ |

## 🔄 Automation

### Cronjob (Linux/macOS)

```bash
# Run every Friday at 6 PM
0 18 * * 5 cd /path/to/plex-mood-curator && docker compose up
```

### Task Scheduler (Windows)

1. Open Task Scheduler
2. Create new task
3. Trigger: Weekly, Friday 6 PM
4. Action: `docker compose up`
5. Start in: `C:\path\to\plex-mood-curator`

## 🐳 Using GitHub Container Registry

Once you push code to GitHub, GitHub Actions automatically builds a Docker image and uploads it to GHCR.

**Image:** `ghcr.io/mutenroshi90/plex-mood-curator:latest`

The docker-compose.yml is already configured to pull from GHCR when available.

## 🛠️ Development

### Local Testing

```bash
# Install dependencies
pip install -r requirements.txt

# Set environment variables (Linux/macOS)
export PLEX_URL="http://localhost:32400"
export PLEX_TOKEN="your-token"
export OPENAI_API_KEY="your-key"
export MOOD_PROMPT="Test run"

# Run script
python mood_curator.py
```

### Customization Ideas

- Switch OpenAI model (GPT-4 for better results)
- Add filtering by year, genre, or rating
- Implement multi-language support
- Extend logging capabilities

## 📝 License

MIT License - see [LICENSE](LICENSE)

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first.

## ⚠️ Important Notes

- **API Costs**: OpenAI charges per API call. GPT-3.5-turbo is inexpensive (~$0.002/1K tokens)
- **Rate Limits**: OpenAI has rate limits. For large libraries (>1000 movies), consider implementing batching
- **Security**: Treat your tokens like passwords! Never commit `.env` to Git

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/mutenroshi90/plex-mood-curator/issues)
- **Discussions**: [GitHub Discussions](https://github.com/mutenroshi90/plex-mood-curator/discussions)

## 🙏 Credits

Inspired by [PlexAutoSkip](https://github.com/mdhiggins/PlexAutoSkip) and [Kometa](https://github.com/Kometa-Team/Kometa)

---

**Made with ❤️ for the Plex Community**
