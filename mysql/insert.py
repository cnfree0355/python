#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/12/1 15:58
# @Author  : GHL
# @File    : insert.py

"""如果使用Linux awk 只需要一行即可处理
 awk -v s=\'  '{print "insert into follower_repository
 values((select id from seed where seed.real_name="s$1s")"","s$2s")"";"}' info.txt
"""


def insert_from_text(file_name):
    try:
        with open(file_name) as f:
            contents = f.readlines()  # 结果是一个列表
            count = len(contents)
            sql = "insert into follower_repository values((select id from seed where seed.real_name="
            # 不用with 因为写入文件，所以保持文件打开状态，手动关闭
            f1 = open('result.sql', 'w')
            for i in range(count - 1):
                name, repo = contents[i].rsplit('\t')[0], contents[i].rsplit('\t')[1]  # 注意分隔符是tab
                f1.write(sql + "'" + name + "'" + ")" + "," + "'" + repo + "'" + ")" + ";" + "\n")
            f1.close()
    except IOError:
        print "文件不存在!"


if __name__ == '__main__':
    insert_from_text('info.txt')
