#!/usr/bin/env python
# -*- coding:utf8 -*-
# def f(a):
#     return a*a
# a = map(f, [1, 2, 3, 4, 5])
# print a
# def add( x , y ):
#     return x + y
#
# print reduce( add, [1, 3, 5, 7, 9] )
# #
# def add(m ,n):
#     return m + n
# for i in range(1 , 100):
#     k = []
#     li = k.append(i)
#     print reduce(add , k)

#
# def fuck(fn):
#     print "fuck %s!" % fn.__name__[::-1].upper()
#
#
# @fuck
# def wfg():
#    pass
# #
#
#
# f = [x * y for x in range(1, 10) for y in range(1, 10)]
# print f
# #
# f1 = [i for i in range(1, 100) if i % 3 == 0]
# print f1
# a = set(range(10))
# print a



# def  foo(fn):
#     def a():
#         print "装饰器传入函数 %s"  %fn.__name__

#         fn()
#         print  "装饰器回调函数 %s"  %fn.__name__
#     return a
#
# @foo
# def  tt():
#     print "进入装饰器，自己体验"
# tt()

#  注意一下两行区别

# def g(a, b, c):
#     return a + b * c
#
#
# print g(1, 5, 10)
#
# ''' 注意下面的默认参数只能放在行尾'''
#
#
# def g(a, b, c=8):
#     return a + b * c
#

# print g(5, 10)
#
# g = lambda a, b, c=8: a + b * c
#
# print g(2, 3)



# f3 = map( lambda x,y: x*y,[x for x in range(1,10)] , [y for y in range(1,10)])
# print f3
#
# for x in range(1, 10):
#     for y in range(1, 10):
#         print  x * y

#
# f3 = map( lambda x: x*x,[x for x in range(1,9)] )
# print f3
# #

#
# def a(x):
#     return x*x

# x = []
# for i in range(1, 10):
#     x.append(i)
#
# print x


