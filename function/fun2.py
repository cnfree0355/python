#!/usr/bin/env python
# encoding: utf-8
print "more arguments"
def student_info(name,gender,age,city='shiyan'):
    print 'name:', name
    print 'gender:', gender
    print 'age:',age
    print 'city:',city

student_info('xiaoming','femal',6)
student_info('ll','male',age=7)

print "key word arguments"
def info(name,password,**kw):
    print 'name is: ' ,name
    print 'password is: ',password
    print 'host is : ',kw

info('liu',123456,host='database')


