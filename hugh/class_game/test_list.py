#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : test_list.py
# Author: hugh
# Date  : 2020/5/7

if __name__ == '__main__':
    print([].__sizeof__()) # size 40
    lst = [1, 2, 4]
    lst.insert(1, 6) # 插入超过限制就是最后一列
    print(lst)
    lst.pop()
    print(lst.__sizeof__()) #
    print(lst)