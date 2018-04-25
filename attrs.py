#!/usr/local/python3
# -*- coding:utf-8 -*-

class MyObject(object):
    
    def __init__(self):
        self.x = 9

    def power(self):
        return self.x *self.x


obj = MyObject()

print(hasattr(obj, 'x')) #有属性x吗?
print(hasattr(obj, 'y'))

setattr(obj, 'y', 19)  #设置一个属性y
print(hasattr(obj, 'y'))
print(getattr(obj, 'y'))  #获取y属性
print(obj.y)   #获取属性y

print(getattr(obj, 'z', 404))  #获取属性z，如果不存在，返回404


f = getattr(obj,'power')   #获取属性'power'
print(f)
print(f())

