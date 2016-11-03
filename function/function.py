#!/usr/bin/python
def choose(x,y):
  if x >y:
    print 'x is bigger'
  else:
   print 'y is bigger'
x = int(raw_input('type the x here'))

y  = int(raw_input('type the y here'))
choose(x,y)
choose(10,15)


def test(value):
    a = int(raw_input("Type number here:"))
    if a > value:
        print a , "is bigger"
    else:
        print value, 'is bigger'

test(7)

a = '*'
print a*15
#for  the future
def tt(hh):
    pass
def test(user):
  print 'hello , i love %s ' % (user)

test('liu')
