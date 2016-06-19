#!/usr/bin/env python
#-*- coding=utf8 -*-
test = '''这是一个文本文件,为了验证python的读取和写入\
测试,
都是测试,
都是测试,
现在结束'''
#test1 = raw_input(' type the info here')
f = file('test.txt','w')
f.write(test)
f.close()
#没有指定mode,默认为r
f = file ('test.txt')
while True:
  line = f.readline()
  if len(line) == 0:
    break
  print line,
#注意上面多了一个逗号是用来消除自动换行
f.close()

