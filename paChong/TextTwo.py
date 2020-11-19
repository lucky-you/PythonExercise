# encoding  : utf-8
# Author    : zhoBin
# Datetime  : 2020/5/16 9:28
# File      : TextTwo.py
# explain   : 爬取图片并保存到本地
import os

import requests
from bs4 import BeautifulSoup


def requestText():
    urlSnas = "http://news.sina.com.cn/photo/rel/csjsy07/399/"
    r = requests.get(urlSnas)
    r.encoding = r.apparent_encoding
    text = r.text
    soup = BeautifulSoup(text, "html.parser")
    a = soup.find_all('img', {'class': 'b1'})
    for i in a:
        url = i['src']
        print(url)
        saveImage(url)


def saveImage(url):
    root = "D://AAA//"
    path = root + url.split("/")[-1]
    try:
        if not os.path.exists(root):
            os.makedirs(root)
        if not os.path.exists(path):
            r = requests.get(url)
            r.raise_for_status()
            with open(path, "wb") as f:
                f.write(r.content)
                f.close()
                print("文件保存成功")
        else:
            print("文件已存在")
    except:
        return "爬取错误了"

if __name__ == '__main__':
    requestText()
