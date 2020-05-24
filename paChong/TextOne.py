# 爬虫的练习使用

import requests
import os
from bs4 import BeautifulSoup


def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "产生了异常"


def downLoadImage(url):
    root = "D://pics//"
    path = root + url.split("_")[1] + ".jpg"
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


def getResponse(url):
    r = requests.get(url)
    r.encoding = r.apparent_encoding
    demo = r.text
    return demo


def bs4TextHtml():
    url = "https://www.icourse163.org/"
    soup = BeautifulSoup(getResponse(url), "html.parser")
    # print(soup.prettify())
    print(soup.a.prettify())


if __name__ == '__main__':
    # url = "http://hbimg.b0.upaiyun.com/bc18f16be6a599d2649b645ece7b7300d281853b87f93-TxNHuG_fw658"
    # downLoadImage(url)
    bs4TextHtml()
