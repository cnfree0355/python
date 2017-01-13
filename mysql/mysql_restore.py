#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/09/23 15:01
# @Author  : GHL
# @File    : mysql_restore.py


from colors import ColorsPrint
import time
from subprocess import call
import os


CL = ColorsPrint


def mysql_restore(user, password, config_file='/etc/mysql/my.cnf', host='127.0.0.1', **args):
    CL().notify_color('info', '开始还原数据库')
    CL().notify_color('info', '还原开始 ' + time.strftime('%Y%m%d %H:%M:%S', time.localtime()))
    print 'user is', user
    print 'pass is', password
    print 'config is', config_file
    print 'host is', host
    print 'back_dir is', args.values()[0]
    print 'use memory is', args.values()[1]
    #
    # if  os.path.exists(back_dir)
