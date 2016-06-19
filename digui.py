#!/usr/bin/env python
# encoding: utf-8
def fact(n):
    if n == 1:
        return 1
    return n* fact(n-1)

print "递归函数"

print fact(1)
print fact(10)

print "尾递归函数"
def fact(n):
    return fact_iter(n ,1)

def fact_iter(n,total):
    if n == 1:
        return total
    return fact_iter(n-1, n*total)

print "5 的递归是:" , fact_iter(5 ,1)
