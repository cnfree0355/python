#!/usr/bin/env python
# encoding: utf-8
class test(object):

    def __init__(self):
        self.number = 0

    def t1(self):
        print "class test!!!"

    def add(self,count):
        self.number += count
        return self.number

a = test() # 实例化
b = test()

a.t1()
print a.add(30)
print a.add(20)
print "实例b"
print b.add(30)

print a.number


