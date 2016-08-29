#!/usr/bin/env python
from sys import argv
script,filename = argv
print "now open %r file" % filename
f = open(filename)
print f.read()
f.close()
print '#'*25
print "open other txt file"
prompt = '>'
f2 = open(raw_input(prompt))
print f2.readline()
f2.close()
