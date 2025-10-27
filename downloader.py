import yt_dlp
import os

def download_video(url, download_dir='downloads'):
    os.makedirs(download_dir, exist_ok=True)

    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': os.path.join(download_dir, '%(title)s.%(ext)s'),
        'merge_output_format': 'mp4',
        # don't print a massive progress bar on some hosts
        'noprogress': True,
        # reduce retries to avoid long hangs
        'retries': 1,
        # quiet but still raise useful exceptions
        'quiet': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
