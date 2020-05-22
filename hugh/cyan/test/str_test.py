#!/usr/bin/env python
# -- coding: utf-8 --#
# @Time : 2020/4/16 15:43 
# @Author : Aries 
# @Site :  
# @File : str_test.py 
# @Software: PyCharm

import re
import datetime, time

from typing import List

if __name__ == '__main__':
    '''
    一些str操作
    '''
    month = '223'
    print(month.zfill(2))

    data = '3333* ；！? @ # ￥ % …… ^ & 。，_  ~ 宏'

    exp = re.compile('[^\u4e00-\u9fa5]+')
    print(exp.fullmatch(data))
    now_time = datetime.datetime.now()
    print(now_time.strftime('%Y%m%d'))

    data_str = '20200418'
    data = time.strptime(data_str, '%Y%m%d')
    print(data)
    print(time.mktime(data))
    date = datetime.datetime.fromtimestamp(time.mktime(data))
    print(date.date())
    # print(datetime.datetime())
    print(time.strftime('%Y-%m-%d %H:%M:%S', data))
    delta = datetime.timedelta(days=7)
    data = datetime.date(data.tm_year, data.tm_mon, data.tm_mday)
    data = data - delta
    print(data)
    print(data.strftime('%Y-%m-%d %H:%M:%S'))

    print('------------------')
    data = ['']
    print(len(data))
    print(data[0])
    i = None
    print(i != '')
    lst = [1, 2]
    print(lst.reverse())


    data = {'dd':'dd', 'xx':'xx'}
    print(data)
    data.pop('dd')
    print(data)



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
