# 爬取图片并保存到本地

import requests
import os

from bs4 import BeautifulSoup

header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36',
    'Referer': 'http://www.xiachufang.com/'
}


def requestText():
    urlSnas = "http://www.xiachufang.com/"
    r = requests.get(urlSnas, header=header)
    r.encoding = r.apparent_encoding
    text = r.text
    soup = BeautifulSoup(text, "html.parser")
    # a = soup.find_all('img', {'class': 'cover'})
    print(soup)
    # for i in a:
    #     url = i['src']
    #     print(url)
    #     # saveImage(url)
