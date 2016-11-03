#!/usr/bin/env python
# encoding: utf-8
#下面使用
from types import MethodType
class Employ_info(object):
    pass
#给实例绑定一个属性
s = Employ_info()
print type(s)
s.name = 'guo'
s.age = 25
s.salary = 15000

print s.name
print s.age
print s.salary

#给实例绑定一个方法

def set_age(self,age):
    self.age=age

s.set_age = MethodType(set_age,s,Employ_info)
s.set_age(23)
print 's.age is', s.age

#给一个实例绑定方法,对另一个实例是不起作用的
s2 = Employ_info()
#s2.set_age(22)

#给所有实例都绑定方法,可以给class绑定方法

def set_salary(self,salary):
    self.salary = salary

Employ_info.set_salary = MethodType(set_salary,None,Employ_info)

s.set_salary(18000)
print s.salary
s2.set_salary(20000)
print s2.salary

#限定class 属性
#__slots__ 仅对当前类生效,对继承的子类是不起作用的
class Test(object):
     __slots__ = ('name','salary')

s3 = Test()
s3.name = 'liuliu'
s3.salary = 8000
#会出现error
#s3.age = 25

print s3.name
print s3.salary
#会出现error
#print s3.age
