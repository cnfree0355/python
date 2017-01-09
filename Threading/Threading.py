#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/12/15 17:56
# @Author  : GHL
# @File    : Threading.py


"""多线程相关"""
import threading
from colors import ColorsPrint
import time

cp = ColorsPrint()


class Mutithreads(threading.Thread):
    def __init__(self, count, name):
        # threading.Thread.__init__(self)  # 调用父类属性
        super(Mutithreads, self).__init__()  # 使用超类
        self.count = count
        self.name = name

    def run(self):
        num = 0
        while num < self.count:
            time_format = time.strftime('%Y%m%d-%H:%M:%S')
            cp.notify_color('notify', "%s start %s" % (time_format, self.name))
            # cp.notify_color('notify', "%s,The current thread_name is  %s" % \
            # (time_format, threading.Thread().getName()))
            time.sleep(2)
            num += 1


Mutithreads(5, 'thread_1').start()
Mutithreads(3, 'thread_2').start()
