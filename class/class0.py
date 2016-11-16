#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/8/11 18:01
# @Author  : GHL
# @File    : class0.py


class User(object):
    """ python 例子"""
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print "%s's age is %d" % (self.name, self.age)


# User 为class, t1为实例，也是object
t1 = User('nana', 25)
t1.info()

# 这些数据和逻辑被“封装”起来了，调用很容易，但却不用知道内部实现的细节。
#  实现封装，以下请仔细体会

print t1.__dict__
print "-" * 20

t2 = User('lin_lin', 24)


def print_some(message):
    print "%s's age is %d" % (message.name, message.age)

print_some(t2)


class Root(object):
    """ 超类的例子,注意新式类才可以使用"""
    def __init__(self):
        print("this is Root")


class B(Root):
    def __init__(self):
        print("enter B")
        # print(self)  # this will print <__main__.D object at 0x...>
        super(B, self).__init__()
        print("leave B")


class C(Root):
    def __init__(self):
        print("enter C")
        super(C, self).__init__()
        print("leave C")


class D(B, C):
    pass


d = D()
print(d.__class__.__mro__)
