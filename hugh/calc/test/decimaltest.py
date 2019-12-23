#!/usr/bin/env python
# -- coding: utf-8 --#
# @Time : 2019/9/19 10:16 
# @Author : Aries 
# @Site :  
# @File : decimaltest.py
# @Software: PyCharm


from decimal import Decimal
import decimal


if __name__ == '__main__':
    print('----------')
    decimal.getcontext().prec = 2
    x = Decimal(str(0.1))
    print(x)
    y = Decimal.from_float(3)
    print(x * y)
