#!/usr/bin/env python
# -- coding: utf-8 --#
# @Time : 2020/4/7 13:37 
# @Author : Aries 
# @Site :  
# @File : join_right.py 
# @Software: PyCharm


import pandas as pd



if __name__ == '__main__':
    print('xxxxxxxxx')
    leftDf = pd.read_csv(r'C:\Users\BBD\Desktop\test\tmp\2.csv')
    rightDf = pd.read_csv(r'C:\Users\BBD\Desktop\test\tmp\31.csv')
    print(leftDf)
    print(rightDf)

    data = rightDf.set_index(['class', 'name'])
    print(data)
    l_data = leftDf.set_index(['class', 'name'])
    print(l_data)
    allDf = leftDf.join(rightDf.set_index(['class', 'name']), on=['class', 'name'], how='right', lsuffix='_l', rsuffix='_r')
    print('xxxxxxxxxxxxxx')
    print(allDf)

    allDf2 = pd.merge(leftDf, rightDf, how='right', left_on=['class', 'name'], right_on=['class', 'name'], suffixes=('_x', '_y'))
    print(allDf2)
