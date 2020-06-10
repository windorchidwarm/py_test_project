#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : test_time.py
# Author: hugh
# Date  : 2020/5/27

import timeit


if __name__ == '__main__':
    '''
    测试性能
    '''
    print(timeit.__all__)
    print(timeit._globals)
    print(timeit.timeit('print(i for i in range(199))', number=1000))