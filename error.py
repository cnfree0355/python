#!/usr/bin/env python
# encoding: utf-8

import time
import logging
def foo(s):
    return 100 / int(s)

try:
    s = int(raw_input('在此输入数字:  '))
    r = foo(s)
    print 'result is' ,r
except (ZeroDivisionError,ValueError),e:
# 输出对应的错误
    #print 'error is',e
    print "不能输入0或者其他字符"
#但程序打印完错误信息后会继续执行，并正常退出
except StandardError, e:
    logging.exception(e)
else:
    print "正在计算,请稍后......"
finally:
    print 'exit'


try:
    time.sleep(3)
    # m = raw_input('输入你想输入的: ')
    for i in range(100):
        print i,
except KeyboardInterrupt:
    print "你选择了退出"
else:
    print i,
finally:
    exit(1)




