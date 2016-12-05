#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/11/10 16:15
# @Author  : GHL
# @File    : show_content.py


import requests
from bs4 import BeautifulSoup
import colors
import time

clp = colors.ColorsPrint
s = requests.Session()
Header = {
    "user-agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5)'
                  'AppleWebKit/537.36 (KHTML, like Gecko)Chrome/52.0.2743.82 Safari/537.36'
}
url = "http://i.qq.com"
url2 = "http://users.qzone.qq.com/fcg-bin/cgi_get_portrait.fcg?uins=948339693"
login_info = {
    "user": "948339693",
    "password": ""
}
pay_load = {

}
html_content = s.get(url, headers=Header).content
soup = BeautifulSoup(html_content, "html.parser")
# print soup.prettify()
# print soup.title
# for link in  soup.find_all('a'):
#     print link.get('href')
