#!/usr/bin ptyhon3
# -*- coding = utf-8 -*-

class Student(object):
    __slots__ = ('name', 'age')   #用tuple定义允许绑定的属性名称 


class GraduateStudent(Student):
    pass


s = Student()       #创建新的实例
s.name = 'Micheal'  #绑定属性name
s.age = 28          #绑定属性age


#error Student不能绑定score 
try:
    s.score = 99
except AttributeError as e:
    print('AttributeError:', e)

g = GraduateStudent()
g.score = 99     #__solts__定义只对当前类起作用，对继承的子类是不起作用的
print('g.score=', g.score)
