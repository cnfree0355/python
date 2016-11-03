#!/usr/bin/env python
# -*- coding:utf8 -*-
# def ff(x, y=1,*z ):
#     return x, y, z
#
# print ff(2,  10, 100, 1000)

# def  n(a, b=1,*z,**m ):
#     return a, b, z, m
#
#
# """多个参数返回一个元祖tupple ,关键字参数返回字典 dic"""""
# print n(2,  10, 3, 11, m=1)

_formats = {
    'ymd' : '{d.year}-{d.month}-{d.day}',
    'mdy' : '{d.month}/{d.day}/{d.year}',
    'dmy' : '{d.day}/{d.month}/{d.year}'
    }

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __format__(self, code):
        if code == '':
            code = 'dmy'
        fmt = _formats[code]
        return fmt.format(d=self)

d = Date(2016, 1, 21)
print format(d)

