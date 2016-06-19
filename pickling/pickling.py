#!/usr/bin/env python
# encoding: utf-8
# 序列化和反序列化例子
try:
    import cPickle as pickle
except ImportError:
    import pickle
import json
d = dict(name='user1',age=22,score=90)
print pickle.dumps(d)

####
print "use json"
print json.dumps(d)
####
print "pickle 序列化写入文件"
f = open('dump.txt','wb')
pickle.dump(d,f)
## 以json 格式写入文件
f1 = open('dump.json','w')
json.dump(d,f1)
f1.close()
print "##读取序列化后的文件##"
with open('dump.txt') as f:
    print f.read()
    if f:
        f.close()


