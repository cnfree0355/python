#!/usr/bin/env python
#-*- coding: utf-8 -*-
from  sys import argv
#scriptname,fir,sec,thi,fou = argv
script,user = argv
#此处输出需要逗号，区分字符串和变量
#print "脚本名称是:" ,scriptname
#print "第一个参数是:", fir
#print "第二个参数是:",sec
#print "第三个参数是:",thi
#print "当前系统是" , fou
prompt = '>'

print 'hello  %s welcome to here'  %(user)
print 'type your age'
age = raw_input(prompt)
print  'you age is' ,age
