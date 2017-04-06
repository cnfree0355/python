#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/09/23 15:01
# @Author  : GHL
# @File    : mysql_restore.py


from colors import ColorsPrint
import time
from subprocess import call
import sys


CL = ColorsPrint


def mysql_restore(user, password, config_file='/etc/mysql/my.cnf', host='127.0.0.1', **args):
    CL().notify_color('info', '开始还原数据库')
    CL().notify_color('info', '还原开始 ' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
    print 'user is', user
    print 'password is', password
    print 'config is', config_file
    print 'host is', host
    print 'back_dir is', args.values()[0]
    print 'use memory is', args.values()[1]

    back_dir = args.values()[0]
    memory = args.values()[1]

    CL().notify_color('info', '开始应用事物日志')
    ret_code = call("innobackupex --defaults-file=" + config_file + "\t" + "--apply-log"
                    + "\t" + "--use-memory=" + memory + '\t' + back_dir +
                     ">/dev/null 2&>1", shell=True)
    if ret_code == 0:
        CL().notify_color('success', '事物日志应用成功')
    else:
        CL().notify_color('error', '遇到错误请检查日志,再继续操作!')
        sys.exit(1)

    CL().notify_color('info', '开始拷贝数据和日志')
    # 拷贝数据时候需要data_dir 目录为空
    ret_code_1 = call("innobackupex --defaults-file=" + config_file + "\t" + "--copy-back"
                      + "\t" + "--use-memory=" + memory + '\t' + back_dir +
                      ">/dev/null 2&>1", shell=True)

    if ret_code_1 == 0:
        CL().notify_color('success', '拷贝数据成功')
    else:
        CL().notify_color('error', '遇到错误请检查日志,再继续操作!')
        sys.exit(2)

    CL().notify_color('info', '赋予用户权限')
    call("chown -R" + 'mysql.' + 'mysql' + "\t" + 'data_dir')


if __name__ == '__main__':
    mysql_restore('root', 'db_pass', backdir="/opt/mysql/back", use_memory='2G',
                  data_dir='/opt/mysql_data')
