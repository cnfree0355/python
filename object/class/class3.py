#!/usr/bin/env python
# encoding: utf-8

import colors


class Student(object):
    pass


s = Student()
s.name = 'liu'
s.age = 23

print s.name
print s.age


class Share:
    name = 'guo'

    def __init__(self, data):
        self.data = data

    def mess(self):
        print self.data


a = Share('23')
b = Share('35')

print Share.name
a.mess()

Share.mess(b)
b.mess()


class NextClass:
    def printer(self, text):
        self.message = text
        print self.message


CL = colors.ColorsPrint()
CL.notify_color('info', '实例调用')
X = NextClass()
CL.notify_color('success', '实例方法调用')
X.printer('instance call')  # 方法调用不需要print
CL.notify_color('alert', '实例属性调用')
print X.message

CL.notify_color('error', '类的调用')
NextClass.printer(X, 'class call')  # 类调用将self变成实例X
print X.message


class superList(list):
    def __sub__(self, b):
        a = self[:]  # 这里，self是supeList的对象。由于superList继承于list，它可以利用和list[:]相同的引用方法来表示整个对象。
        b = b[:]
        while len(b) > 0:
            element_b = b.pop()
            if element_b in a:
                a.remove(element_b)
        return a

# - 其实调用了特殊方法__sub__(特殊方法和运算符等价）
print superList([1, 2, 3, 4]) - superList([3, 4])
m = superList([9, 7, 5])
n = superList([6, 5, 4])
print m - n
