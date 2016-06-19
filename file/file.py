#!/usr/bin/env python
# -* coding:utf8 -*
import os 
from sys import argv
scripts,filename  = argv
print "now open the file"
try:
  f = open(filename)
  print f.read()
finally:
  if f:
    f.close()

