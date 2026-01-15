import yt_dlp
import sys
import os

def download_video(url, output_path='.'):
    """
    Downloads a video from a given URL using yt-dlp.
    """
    first_attempt_opts = {
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',
        'format': 'bestvideo+bestaudio/best',  # Try best quality first (requires ffmpeg)
    }

    fallback_opts = {
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',
        'format': 'best',  # Fallback to best single file (usually 720p, no ffmpeg needed)
    }

    try:
        print(f"Attempting to download best quality (requires ffmpeg)...")
        with yt_dlp.YoutubeDL(first_attempt_opts) as ydl:
            ydl.download([url])
        print("Download completed successfully!")
    except Exception as e:
        error_msg = str(e)
        if "ffmpeg is not installed" in error_msg or "merging of multiple formats" in error_msg:
            print("\nFFmpeg not found. Falling back to best compatible quality (up to 720p)...")
            try:
                with yt_dlp.YoutubeDL(fallback_opts) as ydl:
                    ydl.download([url])
                print("Download completed successfully (fallback quality)!")
            except Exception as e2:
                 print(f"An error occurred during fallback download: {e2}")
        else:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        video_url = sys.argv[1]
        download_video(video_url)
    else:
        video_url = input("Enter YouTube video URL: ")
        if video_url:
            download_video(video_url)
        else:
            print("No URL provided. Exiting.")
