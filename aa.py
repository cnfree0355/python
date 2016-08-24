#!/usr/bin/env python
# -*- coding:utf8 -*-


def  foo(fn1):
    def a():
        print "装饰器传入函数 %s"  %(fn1.__name__)

        fn1()
        print  "装饰器回调函数 %s"  %(fn1.__name__)
    return a

@foo
def tt():
    print "装饰器测试"
tt()


