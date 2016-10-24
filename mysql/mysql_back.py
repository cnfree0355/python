#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/9/23 10:18
# @Author  : GHL
# @File    : mysql_back.py


from colors import ColorsPrint as CL
from  subprocess import call
import time
import os


#host为默认参数，需要放在关键字参数前

def mysql_back( user, password, db_name,config_file='/etc/mysql/my.cnf',host ='127.0.0.1',**args):
    CL().notify_color('info', '开始备份数据库'+ db_name)
    CL().notify_color('info','备份开始 ' + time.strftime('%Y%m%d %H:%m:%S', time.localtime()))
    print 'user is',user
    print 'pass is',password
    print 'db is',db_name
    print 'config is', config_file
    print 'host is',host
    print 'back_dir is', args.values()[0]
    print 'use memory is', args.values()[1]
    time.sleep(5)
    CL().notify_color('success', '备份结束 ' + time.strftime('%Y%m%d %H:%m:%S', time.localtime()))
if __name__ == '__main__':
    mysql_back('root','123456','oms',backdir='/opt/mysql-back',value='4G')



