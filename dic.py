#!/usr/bin/env python
#-*- coding:utf-8 -*-
print "列表输出"
dic = { '湖北':'十堰',
	'广东':'广州',	
	'江苏':'南京',
	'陕西':'西安'	

        }

for province ,city in dic.items():
  print 'this city %s  is in %s' %(city,province)       
