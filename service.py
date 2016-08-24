#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/8/12 16:31
# @Author  : GHL
# @File    : service.py

import os
import sys
import commands


class Colors:
    """设置输出的颜色显示"""

    def __init__(self):
        self.red_color = '\033[31m'
        self.green_color = '\033[32m'
        self.yellow_color = '\033[33m'
        self.blue_color = '\033[36m'
        self.End_color = '\033[0m'

    def notify_color(self, notify, services, message):
        # self.notify = notify
        # self.message = message
        # self.services = services
        if notify == 'success':
            print self.green_color + services + message + self.End_color
        elif notify == 'error':
            print self.red_color + services + message + self.End_color
        elif notify == 'alert':
            print self.yellow_color + services + message + self.End_color
        else:
            print self.blue_color + services + message + self.End_color


# 初始化函数实例
color = Colors()

action_list = ["start", "stop", "restart", "reload", "status"]
""" 注意python 脚本即为第一个参数，argv[:]保存的是参数列表，0即为脚本名称"""
if len(sys.argv) < 3:
    print "用法为:", sys.argv[0], "service_name", '|'.join(action_list)
    sys.exit(1)
else:
    file_name, service_name, action_name = sys.argv
    # 传递变量给linux shell
    os.environ['service'] = service_name
    # 调用系统shell
    command_status, output = commands.getstatusoutput('ps -ef|grep "$service"|grep -v grep|grep -v python  >/dev/null')
    ret = command_status


    def check_status(num):
        if num == 0:
            color.notify_color('success', service_name, '服务已经启动')
            sys.exit(0)
        else:
            color.notify_color('error', service_name, '服务没有启动')
            sys.exit(1)


    def service_control(action):
        if action == 'start':
            if ret == 0:
                color.notify_color('success', service_name, '服务已经启动')
            else:
                color.notify_color('notice', service_name, '正在启动')
                os.system('$service')
        elif action == 'stop':
            if ret != 0:
                color.notify_color('notice', service_name, '已经停止')
            else:
                color.notify_color('alert', service_name, '正在停止')
                os.system('$service -s stop')
        elif action == 'reload':
            color.notify_color('alert', service_name, '正在reload')
            os.system('$service -s reload')
        elif action == 'restart':
            color.notify_color('alert', service_name, '正在停止')
            os.system('$service -s stop')
            os.system('sleep 3')
            color.notify_color('notice', service_name, '正在启动')
            os.system('$service')
        elif action == 'status':
            check_status(ret)
        else:
            print "用法为:", sys.argv[0], "service_name", '|'.join(action_list)

if __name__ == '__main__':
    service_control(action_name)
