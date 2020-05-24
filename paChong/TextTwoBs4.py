# encoding: utf-8
# Datetime  : 2020/5/24 15:41
# User      : zhoBin
# File      : TextTwoBs4.py
# explain   :  bs4的使用


import bs4
import requests
from bs4 import BeautifulSoup


def getHtmlText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "出错了"


def fillUnivList(uvList, html):
    soup = BeautifulSoup(html, "html.parser")
    for tr in soup.find("tbody").children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr("td")
            uvList.append([tds[0].string, tds[1].string, tds[2].string])


def printUnivList(uvList, num):
    tplt = "{0:^10}\t{1:{3}^10}\t{2:^10}"
    print(tplt.format("排名", "学校名称", "总分", chr(12288)))
    for i in range(num):
        u = uvList[i]
        print(tplt.format(u[0], u[1], u[2], chr(12288)))


if __name__ == '__main__':
    uInfo = []
    url = "http://www.zuihaodaxue.com/zuihaodaxuepaiming2020.html"
    html = getHtmlText(url)
    fillUnivList(uInfo, html)
    printUnivList(uInfo, 20)
