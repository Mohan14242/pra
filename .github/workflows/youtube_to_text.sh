#!/bin/bash

# Define folder and filenames
DOWNLOAD_FOLDER="./downloads"
AUDIO_FILE="$DOWNLOAD_FOLDER/downloaded_audio.mp3"
TEXT_FILE="$DOWNLOAD_FOLDER/downloaded_audio.mp3.txt"

# Ensure the download folder exists
mkdir -p "$DOWNLOAD_FOLDER"

# Check if a URL was provided
if [ -z "$1" ]; then
    echo "Usage: ./youtube_to_text.sh <YouTube-Video-URL>"
    exit 1
fi

# Install dependencies (only for GitHub Actions)
sudo apt update && sudo apt install -y ffmpeg yt-dlp
pip install openai-whisper

# Download YouTube audio
echo "Downloading audio from YouTube..."
yt-dlp -x --audio-format mp3 -o "$AUDIO_FILE" "$1"

# Check if the audio file was created
if [ ! -f "$AUDIO_FILE" ]; then
    echo "Error: Audio file not found!"
    exit 1
fi

# Convert audio to text using Whisper
echo "Transcribing audio to text..."
whisper "$AUDIO_FILE" --language English --output_dir "$DOWNLOAD_FOLDER" --output_format txt

# Check if transcription was created
if [ ! -f "$TEXT_FILE" ]; then
    echo "Error: Transcription failed!"
    exit 1
fi

echo "Transcription saved as $TEXT_FILE"
