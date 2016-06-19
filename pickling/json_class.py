#!/usr/bin/env python
# encoding: utf-8
import json
class Student(object):
    def __init__(self,name,age,score):
        self.name = name
        self.age = age
        self.score = score

s = Student('tom',20,89)
print s.name

def student2dic(std):
    return {
        'name':std.name,
        'age':std.age,
        'score':std.score
            }

print (json.dumps(s,default=student2dic))
##
print(json.dumps(s, default=lambda obj: obj.__dict__))
print s.__dict__

def dict2student(d):
    return Student(d['name'],d['age'],d['score'])

f = '{"age":20,"score":88,"name":"Bob"}'
print (json.loads(f,object_hook=dict2student))
