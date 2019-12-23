#!/usr/bin/env python
# -- coding: utf-8 --#

import numpy as np

def func99(i, j):
    return (i + 1) * (j + 1)

if __name__ == '__main__':
    '''
    测试
    '''
    np1 = np.linspace(0, 1, 12)
    print(np1)
    np2 = np.logspace(0, 2, 20)
    print(np2)
    str = "ldsjflkdsfewori23-42-0sljrwle；dds;fsksldaiewjflands;fjeislfs;ajifslajlkeo324329-23#@$@#$@#"
    np3 = np.fromstring(str, dtype=np.int16)
    print(np3)
    np4 = np.fromfunction(func99, (9,9))
    print(np4)
    np4 = np.array(np4)
    print(np.array(np4).shape)
    print(np4[1:3, 2:4])
    print(np4 > 55)

    personType = np.dtype({
        'names':['name','age','mny','sex'],
        'formats':['S32','i','f','b']
    }, align=True)
    np5 = np.array([('zhangsan', 23, 73.5, True), ('lisi', 32, 23.6, True), ('wangss', 18, 34.5, False)],dtype=personType)
    print(np5)
    print(np5.dtype)
    print(np5[0]['name'])

