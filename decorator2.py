#!/usr/bin/env python
# encoding: utf-8

from colors import ColorsPrint

CLP = ColorsPrint()
CLP.notify_color('info', '装饰器演示')


def decorator(F):
    def new_f(a, b):
        print("input", a, b)
        return F(a, b)

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
    def decorator(f):
        def new_f(a, b):
            print(pre + "input", a, b)
            return f(a, b)
        return new_f
    return decorator


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
