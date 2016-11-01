#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/9/26 10:18
# @Author  : GHL
from subprocess import call
import time
import os


try:
    with open('hosts.txt','r') as f:
        host_list = f.readlines()
except IOError:
    print '文件不存在请检查'
else:
    for i in range(0,len(host_list)):
        sp = host_list[i].rsplit('\t\t')
        print '现在连接到',sp[0]
        ip = sp[1].rstrip('\n')
        call('ssh-copy-id -i  ~/.ssh/id_rsa.pub root@' + sp[1].rstrip('\n'),shell=True)
        time.sleep(3)

