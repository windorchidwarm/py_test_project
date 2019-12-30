#!/usr/bin/env python
# -- coding: utf-8 --#
# @Time : 2019/12/28 10:35 
# @Author : Aries 
# @Site :  
# @File : metris_test.py 
# @Software: PyCharm

import numpy as np


def metris_cheng():
    '''
    矩阵乘法
    :return:
    '''


if __name__ == '__main__':
    print('-----')
    l = [[1,2,3],[2,3,4], [3,4,6], [8,4,3]]
    m = [[2, 4, 0], [5,6,3], [9, 9,2]]
    n_l = np.array(l)
    n_m = np.array(m)
    print(n_l)
    res = np.dot(n_l, n_m)
    print(res)