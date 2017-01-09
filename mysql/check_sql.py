#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/11/16 17:45
# @Author  : GHL
# @File    : check_sql.py


# 从模板中导入某一个类
from colors import ColorsPrint as CLP
import re

CL = CLP()
CL.notify_color('notify', '检查mysql 脚本')


class MysqlCheck(object):
    def __init__(self, filename):
        self.filename = filename

    def check_file(self):
        try:
            with open(self.filename.decode('utf-8')) as f: # 若路径含有中文open需要做编码处理
                contents = f.read()
                update_reg = re.compile(r"^\s*UPDATE[\s\w.,!=()'`\[\]\n+\-\x80-\xff]*;$", re.I | re.M)
                alter_reg = re.compile(r"^\s*ALTER[\w\s'`\-()\n.:=%,+\x80-\xff]*;$", re.I | re.M)
                delete_reg = re.compile(r"^\s*DELETE[\w\s'`.=><!]*;$", re.I | re.M)
                create_table_reg = re.compile(r'^\s*CREATE TABLE[\w\s.=(),\'`\n+/\-\x80-\xff]*', re.I | re.M)
                create_view_reg = re.compile(r"^\s*CREATE VIEW[\w\s.=(),'`\n+/\-\x80-\xff]*", re.I | re.M)
                # utf-8 字符集匹配中文 \x80-\xff unicode 字符集匹配中文为 \u3040-\u309f
                match_create_table = re.findall(create_table_reg, contents)
                match_create_view = re.findall(create_view_reg, contents)
                match_update = re.findall(update_reg, contents)
                match_alter = re.findall(alter_reg, contents)
                match_delete = re.findall(delete_reg, contents)

                if match_create_table:
                    print "一共有 %d 个%s 语句 " % (len(match_create_table), "CREATE TABLE")
                else:
                    CL.notify_color('error', "没有匹配到CREATE TABLE结果")
                if match_create_view:
                    print "一共有 %d 个%s 语句 " % (len(match_create_view), "CREATE VIEW")
                else:
                    CL.notify_color('error', "没有匹配到CREATE VIEW结果")
                if match_delete:
                    print "一共有 %d 个%s 语句 " % (len(match_delete), "DELETE")
                else:
                    CL.notify_color('error', "没有匹配到DELETE结果")
                if match_alter:
                    print "一共有 %d 个%s 语句 " % (len(match_alter), "ALTER")
                else:
                    CL.notify_color('error', "没有匹配到ALTER结果")
                if match_update:
                    print "一共有 %d 个%s 语句 " % (len(match_update), "UPDATE")
                else:
                    CL.notify_color('error', "没有匹配到UPDATE结果")
        except IOError:
            CL.notify_color('error', '文件不存在,请检查!')


if __name__ == '__main__':
    MC = MysqlCheck("redwood.sql")
    MC.check_file()
