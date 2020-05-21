#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : test_fun.py
# Author: chen
# Date  : 2020-04-27

def adder(x):
    def wrapper(y):
        return x + y
    return wrapper
adder5 = adder(5)
print(adder5(adder5(6)))

def f(): pass
print(type(f()))

s = "I love Python"
ls = s.split()
ls.reverse()
print(ls)

mytuple=3,4,5
print(mytuple)
x,y,z=mytuple
print(x+y+z)

print((10) // (-3))
print(2 ** 2.4)