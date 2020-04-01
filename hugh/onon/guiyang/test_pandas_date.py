#!/usr/bin/env python
# -- coding: utf-8 --#
# @Time : 2020/3/30 15:46 
# @Author : Aries 
# @Site :  
# @File : test_pandas_date.py 
# @Software: PyCharm


import pandas as pd


if __name__ == '__main__':
    print('xxx')
    df = pd.read_excel(r'C:\Users\BBD\Desktop\test\tmp\有表头.xls')
    print(df)
    print(type(df))
    print(df.dtypes)
    i = 0 if '创建日期' in df.columns else 1
    print(i)