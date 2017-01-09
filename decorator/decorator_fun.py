#!/usr/bin/env python
# coding: utf-8
import time

current_time = time.strftime("%Y-%m-%d  %H:%M:%S")


def now():
    print current_time


now()
print "输出函数名字", now.__name__


def log(func):
    def wrapper(*args, **kw):
        print 'call %s():' % func.__name__
        return func(*args, **kw)
    return wrapper


@log
def now():
    print '2016-05-22'

now()


def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print '%s %s()' % (text, func.__name__)
            return func(*args, **kw)
        return wrapper
    return decorator


@log('The called name is')
def test():
    print "test fun"

test()
