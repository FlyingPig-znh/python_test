#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'flying pig'

class test_1(object):
    def __init__(self):
        self.x = 11
    def power_1(self):
        return self.x * self.x
obj = test_1()
print(obj.x,obj.power_1())


def set_score(self,score):
    silf.score = score

'''
from types import *

obj.set_score = methodtyte(set_score, s)
print(obj.set_score(99))
'''
#__iter__使用（迭代）
class Fib(object):
    def __init__(self):
        self.a , self.b = 0, 1
    def __iter__(self):
        return self
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 10000:
            raise StopIteration()
        return self.a
for n in Fib():
    print(n)
#__getitem__(获取任意项)
class Fib_1(object):
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a
f =  Fib_1()
print (f[6])
print (f[10])      
