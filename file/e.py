#!/usr/bin/env python
sum = 0
for i in range(101):
  sum = sum + i
print sum

f = reduce(lambda x,y:x +y ,xrange(101))
print f

def clac(numbers):
  sum = 0
  for n in numbers:
     sum = sum + n*n
  return sum

a = clac([2,5]) 
print a
#numbers = range(9)
#f = clac(*numbers)
#print 'f is' ,f




def clac1(*numbers):
  sum = 0
  for n in numbers:
     sum = sum + n*n
  return sum

b = clac1(2,5)
c = clac1(2,3,4,5)
print  b,c

numbers = range(9)
d = clac1(*numbers)
print 'd is ', d


