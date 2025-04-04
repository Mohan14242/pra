# download_audio.py
import sys
from pytube import YouTube
import os

def download_audio(video_url):
    yt = YouTube(video_url)
    audio_stream = yt.streams.filter(only_audio=True).first()
    os.makedirs("downloads", exist_ok=True)
    output_file = audio_stream.download(output_path="downloads")
    
    # Convert to mp3 using ffmpeg
    mp3_output = "downloads/downloaded_audio.mp3"
    os.system(f"ffmpeg -i \"{output_file}\" -vn -ab 192k -ar 44100 -y \"{mp3_output}\"")
    
    # Remove original (e.g., .mp4) file
    if output_file != mp3_output:
        os.remove(output_file)

if __name__ == "__main__":
    video_url = sys.argv[1]
    download_audio(video_url)
