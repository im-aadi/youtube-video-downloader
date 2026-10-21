# YouTube Video Downloader

A simple command-line tool for downloading YouTube videos or audio with [yt-dlp](https://github.com/yt-dlp/yt-dlp).

## Features

- Download a video at the best available quality
- Extract audio as MP3
- Choose an output folder
- Show available video formats
- Keep downloaded files organized with the video title

## Requirements

- Python 3.9 or later
- [FFmpeg](https://ffmpeg.org/) on your system `PATH` (needed for audio extraction and merging separate video/audio streams)

## Setup

1. Clone or download this project.
2. Create and activate a virtual environment (recommended).
3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

   If this project does not include a `requirements.txt` yet, install yt-dlp directly:

   ```bash
   pip install yt-dlp
   ```

## Usage

The examples below use the `yt-dlp` command directly. If this project includes its own Python script, replace `yt-dlp` with that script's command as appropriate.

Download a video:

```bash
yt-dlp "https://www.youtube.com/watch?v=VIDEO_ID"
```

Download the best available MP4 video and audio combination:

```bash
yt-dlp -f "bv*[ext=mp4]+ba[ext=m4a]/b[ext=mp4]" "https://www.youtube.com/watch?v=VIDEO_ID"
```

Extract audio as MP3:

```bash
yt-dlp -x --audio-format mp3 "https://www.youtube.com/watch?v=VIDEO_ID"
```

Save downloads in a chosen folder and name them after the video:

```bash
yt-dlp -o "downloads/%(title)s.%(ext)s" "https://www.youtube.com/watch?v=VIDEO_ID"
```

List available formats:

```bash
yt-dlp -F "https://www.youtube.com/watch?v=VIDEO_ID"
```

## Updating yt-dlp

YouTube may change its systems over time. Keep yt-dlp up to date:

```bash
python -m pip install --upgrade yt-dlp
```

## Troubleshooting

- **`ffmpeg` not found:** Install FFmpeg and make sure its `bin` directory is on your `PATH`.
- **Download errors:** Update yt-dlp and try again. Some videos may be private, age-restricted, region-restricted, or otherwise unavailable to your account.
- **No audio conversion:** Check that FFmpeg is installed and available from the command line.

## Responsible use

Only download videos when you have the rights and permission to do so. Follow YouTube's Terms of Service and respect copyright, privacy, and access restrictions. This project does not bypass DRM or access controls.

## License

Add the license that applies to this project. If you have not chosen one, remove this section or select a license before distributing the code.
