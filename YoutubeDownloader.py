# pip install youtube_dl


import youtube_dl
video_url=input("Link Giriniz")

video_bilgisi=youtube_dl.YoutubeDL().extract_info(url=video_url,download=False)

dosya_adi = f"{video_bilgisi['title']}.mp3"

ayarlar={
    'format':'bestaudio/best',
    'keepvideo':False,
    'outtpml':dosya_adi
}
with youtube_dl.YoutubeDL(ayarlar) as ydl:
    ydl.download([video_bilgisi['webpage_url']])

print(f"İndirme tamamlandı...{dosya_adi}")

