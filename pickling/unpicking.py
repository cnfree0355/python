#!/usr/bin/env python
# encoding: utf-8
import cPickle as pickle
import json
f = open('dump.txt','rb')
d = pickle.load(f)
f.close()
print d

##
print 'use json '
f1 = open('dump.json')
d1 = json.load(f1)
print d1



