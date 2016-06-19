#!/bin/python 
#-*- coding:utf-8 -*-
age=int(raw_input("please type in here" ))
if age<=18:
  print "you are young"
else:
  print "you are adult"
print  "测试中文"

for i in range(1,10):
  print i 
  print "将不包括10"
a = '+'
print a*25
print "list 列表"
tt = ['shiyan','xiangyang','huangshi','jingzhou','huangang','wuhan']
print 'item 0 is ', tt[0]
print 'item 0 to 3 is', tt[0:3]
print 'item -5 to -s is', tt[-5:-3]
print "包含开始位置，但不包含结束位置"


