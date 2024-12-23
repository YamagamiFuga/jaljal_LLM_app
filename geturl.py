import yt_dlp # type: ignore

playlist_url = "https://youtube.com/playlist?list=PLGIk_2Rdu8YGV-xAyb37H3NVMMSfbLGse&si=X5-V0eKuoNP2wrHh"

#再生リスト情報を取得
ydl_opts = {
    'extract_flat': True,  # 再生リスト内の動画の情報を取得
    'skip_download': True  # 動画をダウンロードせずに情報のみ取得
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    playlist_info = ydl.extract_info(playlist_url, download=False)

# 動画タイトルとURLを保存
video_data = [(entry['title'], entry['url']) for entry in playlist_info['entries']]
with open("video_urls.txt", "w", encoding="utf-8") as file:
    for title, url in video_data:
        file.write(f"タイトル: {title}\nURL: {url}\n\n")
        
