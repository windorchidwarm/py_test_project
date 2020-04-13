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


def changeToNum(x):
    try:
        float(x)
    except ValueError:
        x = None
    return x


def changeNumberType(df, filedName, type):
    try:
        df[filedName] = df[filedName].astype(type)
    except ValueError:
        df[filedName] = df[filedName].apply(changeToNum)
        df[filedName] = df[filedName].astype('float')
    return df


def changeLocalDatatype(allDf, outDataTypes):
    for i in range(len(outDataTypes)):
        if outDataTypes[i]['dataType'] == 'date':
            try:
                allDf[outDataTypes[i]['filedName']] = pd.to_datetime(allDf[outDataTypes[i]['filedName']])
            except Exception as e:
                allDf[outDataTypes[i]['filedName']] = allDf[outDataTypes[i]['filedName']].astype('object')
        elif outDataTypes[i]['dataType'] == 'int':
            if allDf[outDataTypes[i]['filedName']].isnull().any() or allDf[outDataTypes[i]['filedName']].dtype == 'float':
                allDf = changeNumberType(allDf, outDataTypes[i]['filedName'], 'float')
            else:
                allDf = changeNumberType(allDf, outDataTypes[i]['filedName'], 'int')
        elif outDataTypes[i]['dataType'] == 'float':
            allDf = changeNumberType(allDf, outDataTypes[i]['filedName'], 'float')
        else:
            allDf[outDataTypes[i]['filedName']] = allDf[outDataTypes[i]['filedName']].astype('object')
    return allDf


if __name__ == '__main__':
    print('xxx')
    local = r'C:\Users\BBD\Desktop\test\tmp\tt.csv'
    remote = b'group1/M00/03/3B/ChQUAV6QCIeAVfgKAAACN4l15-A474.csv'
    down_load_file(remote, local)
    df = pd.read_csv(local, sep='\u0001')
    print(df)
    print(df.columns)
    checkNullValues(df)
    print(str(df.head(10)))

    data = [{'filedName': '创建日期', 'dataType': 'date'}, {'filedName': '商品价格', 'dataType': 'float'}, {'filedName': '创建人', 'dataType': 'str'}, {'filedName': '商品编号', 'dataType': 'float'}]
    print(data)
    columns = ['创建日期', '商品价格', '创建人', '商品编号']
    df.columns = columns
    print(df)
    df = changeLocalDatatype(df, data)
    print(df)

    col_test = df.columns
    print(type(col_test))
    col_test = col_test.insert(len(col_test), 'test')
    t_pd = pd.DataFrame(columns = col_test)
    print('----------')
    print(t_pd)
    print('----------')
    print(t_pd.columns)
    print('----------')
    print(type(t_pd))