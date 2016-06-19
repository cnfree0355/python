#!/usr/bin/env python
# encoding: utf-8
while  True:
    try:
        x = input('type the number here: ')
        y = input('type the seconde number here: ')
        value = x /y
        print 'x / y is'  ,value

    #except (ZeroDivisionError,TypeError,NameError):
    except Exception,e:
        print "The second number can't be zero or other things that is not the number"
        print "Please try again"
    else:
        break



