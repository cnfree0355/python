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
# sql = "show GLOBAL status like 'Bytes_received'"
# cursor.execute(sql)
# CL.notify_color('success', 'mysql 接收的流量')
# receive = cursor.fetchall()
# rec = ','.join(receive[0])
# value = int(rec.split(',')[1]) / 1024 / 1024
# print "%s %dM" % (rec.split(',')[0], value)
DB_Drop = [
    "Com_drop_db", "Com_drop_table", "Com_drop_index", "Com_drop_view", "Com_drop_procedure",
    "Com_drop_function", "Com_drop_trigger", "Com_drop_event", "Com_drop_user"
            ]

DB_create = [
    "Com_create_db", "Com_create_table", "Com_create_index", "Com_create_view",
    "Com_create_function", "Com_create_procedure", "Com_create_trigger", "Com_create_user"
]
DB_insert = ["COM_INSERT",	"COM_INSERT_SELECT"]
DB_lock = ["COM_LOCK_TABLES",	"COM_ROLLBACK",	"COM_SELECT"]
DB_update = ["COM_UPDATE",	"COM_UPDATE_MULTI"]

DB_alter = [
    "Com_alter_db", "Com_alter_table", "Com_alter_view",
    "Com_alter_function", "Com_alter_procedure", "Com_alter_trigger"
          ]


def show_status(variables):
    li = []
    for i in range(0, len(variables)):
        cursor.execute("select VARIABLE_NAME,VARIABLE_VALUE from "
                       "information_schema.GLOBAL_STATUS where VARIABLE_NAME=('%s')" % (variables[i]))
        r = cursor.fetchall()
        li.append(r)
    for n in range(0, len(li)):
        print li[n][0][0] + "\t" + li[n][0][1]



CL.notify_color('notify', "create 相关的状态")
show_status(DB_create)
print DMT * 80
CL.notify_color('notify', "drop 相关的状态")
show_status(DB_Drop)
CL.notify_color('notify', "update相关的状态")
show_status(DB_update)
cursor.close()
conn.close()
