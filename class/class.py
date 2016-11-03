#!/usr/bin/env python
#-*- coding: utf-8 -*-
class Employee:
  'common base class for all employees'
  empCount = 0
# Here is __init__ ,otherwise it says typeError: this constructor takes no arguments
 
  def __init__ (self,name,salary):
    self.name = name
    self.salary = salary
    Employee.empCount +=1
  
  def displayCount(self):
     print "所有雇员人数 %d" % Employee.empCount
   
  def displayEmployee(self):
     print "姓名:%s ,薪水:%s" %(self.name,self.salary) 


emp1 = Employee('liu',9000)
emp2 = Employee("guo",20000)

emp1.displayEmployee()
emp2.displayEmployee()
print "所有雇员人数 %d" % Employee.empCount
