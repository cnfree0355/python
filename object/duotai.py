#!/usr/bin/env python
# encoding: utf-8

print "多态和封装练习"
class Nature(object):
    def run(self):
        print "Nature is running"

# "子类继承父类"
#参数传递的是父类
class Fruit(Nature):
    def run(self):
        print "Fruit class "

class Flower(Nature):
    def f2(self,name):
        #self.name = name
        print 'Flower name is %s' %(name)

a = Nature()
b = Fruit()
c = Flower()
#继承父类方法,如果子类拥有父类同样的方法会覆盖掉父类方法
a.run()
b.run()
c.run()
#b.f1()
c.f2('rose')
print "获取对象信息"
print isinstance(c,Flower)
print isinstance(c,Nature)
print isinstance(c,Fruit)


