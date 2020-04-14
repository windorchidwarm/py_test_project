#!/usr/bin/env python
# -- coding: utf-8 --#
# @Time : 2020/4/10 13:42 
# @Author : Aries 
# @Site :  
# @File : test_data_pandas_null.py 
# @Software: PyCharm


import pandas as pd
from hugh.cyan.pandas.test_fastdfs import *
import json


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


def test_delete_json(data):
    latest_out_put = json.loads(data)
    k = '0'
    if k in latest_out_put.keys():
        # 删除原来的中间文件
        latest_old = latest_out_put[k]
        delete_file(latest_old['allDataPath'].replace("\"", '').encode('utf-8'))
        delete_file(latest_old['displayDataPath'].replace("\"", '').encode('utf-8'))
        delete_file(latest_old['downloadDataPath'].replace("\"", '').encode('utf-8'))


if __name__ == '__main__':
    print('xxx')

    data = '{"0":{"displayDataPath":"group1/M00/03/44/ChQUAV6UHLCACHUvAAAASg_DaMw075.csv","allDataPath":"group1/M00/01/29/ChQKKV6UHLCAFFMjAAAASg_DaMw850.csv","downloadDataPath":"group1/M00/01/29/ChQKKV6UHLCASDpdAAAASi1l-Pk649.csv","statisticData":{"str":3,"date":0,"targetAllDir":"group1/M00/01/29/ChQKKV6UHLCAFFMjAAAASg_DaMw850.csv","targetDisplayDir":"group1/M00/03/44/ChQUAV6UHLCACHUvAAAASg_DaMw075.csv","address":{"min":1,"fieldName":"address","distData":[{"上海":1},{"北京":1}],"max":1,"defectCount":1,"dataType":"string","uniqueCount":3},"name":{"min":1,"fieldName":"name","distData":[{"zhangsian2":1},{"zhangsian1":1},{"李华":1}],"max":1,"defectCount":0,"dataType":"string","uniqueCount":3},"float":0,"totalCount":3,"targetDownloadDir":"group1/M00/01/29/ChQKKV6UHLCASDpdAAAASi1l-Pk649.csv","class":{"min":2,"fieldName":"class","distData":[{"1班":2}],"max":2,"defectCount":1,"dataType":"string","uniqueCount":2},"int":0}}}'
    # test_delete_json(data)

    local = r'C:\Users\BBD\Desktop\test\tmp\tt.csv'
    remote = b'group1/M00/01/29/ChQKKV6UJo6AKA7RAAAANi5XJdA093.csv'
    down_load_file(remote, local)
    df = pd.read_csv(local, sep='\u0001')
    print(df)
    # print(df.columns)
    # checkNullValues(df)
    # print(str(df.head(10)))
    #
    # data = [{'filedName': '创建日期', 'dataType': 'date'}, {'filedName': '商品价格', 'dataType': 'float'}, {'filedName': '创建人', 'dataType': 'str'}, {'filedName': '商品编号', 'dataType': 'float'}]
    # print(data)
    # columns = ['创建日期', '商品价格', '创建人', '商品编号']
    # df.columns = columns
    # print(df)
    # df = changeLocalDatatype(df, data)
    # print(df)
    #
    # col_test = df.columns
    # print(type(col_test))
    # col_test = col_test.insert(len(col_test), 'test')
    # t_pd = pd.DataFrame(columns = col_test)
    # print('----------')
    # print(t_pd)
    # print('----------')
    # print(t_pd.columns)
    # print('----------')
    # print(type(t_pd))