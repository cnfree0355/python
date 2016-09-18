#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/9/1 18:02
# @Author  : GHL
# @File    : logs.py

"""用于程序输出日志"""
import logging as log
# %(asctime)s 设置日期时间
# %(levelname)s 设置日期级别
# filename='message.log' 可以把日志写入文件
# %(processName)s 设置进程名
log.basicConfig(format='[%(asctime)s]  [%(levelname)s]  %(message)s',level=log.INFO,datefmt='%Y%m%d %H:%M:%S')
log.info('日志消息输出测试，级别为info')
log.warning('日志消息输出测试，级别为warning')







