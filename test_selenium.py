from wmain.selenium import WEdgeDownloader
from wmain.requests import WSession
import time
session = WSession()
session.ini.set_proxy(7890)
downloader = WEdgeDownloader(session=session)
driver = downloader.get_driver()
driver.start()
driver.get('https://v8.chaoxing.com/')
driver.send_keys_by_xpath('//*[@id="uunnmm"]', "13214310112")
driver.send_keys_by_xpath('//*[@id="pwd"]', "13214310112asdw")
driver.click_by_xpath('//*[@class="btn"]')
while 1:
    time.sleep(5)