#!/usr/bin/env python
# encoding: utf-8
import mysql.connector
conn = mysql.connector.connect(user='root',password='',database='test',use_unicode='false')
#conn = mysql.connector.connect(user='root',password='',database='test')
cursor = conn.cursor()
cursor.execute('select * from user where id=%s',(00001,))
values = cursor.fetchall()
print (values)
cursor.close()
conn.close
