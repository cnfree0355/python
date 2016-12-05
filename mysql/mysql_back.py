#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/9/23 10:18
# @Author  : GHL
# @File    : mysql_back.py


from colors import ColorsPrint as CL
from subprocess import call
import time
import datetime


def days_ago(days_num):
    """ 获取几天前的日期"""
    today = datetime.datetime.now()
    interval_days = datetime.timedelta(days=days_num)
    few_days_ago = (today + interval_days).strftime('%Y-%m-%d %H:%M:%S')
    return few_days_ago


def mysql_back(user, password, config_file='/etc/mysql/my.cnf', host='127.0.0.1', **args):
    CL().notify_color('info', '开始备份数据库')
    CL().notify_color('info', '备份开始 ' + time.strftime('%Y%m%d %H:%M:%S', time.localtime()))
    print 'user is', user
    print 'pass is', password
    print 'config is', config_file
    print 'host is', host
    print 'back_dir is', args.values()[0]
    print 'use memory is', args.values()[1]

    # 此处没有使用use_memory 可以自行添加
    ret_code = call("innobackupex --defaults-file=" + config_file + "\t" + "--user=" + user + "\t"
                    + "--password=" + password + '\t' + args.values()[0], shell=True)
    if ret_code == 0:
        CL().notify_color('success', '备份结束 ' + time.strftime('%Y%m%d %H:%M:%S', time.localtime()))
        call("find ./mysql-back -mtime +7 -type d |xargs rm -f", shell=True)
    else:
        CL().notify_color('error', '备份失败请检查!')


if __name__ == '__main__':
    mysql_back('root', 'Da87X!lD#B0@m', back_dir='/opt/mysql-back', value='2G')
