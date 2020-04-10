#!/usr/bin/env python
# -- coding: utf-8 --#
# @Time : 2020/4/10 13:42 
# @Author : Aries 
# @Site :  
# @File : test_data_pandas_null.py 
# @Software: PyCharm


import pandas as pd
from hugh.cyan.pandas.test_fastdfs import *


def checkNullValues(df):
    '''
    检验是否存在null值
    :param df:
    :return:
    '''
    isNulls = df.isnull().any()
    nullIndexes = []
    cnt = 0
    for isNull in isNulls:
        cnt += 1
        if(isNull == True):
            nullIndexes.append(cnt-1)
    if(len(nullIndexes) > 0):
        nullColumns = []
        columns = df.columns
        for i in nullIndexes:
            nullColumns.append(columns[i])
        excepStr = "输入数据列{0}中存在空值".format(str(nullColumns))
        raise Exception(excepStr)


if __name__ == '__main__':
    print('xxx')
    local = r'C:\Users\BBD\Desktop\test\tmp\tt.csv'
    down_load_file(b'group1/M00/03/3B/ChQUAV6QDYuADte6AAABwHWcPG8687.csv', local)
    df = pd.read_csv(local, sep='\u0001')
    print(df)
    print(df.columns)
    checkNullValues(df)