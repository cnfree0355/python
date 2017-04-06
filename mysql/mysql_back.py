#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/9/23 10:18
# @Author  : GHL
# @File    : mysql_back.py


from colors import ColorsPrint as CL
from subprocess import call
import time
import datetime
import os



def days_ago(days_num):
    """ 获取几天前的日期"""
    today = datetime.datetime.now()
    interval_days = datetime.timedelta(days=days_num)
    few_days_ago = (today + interval_days).strftime('%Y-%m-%d %H:%M:%S')
    return few_days_ago

# 输入密码,需要添加单引号,否则会提示找不到命令
CL().notify_color('alert', '输入密码，用单引号包含!!!')
time.sleep(3)
db_pass = raw_input('在此输入密码: ')
compress_time = time.strftime('%Y%m%d', time.localtime())


def mysql_back(user, password, config_file='/etc/mysql/my.cnf', host='127.0.0.1', **args):
    print 'user is', user
    print 'pass is', password
    print 'config is', config_file
    print 'host is', host
    print 'use memory is', args.values()[1] # arg.values()有顺序
    print 'back_dir is', args.values()[0]
    back_dir = args.values()[0]
    memory = args.values()[1]

    if not os.path.exists(back_dir):
        os.mkdir(back_dir)
    else:
        CL().notify_color('info', '备份开始 ' + time.strftime('%Y%m%d %H:%M:%S', time.localtime()))
        ret_code = call("innobackupex --defaults-file=" + config_file + "\t" + "--user=" + user + "\t"
                        + "--password=" + password + "\t" + "--use-memory="
                        + memory + '\t' + back_dir + " " + ">/dev/null 2&>1", shell=True)
        if ret_code == 0:
            CL().notify_color('success', '备份结束 ' + time.strftime('%Y%m%d %H:%M:%S', time.localtime()))
            os.chdir(back_dir)
            call("find ./ -mtime +7 -type d |xargs rm -f", shell=True)
        else:
            CL().notify_color('error', '备份失败请检查!')


if __name__ == '__main__':
    mysql_back('root', db_pass,  back_dir='/opt/mysql-back', value='2G')
