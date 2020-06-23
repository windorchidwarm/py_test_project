#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : test_ols.py
# Author: hugh
# Date  : 2020/6/23

from numpy.linalg import inv # 矩阵求逆
from numpy import dot # 矩阵点乘
from numpy import mat # 二维矩阵

if __name__ == '__main__':
    '''
    Y = X a
    X.T X a = X.T Y
    a = (X.T X ) ^ -1 X.T Y
    '''
    X = mat([1, 2, 3]).reshape(3, 1)
    Y = mat([5, 10, 15]).reshape(3, 1)
    x_t = X.T
    x_x = dot(x_t, X)
    x_x_inv = inv(x_x)
    inv_x = dot(x_x_inv, x_t)
    res = dot(inv_x, Y)

    print(X)
    print(Y)
    print(x_t)
    print(x_x)
    print(x_x_inv)
    print(inv_x)
    print(res)