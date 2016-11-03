#!/usr/bin/env python
# encoding: utf-8
def count():
    fs = []
    for i in range(1,4):
        def f(j=i):
            return j*j
        fs.append(f)
    return fs
f1,f2,f3 = count()
print f1()
print f2()
print f3()

print "lambda 函数"
f1, f2,f3 = [(lambda i = j : i ** 2) for j in range(1, 4)]
print f1()
print f2()
print f3()

