#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : sixianyu.py
# Author: hugh
# Date  : 2020/10/30


class People(object):
    __name = 'dd'
    _age = 10
    _sex = 'xx'

    def __init__(self, name, age, sex):
        self.__name = name
        self._age = age
        self._sex = sex


if __name__ == '__main__':
    """
    """
    p = People('zly', 99, 'female')
    print(p._People__name)
