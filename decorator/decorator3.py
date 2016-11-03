#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/11/1 11:43
# @Author  : GHL
# @File    : decorator3.py

import time


def show_decorator(function):
    def wrapper(*args, **kwargs):
        print 'now is', time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        return function(*args, **kwargs)
    return wrapper


@show_decorator
def print_info(words):
    return words


print print_info('why are you always angry,liu tong xue?')

print "新的装饰器演示"


def logged(func):
    def with_logging(*args, **kwargs):
        print func.__name__ + " was called"
        return func(*args, **kwargs)
    return with_logging


@logged
def logs(name):
    print 'username is', name


logs('guo')
