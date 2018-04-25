#!/usr/local/bin/python3.6
# -*- coding: utf-8 -*-

class Animal(object):
    def run(self):
        print('Animal is running...')


class Dog(Animal):
    def run(self):
        print('Dog is running...')


class Cat(Animal):
    def run(self):
        print('Cat is running...')


def run_twice(animal):
    animal.run()
    animal.run()

a = Animal()
b = Dog()
C = Cat()

print('a is Animal?', isinstance(a, Animal))
print('b is Dog?', isinstance(b, Dog))
print('c is Cat?', isinstance(c, Cat))


d = Cat()
print('d is Animal?', isinstance(d, Animal))
print('d is Dog?', isinstance(d, Dog))
print('d is Cat?', isinstance(d, Cat))

run_twice(c)
