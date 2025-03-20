import os
import yt_dlp

def download_tiktok_video(url):
    output_path = "Downloaded_Videos/%(title)s.%(ext)s"
    options = {
        'outtmpl': output_path,
        'format': 'best'
    }

    with yt_dlp.YoutubeDL(options) as ydl:
        ydl.download([url])
        print(f"✅ تم تحميل الفيديو بنجاح!")

if __name__ == "__main__":
    video_url = input("🎥 أدخل رابط TikTok: ")
    download_tiktok_video(video_url)
