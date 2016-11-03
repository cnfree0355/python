#!/usr/bin/env python
# encoding: utf-8
sum = 0
for i in range(101):
    sum = sum + i
print sum

f = reduce(lambda x, y: x + y, xrange(101))
print f


def clac(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


a = clac([2, 5])
print a


# numbers = range(9)
# f = clac(*numbers)
# print 'f is' ,f



def clac1(*numbers):
    sum = 0
    for  i in numbers:
        sum = sum + i * i
    return sum


b = clac1(2, 5)
c = clac1(2, 3, 4, 5)
print 'b is', b
print 'c is', c

numbers = range(9)
d = clac1(*numbers)
print 'd is ', d


#  函数闭包
def line_conf(a, b):
    def line(x):
        return a * x + b

    return line


line1 = line_conf(1, 1)
line2 = line_conf(4, 5)
print (line1(5), line2(5))
