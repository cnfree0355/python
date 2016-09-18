#!/usr/bin/env python
# encoding: utf-8

from colors import ColorsPrint
import os
import requests
from bs4 import BeautifulSoup

pages = [i for i  in range(1,20)]
url = 'http://www.dbmeinv.com/dbgroup/current.htm?gid=haixiuzu&page_offset=5&pager_offset=50'
s = requests.Session()
Header = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/52.0.2743.82 Safari/537.36"
}
html_doc = s.get(url).content
soup = BeautifulSoup(html_doc, "html.parser")

cl = ColorsPrint()

cl.notify_color('info', '开始下载')

# 获取图片url
li = []
for img_url in soup.find_all('img'):
    m = img_url.get('src')
    li.append(m)


# 新建图片保存目录
def img_dir(pic_path):
    if not pic_path:
        os.mkdir(pic_path)
    else:
        "目录已经存在"


photo_name = []
for pic_url in li:
    photo_name.append(pic_url.split('/')[4])  # 保存图片名称
    r = requests.get(pic_url)
    with open(photo_name[:][-1], 'wb') as f:
        print "正在下载",photo_name[:][-1]
        for chunk in r.iter_content(1024):
            f.write(chunk)
    f.close()

cl.notify_color('success', '下载完成')
if __name__ == '__main__':
    img_dir('img_download')


