#!/usr/bin/env python
# -- coding: utf-8 --#
# @Time : 2020/4/16 15:43 
# @Author : Aries 
# @Site :  
# @File : str_test.py 
# @Software: PyCharm

import re
import datetime

if __name__ == '__main__':
    '''
    一些str操作
    '''
    month = '223'
    print(month.zfill(2))

    data = '3333* ；！? @ # ￥ % …… ^ & 。，_  ~ 宏'

    exp = re.compile('[^\u4e00-\u9fa5]+')
    print(exp.fullmatch(data))

    lst = []
    lst.append(3)
    lst.append(6)
    lst.append(4)
    print(lst)
    lst.remove(6)
    print(lst)
    print(datetime.datetime)
    lset = {}
    lset[32] = '1'
    print(lset[32])
    lset.pop(32)
    print(lset)
    dd = [[0, 1], [3,3], [5,2]]
    mm = [[1,3]]
    dd.sort(key=lambda x:x[1], reverse=True)
    print(dd)


    for n in range(10):
        print(f'this is num {n}')
