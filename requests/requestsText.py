# encoding  : utf-8
# Author    : zhoBin
# Datetime  : 2020/5/16 9:28
# File      : requestsText.py
# explain   : 
import requests
from bs4 import BeautifulSoup
import urllib

r = requests.get("http://news.sina.com.cn/photo/rel/csjsy07/399/")
r.encoding = r.apparent_encoding
text = r.text
soup = BeautifulSoup(text, "html.parser")
a = soup.find_all('img', {'class': 'b1'})
for i in a:
    print(i['src'])

