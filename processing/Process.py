#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/8/22 17:35
# @Author  : GHL
# @File    : Process.py

import subprocess
from threading import Timer

kill = lambda  process: process.kil()
cmd = ['ping', 'www.soouya.com']
ping = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

my_timer = Timer(5, kill, [ping])

try:
    my_timer.start()
    stdout, stderr = ping.communicate()
finally:
    my_timer.cancel()

print  (str(stdout))