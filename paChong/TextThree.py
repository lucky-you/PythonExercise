# 爬取图片并保存到本地

import re
import requests

webUrl = "http://www.nipic.com/photo/jingguan/ziran/index.html"


def getHtml():
    data = requests.get(webUrl).text
    regex = r'data-src="(.*?.jpg)"'
    pa = re.compile(regex)
    ma = re.findall(pa, data)
    i = 1
    for image in ma:
        i += 1
        image = requests.get(image).content
        print(str(i) + ".jpg 正在保存")
        with open('../imgs' + str(i) + ".jpg", "wb") as  f:
            f.write(image)

    print("保存完毕")

if __name__ == '__main__':
    getHtml()
