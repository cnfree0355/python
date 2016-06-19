#!/usr/bin/env python
# -*- coding: utf8 -*-
def f(x):
    return x*x
def j(m,n):
    return m + n
def h(x):
    return x % 2 == 0 and x % 3 == 0
k = []
for i in range(10):
    k.append(i)

v = map(f,k)
t = reduce(j,k)
z = filter(h,k)
print v
print 't\'s values is %d' %t
print z

print "reduce function"
def fn(x,y):
    return x*10 +y
print reduce(fn,k)

print "filter 函数"
def is_sushu(num):
    for i in range(2,101):
        if (i != num and num % i ==0) or num == 1:
            return False
        return True

print filter(is_sushu,range(1,101))
