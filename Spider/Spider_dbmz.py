#!/usr/bin/env python
# *-* coding:utf-8 *-*


from colors import ColorsPrint
import os
import requests
from bs4 import BeautifulSoup
import time

cl = ColorsPrint()
s = requests.Session()
Header = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/52.0.2743.82 Safari/537.36"
}

# 新建图片保存目录
download_dir = 'E:\Python Project\image_download'


def img_dir(pic_path):
    if os.path.exists(pic_path):
        cl.notify_color('error', '目录已经存在,开始下载')
    else:
        cl.notify_color('info', '正在新建目录')
        os.makedirs(pic_path)


img_dir(download_dir)

pages = int(raw_input('输入你想要下载的页数: '))
end_pages = int(raw_input('输入你想要结束的页数: '))
cl.notify_color('info', '开始下载')

for page in range(pages, end_pages):
    # 获取网页文件类容
    url = 'http://www.dbmeinv.com/dbgroup/show.htm'
    cid = [2, 3, 4, 6, 7]

    pay_load = {
        "cid": 6,
        "pager_offset": page  # page 不能加引号
    }

    html_doc = s.get(url, params=pay_load, headers=Header).content

    # 读取网页内容并且解析标签
    soup = BeautifulSoup(html_doc, "html.parser")
    # 获取图片url,保存成list
    li = []
    for img_url in soup.find_all('img'):
        m = img_url.get('src')
        li.append(m)

    os.chdir(download_dir)
    # 保存图片名称
    photo_name = []
    for pic_url in li:
        photo_name.append(pic_url.split('/')[4])
        r = requests.get(pic_url)
        with open(photo_name[:][-1], 'wb') as f:
            print "正在下载", photo_name[:][-1]
            for chunk in r.iter_content(1024):
                f.write(chunk)

        # 设置休眠时间，避免访问频繁,被封
        time.sleep(2)

cl.notify_color('success', '下载完成')
