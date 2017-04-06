#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/13 15:52
# @Author  : GHL
# @File    : mysql_outdata.py


import mysql.connector
from colors import ColorsPrint as CLP


CL = CLP()
CL.notify_color('info', 'mysql 运行状态查看')
DMT = "-"
db_pass = raw_input('输入密码，用单引号包含: ')
print DMT * 80
dbinfo = {
    'user': 'root',
    'password': db_pass,
    'database': 'pay',
    'host': '120.24.39.184'
  }

conn = mysql.connector.Connect(**dbinfo)
try:
    conn
except mysql.connector.Error:
    CL.notify_color('error', '数据库连接失败!')

for month in range(1, 12):
    SQL1 = ("select '订单号','订单时间','数量','单位','总价','购买公司' union all"
             " select o.order_number, o.create_time, sum(c.quantity),  c.quantity_unit, "
             " IFNull(o.full_money,sum(c.quantity * c.price)/100), o.buyer_company"
             " from  pay.rw_order o left join pay.jb_huohao hh "
             " on o.order_number=hh.order_number"
             " left join pay.color c ON c.jb_huo_hao_id=hh.id"
             " where o.category = 'jb-all' and c.`category`=2 AND"
             " o.create_time between '2016-%d-01 00:00:00' AND '2016-%d-01 00:00:00' group by o.order_number "
             " into outfile  '/opt/data_out/2016-%d.csv' CHARACTER SET gbk  FIELDS TERMINATED BY ',' "
             " OPTIONALLY ENCLOSED BY '\"' LINES TERMINATED BY '\n' ;"
             % (int(month), int(month + 1), int(month)))  # 格式化结果放最后面，注意SQL 换行后的空格

    cursor = conn.cursor()
    cursor.execute(SQL1)
    cursor.close()

conn.close()
CL.notify_color('success', 'SQL执行成功')