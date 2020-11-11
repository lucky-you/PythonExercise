# 爬取图片并保存到本地

import requests
import os

from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}
url = 'https://www.zhihu.com/question/26620889/answer/905030937'


