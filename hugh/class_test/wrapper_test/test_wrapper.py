#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : test_wrapper.py
# Author: hugh
# Date  : 2020/6/18

from functools import wraps


def test_wrapper(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        print('this is declar')
        rv = func(*args, **kwargs)
        print('this is end')
        return rv
    return wrapper

def test_wrapper_size(times = 3):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('calll')
            rv = []
            for i in range(times):
                print('this is scyd')
                rv.append(func(*args, **kwargs))
            print('this is end')
            return rv
        return wrapper
    return decorator


@test_wrapper
def hello_3(a, b, c):
    print(1 + 2 + 4, a, b, c)

@test_wrapper_size(5)
def hello_4(a, b, c):
    print(a + b + c)

if __name__ == '__main__':
    '''
    '''
    hello_3(1, 2, 3)
    hello_4(1, 3, 4)