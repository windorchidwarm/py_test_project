#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : logger.py
# Author: hugh
# Date  : 2020/6/18

from functools import update_wrapper

class logger(object):

    def __init__(self, func):
        print('this si do')
        self.func = func
        update_wrapper(self, func)

    def __call__(self, *args, **kwargs):
        print('this is active')
        return self.func(*args, **kwargs)

@logger
def hello_3(a, b, c):
    print(1 + 2 + 4, a, b, c)

if __name__ == '__main__':
    hello_3(1, 2, 3)
    hello_3(1, 2, 3)
    hello_3(1, 2, 3)