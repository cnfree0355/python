#!/usr/bin/env python
# -* coding:utf8 -*
#更简洁的写法
try:
    with open('tet.txt')as f:
        print f.read()
except IOError:
    print "文件不存在,请核对后重新打开"

