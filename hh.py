#!/usr/bin/env python
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
print 't\'s values is %s' %t
print z 
