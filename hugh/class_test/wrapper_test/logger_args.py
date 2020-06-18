#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : logger_args.py
# Author: hugh
# Date  : 2020/6/18

from functools import wraps

class logger(object):

    def __init__(self, num):
        print(num)
        self.num = num

    def __call__(self, func):
        print('this is a')
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('this is d')
            rv = func(*args, **kwargs)
            return rv
        return wrapper

@logger(3)
def hello(a, b):
    print(a, b)

if __name__ == '__main__':
    '''
    '''
    hello(1, 2)
    hello(2, 3)