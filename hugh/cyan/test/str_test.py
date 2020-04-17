#!/usr/bin/env python
# -- coding: utf-8 --#
# @Time : 2020/4/16 15:43 
# @Author : Aries 
# @Site :  
# @File : str_test.py 
# @Software: PyCharm

import re

if __name__ == '__main__':
    '''
    一些str操作
    '''
    month = '223'
    print(month.zfill(2))

    data = '3333* ；！? @ # ￥ % …… ^ & 。，_  ~ 宏'

    exp = re.compile('[^\u4e00-\u9fa5]+')
    print(exp.fullmatch(data))