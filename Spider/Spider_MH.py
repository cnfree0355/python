#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/10/10 16:49
# @Author  : GHL
# @File    : Spider_MH.py


from colors import ColorsPrint as CP
import requests
from bs4 import BeautifulSoup


url='http://tw.ikanman.com/comic/881/7557.html'
CL = CP()
s = requests.Session()
Header = {
    "user-agent": "AppleWebKit/537.36 (KHTML, like Gecko)Chrome/52.0.2743.82 Safari/537.36"
}
pay_load = {
        "p": 7,
        # "pager_offset": page  # page 不能加引号
    }

html_doc = s.get(url, params=pay_load, headers=Header).content


#读取网页内容并且解析标签
soup = BeautifulSoup(html_doc, "html.parser")
# # 获取图片url,保存成list
# li = []
# for img_url in soup.find_all('img'):
#     m = img_url.get('src')
#     li.append(m)
#
# print li
CL.notify_color('notify', '下载漫画')