#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/8/30 9:50
# @Author  : GHL
# @File    : some.py
#

def math_t():
    for i in range(1, 10):
        print ' '.join(["%d * %d = %-5d" % (j, i, i * j)\
             for j in range(1, i + 1)])


math_t()

print "一种简单的写法\n"

print  '\n'.join(([''.join([ "%d * %d = %-5d" %(y,x,x*y) for y in range(1,x+1)]) for x in range(1,10)]))


