import wmain
import time

url = wmain.requests.WUrl(
    "https://v8.longshengtea.com/yyv8/202409/12/Fb6vxdVv1f14/video/index.m3u8"
)
m3u8 = wmain.m3u8.WParser(url)
session = wmain.requests.WSession()
session.ini.set_proxy(7890)
m3u8.session = session
m3u8.parse_m3u8_by_session()
m3u8.try_to_next_level()
downloader = wmain.m3u8.WDownloader(m3u8, "D:/tmp/tmp_0/test_m3u82", "test", 12)
downloader.start()
while downloader.thread.is_running:
    print(f"{downloader.thread.progress * 100:.2f}%")
    time.sleep(1)
print(f"Download finished.")
