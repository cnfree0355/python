#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/8/24 23:22
# @Author  : GHL
# @File    : Iteration.py


""" 生成器和迭代器测试练习 """
items = [1, 2, 3]
it = iter(items)
print next(it)
print next(it)


def f_range(start, stop, increment):
    x = start
    while x < stop:
        yield x
        x += increment


print list(f_range(0, 50, 5))

for n in f_range(0, 4, 0.5):
    print n

#
# def fab(max_number):
#     n, a, b = 0, 0, 1
#     L = []
#     while n < max_number:
#         L.append(b)
#         a, b =b, a + b
#         n = n + 1
#     return L
#
# for n in fab(5):
#     print n


def fab_yield(max_num):
    """ yield 的作用就是把一个函数变成一个 generator，带有 yield 的函数不再是一个普通函数，
    Python 解释器会将其视为一个 generator，"""
    m, a, b = 0, 0, 1
    while m < max_num:
        # print b
        yield b
        a, b = b, a + b
        m += 1


fab_yield(5)
print "*" * 20
for i in fab_yield(5):
    print i
# 以列表方式输出
print list(fab_yield(5))


def countdown(num):
    print('Starting')
    while num > 0:
        yield num
        num -= 1


li = countdown(5)
for i in li:
    print i
