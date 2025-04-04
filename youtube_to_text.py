import os
import sys
import subprocess
import whisper

# Define folder and filenames
DOWNLOAD_FOLDER = "downloads"
AUDIO_FILE = os.path.join(DOWNLOAD_FOLDER, "downloaded_audio.mp3")
TEXT_FILE = os.path.join(DOWNLOAD_FOLDER, "downloaded_audio.mp3.txt")

# Ensure the download folder exists
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

# Check if a URL was provided
if len(sys.argv) < 2:
    print("Usage: python youtube_to_text.py <YouTube-Video-URL>")
    sys.exit(1)

video_url = sys.argv[1]

# Download YouTube audio
print("Downloading audio from YouTube...")
yt_dlp_cmd = [
    "yt-dlp",
    "-x",
    "--audio-format", "mp3",
    "-o", AUDIO_FILE,
    video_url
]
subprocess.run(yt_dlp_cmd, check=True)

# Check if the audio file was created
if not os.path.exists(AUDIO_FILE):
    print("Error: Audio file not found!")
    sys.exit(1)

# Load Whisper model and transcribe
print("Transcribing audio to text...")
model = whisper.load_model("base")  # Change to "small", "medium", or "large" if needed
result = model.transcribe(AUDIO_FILE)

# Save transcription
with open(TEXT_FILE, "w", encoding="utf-8") as f:
    f.write(result["text"])

print(f"Transcription saved as {TEXT_FILE}")
