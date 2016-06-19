#!/usr/bin/env python
# encoding: utf-8

class Student(object):

    def __init__(self,name,score):
        self.name = name
        self.score = score

    def  print_score(self):
        print '%s:%s' %(self.name,self.score)

    def get_grade(self):
        if self.score >=90:
            return "优秀"
        elif self.score >= 60:
            return "还不错,继续加油!"
        else:
            return "要努力啊!"

rst = Student('lilei',93)
lisa = Student('lisa',75)

rst.print_score()
print rst.get_grade()
lisa.print_score()
print lisa.get_grade()
