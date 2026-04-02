# Aurex AI - Intelligent Voice Assistant

An advanced AI-powered voice assistant with real-time search, image generation, automation, and natural language processing capabilities.

## Features

- 🎤 **Voice Interaction** - Speech-to-text and text-to-speech capabilities
- 🤖 **AI Chatbot** - Powered by advanced language models
- 🖼️ **Image Generation** - Generate images from text descriptions
- 🔍 **Real-time Search** - Get current information from the internet
- 🎮 **GUI Interface** - User-friendly graphical interface
- ⚙️ **Automation** - Automate system tasks and applications
- 🌐 **Multi-language Support** - Translate and understand multiple languages

## Project Structure

```
aurex-ai/
├── Backend/
│   ├── Chatbot.py              # AI Chatbot implementation
│   ├── Model.py                # Language model interface
│   ├── ImageGeneration.py       # Image generation module
│   ├── SpeechToText.py          # Speech recognition
│   ├── TextToSpeech.py          # Text-to-speech synthesis
│   ├── RealtimeSearchEngine.py  # Web search functionality
│   └── Automation.py            # System automation
├── Frontend/
│   ├── GUI.py                   # Graphical User Interface
│   ├── Files/                   # Data persistence files
│   └── Graphics/                # UI graphics and assets
├── Data/
│   ├── ChatLog.json             # Chat history
│   └── [images, audio files]    # Generated media
├── Main.py                      # Application entry point
├── Requirements.txt             # Python dependencies
└── .env                         # Environment configuration (create from .env.example)
```

## Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager
- Virtual environment (recommended)

### Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/tanishqagrawal-dev/aurex-ai.git
   cd aurex-ai
   ```

2. **Create a virtual environment** (optional but recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r Requirements.txt
   ```

4. **Configure environment variables**
   ```bash
   cp .env.example .env
   # Edit .env and add your API keys and configuration
   ```

5. **Run the application**
   ```bash
   python Main.py
   ```

## Dependencies

All required packages are listed in `Requirements.txt`:
- **python-dotenv** - Environment variable management
- **groq** - Groq API for AI models
- **AppOpener** - Application launcher
- **pywhatkit** - YouTube and search automation
- **PyQt5** - GUI framework
- **edge-tts** - Text-to-speech
- **selenium** - Web automation
- **bs4** - Web scraping
- And more (see Requirements.txt)

## Configuration

### Environment Variables

Create a `.env` file based on `.env.example` with the following variables:

```env
Username=your_name
Assistantname=Aurex
GROQ_API_KEY=your_groq_key
COHERE_API_KEY=your_cohere_key
```

## Usage

### Launch GUI
```bash
python Main.py
```

### Test Specific Modules
```bash
python test_api.py           # Test API connectivity
python test_modules.py       # Test module imports
python test_image_trigger.py # Test image generation
python test_hf_api.py        # Test Hugging Face API
```

## Troubleshooting

### Missing Dependencies
If you encounter import errors:
```bash
pip install -r Requirements.txt --upgrade
```

### API Key Issues
- Ensure all required API keys are set in `.env`
- Check that your API keys are valid and have proper permissions

### Speech Recognition Issues
- Ensure your microphone is working and properly configured
- Check system audio settings

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bugs and feature requests.

## License

[Add your license here]

## Author

[Your Name/Organization]

---

**Note:** Make sure to keep your `.env` file secure and never commit it to version control. Use `.env.example` for sharing configuration templates.
