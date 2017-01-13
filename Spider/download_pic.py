#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/12/30 17:00
# @Author  : GHL
# @File    : download_pic.py


import time
import os
from colors import ColorsPrint as cp
import requests

url = "http://upload.soouya.com"
s = requests.Session()
url_list = []
error_num_list = []
local_dir = "E:\\Python Project\\python\\Spider\\"
Header = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) \
    AppleWebKit/537.36 (KHTML, like Gecko)Chrome/52.0.2743.82 Safari/537.36"
}
# 数据库密码

class Download_Pic(object):
    def __init__(self, filename, download_path):
        self.filename = filename
        self.download_path = download_path

    def img_dir(self):
        for f_path in self.download_path:
            if not os.path.exists(f_path):
                cp().notify_color('info', '正在新建目录')
                os.makedirs(f_path)
            else:
                cp().notify_color('error', '%s目录已经存在,开始下载' % f_path)

    def open_file(self):
        try:
            with open(self.filename.decode('utf-8'), 'rb') as f:
                for index, line in enumerate(f):
                    file_path = line.split('||')[5]
                    image_url = url + file_path
                    url_list.append(image_url.strip('\n'))
        except IOError:
            cp().notify_color('error', "文件不存在,请检查文件以及路径是否正确")

    def download_file(self):
        for index, download_url in enumerate(url_list[:]):
            # start_num =
            pic_dir = download_url.split('/')[4]
            img_file = download_url.split('/')[5]
            # print  pic_dir, '------',time.strftime('%Y%m%d-%H:%M:%S',time.localtime()),img_file
            # time.sleep(3)
            # print error_num_list
            if pic_dir == "fitting":
                os.chdir(local_dir + self.download_path[0])  # 加上local_dir 以免切换找不到目录
            elif pic_dir == "tmp":
                os.chdir(local_dir + self.download_path[1])
            else:
                raise IOError("不存在图片路径")

            cp().notify_color('info', '%s 正在下载第 %d 张图片,图片为 %s' %
                              (time.strftime('%Y%m%d-%H:%M:%S',
                               time.localtime()), int(index + 1), img_file))

            r = s.get(download_url, headers=Header)
            try:
                r
            except KeyboardInterrupt:
                cp().notify_color('alert', '已手动停止下载!')
            except requests.exceptions.ConnectionError:
                cp().notify_color('error', "%s由于网络连接中断,下载停留在第 %d 张图片,"
                                  "图片名称为 %s,请检查重试" % (time.strftime
                                   ('%Y%m%d-%H:%M:%S', time.localtime()), int(index + 1), img_file)
                                  )
                error_num_list.append({int(index + 1): img_file})

            with open(img_file, 'wb') as pics:
                for chunk in r.iter_content(1024):
                    pics.write(chunk)
            time.sleep(0.5)


if __name__ == "__main__":
    N = Download_Pic("shiyi_data.txt", ['fitting', 'tmp'])
    N.img_dir()
    N.open_file()
    N.download_file()
