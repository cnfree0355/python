#!/usr/bin/env python
# encoding: utf-8
def f(name):
    #return name[0].upper()+name[1:].lower()
    return name.title()
list = ['admin','SHeYup','sfTP']
print map(f,list)



def prod(a):
    def calc(a,b):
        return a*b
    return reduce(calc,a)

l = [x for x in range(1,6)]
print prod(l)


