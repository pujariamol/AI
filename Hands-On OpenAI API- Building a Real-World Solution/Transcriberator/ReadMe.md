# Audio Transcription and Translation Tool

This project provides two options for transcribing audio files and translating them to English:
1. OpenAI Whisper API
2. Google Gemini API

## Prerequisites

- Python 3.7+
- pip (Python package installer)

## Installation

1. Clone this repository
2. Install the required packages:

```bash
pip install openai google-generativeai python-dotenv
```

3. Set up your environment variables:
   Create a `.env` file in the project root and add your API keys:

```bash
OPENAI_API_KEY=your_openai_api_key_here
GEMINI_API_KEY=your_gemini_api_key_here
```

## Usage

### Using OpenAI Whisper

1. Place your audio files (`.ogg` or `.wav`) in the `audio/` directory
2. Run the OpenAI transcription script:

```bash
python transcription.py
```
The script will:
- Transcribe all audio files in their original language
- Translate the transcriptions to English
- Save the results as JSON files in the `output/` directory

### Using Google Gemini

1. Place your audio file (`.ogg` or `.wav`) in the `audio/` directory
2. Run the Gemini transcription script:

```bash
python transcriptionGemini.py
```
The script will:
- Transcribe the audio file in its original language
- Translate the transcription to English
- Display the results in the console

## File Structure

```
.
├── README.md
├── transcription.py      # OpenAI Whisper implementation
├── transcriptionGemini.py # Google Gemini implementation
├── audio/
│   ├── ChitpavaniMarathi.wav # Example audio file
│   └── Example.ogg          # Example audio file
└── output/
    ├── ChitpavaniMarathi.json # Example output from OpenAI Whisper
    └── Example.json           # Example output from OpenAI Whisper
```

## Notes

- The OpenAI Whisper script can process multiple `.ogg` and `.wav` files in the audio directory and automatically translates the transcriptions to English
- The Gemini script currently processes one file at a time and provides English translation
- Both scripts require valid API keys to function
- Transcriptions and translations are saved as JSON files in the `output/` directory for OpenAI Whisper

## Error Handling

Both scripts include basic error handling for:
- Missing API keys
- File not found