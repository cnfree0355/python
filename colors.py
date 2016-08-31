#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/8/31 9:56
# @Author  : GHL
# @File    : colors.py


"""用于print 颜色输出，有绿色、红色、黄色、蓝色输出，通知级别来控制颜色输出，
    success 为绿色输出error为红色输出
    alert为黄色输出 other为蓝色输出，主要用于通知"""


class ColorsPrint:
    def __init__(self):
        self.red_color = '\033[31m'
        self.green_color = '\033[32m'
        self.yellow_color = '\033[33m'
        self.blue_color = '\033[36m'
        self.end_color = '\033[0m'

    def notify_color(self, notify, message):
        if notify == 'success':
            print self.green_color + message + self.end_color
        elif notify == 'error':
            print self.red_color + message + self.end_color
        elif notify == 'alert':
            print self.yellow_color + message + self.end_color
        else:
            print self.blue_color + message + self.end_color

