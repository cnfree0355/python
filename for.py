#!/usr/bin/env python
a = [x*x for x in range(10)]
print a
b = [x*x for x in range(10) if x %3 == 0]
print b
c = [(x,y) for x  in range(1,5) for y  in range(5)]
print c
