#!/usr/bin/env python
# encoding: utf-8
import mysql.connector
conn = mysql.connector.connect(user='root',password='',database='test')
cursor=conn.cursor()
cursor.execute('create table user(\
    id int(5) AUTO_INCREMENT primary key comment "用户id",\
    name varchar(20) comment "用户姓名",\
    age tinyint(4) comment "用户年龄")DEFAULT CHARSET=utf8')

cursor.execute("insert into user values(00001,'guo',26)")
cursor.execute("insert into user values(00002,'liu',26)")
print cursor.rowcount
conn.commit()

cursor.close()

