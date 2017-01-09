#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/11/10 16:15
# @Author  : GHL
# @File    : show_content.py


import requests
from bs4 import BeautifulSoup
import colors
import re

clp = colors.ColorsPrint
s = requests.Session()
Header = {
    "user-agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5)'
                  'AppleWebKit/537.36 (KHTML, like Gecko)Chrome/52.0.2743.82 Safari/537.36'
}
refer = {

}

url = "http://16puo.lofter.com/tag/%E5%A5%B3%E7%A5%9E?page=22&t=1477352341645"
url2 = "http://16puo.lofter.com/"
url4 = "http://haiqinmio.lofter.com/"
# url3 = "http://ptlogin2.qq.com/ptqrshow?appid=549000912&e=2&l=M&s=3&d=72&v=4&t=0.5185702057867643&daid=5"
# login_info = {
#     "user": "948339693",
#     "password": ""
# }

html_content = s.get(url, headers=Header).content
soup = BeautifulSoup(html_content, "html.parser")


# for link in  soup.find_all('img'):
#     print  link.get('src').split('?')[0]

li = [] # 保存获取到的hot
# soup.find_all("a", attrs={"class": "hot"}) 也可以替代下面
for link1 in soup.find_all("a", class_="hot"): # 使用class_ 来获取css 样式中的class
     li.append(int(link1.get_text()))  # get_text()函数获取标签内容


def comp(x, y):
    if x > y:
        return -1
    if x < y:
        return 1
    return 0

print  sorted(li,comp)
print sorted(li)[::-1]


