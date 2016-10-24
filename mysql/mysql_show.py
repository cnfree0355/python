#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/9/12 15:19
# @Author  : GHL
# @File    : mysql_show.py


import mysql.connector
from colors import ColorsPrint as CLP

CL = CLP()
CL.notify_color('info', 'mysql 运行状态查看')
DMT = '-'
print DMT * 80
dbinfo = {
    'user': 'root',
    'password': 's0ouya123!@#',
    'database': 'mysql',
    'host': 'cn1.soouya.cn'

}
conn = mysql.connector.Connect(**dbinfo)
cursor = conn.cursor()
sql = "show GLOBAL status like 'Bytes_received'"
# cursor.execute(sql)
# CL.notify_color('success', 'mysql 接收的流量')
# receive = cursor.fetchall()
# rec = ','.join(receive[0])
# value = int(rec.split(',')[1])/1024 /1024
#
# print  rec.split(',')[0], value,"M"

# li = []
# def format_output(li):
#     print '%s \t %-5s' %(li)
#
#
# cursor.execute("show status like 'Innodb_ibuf%'")
# r = cursor.fetchall()
# for item in r:
#      print "%s \t %-5s" %(item[0], item[1])
#
# cursor.execute("show status like 'Innodb_lsn%'")
# n = cursor.fetchall()
# for lsn in n:
#     print "%s \t %-5s" %(lsn[0], lsn[1])

cursor.close()
conn.close()




