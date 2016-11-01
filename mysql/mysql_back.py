#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/9/23 10:18
# @Author  : GHL
# @File    : mysql_back.py


from colors import ColorsPrint as CL
from  subprocess import call
import time
import sys


# host为默认参数，需要放在关键字参数前

def mysql_back(user, password, config_file='/etc/mysql/my.cnf',host ='127.0.0.1',**args):
    CL().notify_color('info', '开始备份数据库')
    CL().notify_color('info', '备份开始 ' + time.strftime('%Y%m%d %H:%M:%S', time.localtime()))
    print 'user is', user
    print 'pass is', password
    print 'config is', config_file
    print 'host is', host
    print 'back_dir is', args.values()[0]
    print 'use memory is', args.values()[1]

    ret_code = call("innobackupex --defaults-file="+config_file+"\t"+"--user="+user+"\t"+"--password="+password+'\t'+args.values()[0], shell=True )
    if ret_code == 0:
        CL().notify_color('success', '备份结束 ' + time.strftime('%Y%m%d %H:%M:%S', time.localtime()))
    else:
        CL().notify_color('error', '备份失败请检查!')


if __name__ == '__main__':
     mysql_back('root','s0ouya123!@#',back_dir='/opt/mysql-back',value='4G')



