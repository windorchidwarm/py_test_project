#!/usr/bin/env python
# -- coding: utf-8 --#

import numpy as np
import matplotlib.mlab as mlab

if __name__ == '__main__':
    # x, y = np.ogrid[-2:2:20j, -2:2:20j]
    # z = x * np.exp(- x**2 - y**2)
    dd = np.add.reduce([[1, 2, 3], [4, 5, 6]], axis=1)
    print(dd)
    mm = np.add.accumulate([1,2,3])
    print(mm)

    a = np.array([1, 10, 100, 1000])
    result = np.add.reduceat(a, indices=[1,0,2,0,3,0])
    print(result)
    b = np.array([2,3,4])
    print(b)
    print(a)
    print(np.multiply.outer(a, b))

    matrixTest = np.matrix([[1,2,3],[4,5,6],[7,8,9]])
    print(matrixTest)
    print(matrixTest*matrixTest)
    print(matrixTest*matrixTest**-1)
    print(matrixTest**-1)

    print("###################################")
    a = np.arange(12).reshape(2, 3, 2)
    print(a)
    b = np.arange(12, 24).reshape(2, 3, 2)
    print(b)
    c = np.inner(a, b)
    print(c)
    print(c.shape)
    d = np.outer(a, b)
    print(d)
    print(d.shape)