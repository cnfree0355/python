#!/bin/python
users = ['root','test','develop']
passwds = [123456,'abc','dev123']
a=zip(users,passwds)
print a
for user,passd in zip(users,passwds):
  print user ,'passwd is',passd
