#!/usr/bin/env python
# encoding: utf-8

from colors import ColorsPrint

CLP = ColorsPrint()
CLP.notify_color('info', '装饰器演示')


def decorator(f):
    def new_f(a, b):
        print("input", a, b)
        return f(a, b)

    return new_f


# get square sum
@decorator
def square_sum(a, b):
    return a ** 2 + b ** 2


# get square diff
@decorator
def square_diff(a, b):
    return a ** 2 - b ** 2


print(square_sum(3, 4))
print(square_diff(3, 4))


# a new wrapper layer
def pre_str(pre=''):
    # old decorator
    def dec(f):
        def new_f(a, b):
            print(pre + "input", a, b)
            return f(a, b)
        return new_f
    return dec

# get square sum


@pre_str('^_^')
def square_sum(a, b):
    return a ** 2 + b ** 2


# get square diff
@pre_str('T_T')
def square_diff(a, b):
    return a ** 2 - b ** 2


print(square_sum(3, 4))
print(square_diff(3, 4))


def foo(fn1):
    def a():
        print "装饰器开始传入函数 %s" % fn1.__name__
        fn1()
        print "装饰器回调函数 %s" % fn1.__name__
    return a


@foo
def tt():
    print "装饰器测试"

tt()
