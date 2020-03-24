#!/usr/bin/env python
# -- coding: utf-8 --#

import pandas as pd
import numpy as np
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from scipy import stats
import datetime
from fdfs_client.client import *
import re
from pyspark.sql.functions import udf
from pyspark.sql.types import StringType
from pyspark.ml.linalg import VectorUDT
import os
import joblib

def dataDistributionLocal(df):
    '''
    计算单机版的数据分布
    :param data:
    :return:
    '''

    def getDealFun(df):
        dict = {}
        for fieldName in df.columns:
            if str(df[fieldName].dtype).lower() in ['int32', 'int64', 'uint8']:
                dataTypeCount['int'] = dataTypeCount['int'] + 1
                dict[fieldName] = dealNum
            elif str(df[fieldName].dtype).lower() in ['float32', 'float64']:
                dataTypeCount['float'] = dataTypeCount['float'] + 1
                dict[fieldName] = dealNum
            elif str(df[fieldName].dtype).lower() in ['date', 'datetime', 'datetime64', 'datetime32', 'datetime64[ns]', 'datetime32[ns]']:
                dataTypeCount['date'] = dataTypeCount['date'] + 1
                dict[fieldName] = dealDate
            elif str(df[fieldName].dtype).lower() in ['object']:
                dataTypeCount['str'] = dataTypeCount['str'] + 1
                dict[fieldName] = dealStr
            else:
                dict[fieldName] = notDeal
        return dict

    def dealStr(fieldName, showLen=20):
        '''
        处理字符串类型
        :param fieldName:
        :param showLen:
        :return:
        '''
        retDict = {}

        #空列的处理
        if df[fieldName].isnull().all():
            retDict['max'] = 0
            retDict['min'] = 0
            retDict['uniqueCount'] = 0
            retDict['defectCount'] = int(countAll)
            retDict['distData'] = []
            retDict['fieldName'] = fieldName
            retDict['dataType'] = "string"
            return retDict

        strCount = df[fieldName][df[fieldName] != ''].value_counts(ascending=True, dropna=True)
        # strCount = df[fieldName].value_counts(ascending=True, dropna=True)
        retDict['max'] = int(strCount.max() if not np.isnan(strCount.max()) else 0)
        retDict['min'] = int(strCount.min() if not np.isnan(strCount.min()) else 0)
        # 唯一值
        retDict['uniqueCount'] = int(len(df[fieldName].unique()))
        # 缺失值
        retDict['defectCount'] = int(countAll - sum(strCount))
        # 分布图
        distData = []
        strCountSort = sorted(strCount.items(), key=lambda item: item[1], reverse=True)
        top10Count = 0
        for i in range(min(9, len(strCountSort))):
            top10Count = top10Count + strCountSort[i][1]
            key = str(strCountSort[i][0])
            distData.append({key[0:showLen] + u"......" if key and len(key) > showLen else key: int(strCountSort[i][1])})
        if len(strCountSort) > 10:
            distData.append({'other': int(countAll - top10Count)})
        retDict['distData'] = distData
        retDict['fieldName'] = fieldName
        retDict['dataType'] = "string"
        return retDict

    def dealNum(fieldName):
        '''
        数值类型的处理
        :param fieldName:
        :return:
        '''
        retDict = {}

        # 空列的处理
        if df[fieldName].isnull().all():
            retDict['max'] = 0.0
            retDict['min'] = 0.0
            retDict['uniqueCount'] = 0
            retDict['defectCount'] = int(countAll)
            retDict['boxCount'] = 0
            retDict['segmaCount'] = 0
            retDict['mean'] =0.0
            # 众数
            retDict['mode'] = 0.0
            # 峰度
            retDict['kurt'] = 0.0
            # 偏度
            retDict['skew'] = 0.0
            # 中位数
            retDict['median'] = 0.0
            retDict['quarter1'] = 0.0
            retDict['quarter3'] = 0.0
            retDict['distData'] = []
            retDict['totalCount'] = int(countAll)
            retDict['fieldName'] = fieldName
            retDict['dataType'] = "number"
            return retDict

        pp = df[fieldName].dropna()
        maxv = pp.max()
        minv = pp.min()
        retDict['max'] = float(maxv)
        retDict['min'] = float(minv)
        retDict['mean'] = float(pp.mean())
        # 众数
        retDict['mode'] = float(stats.mode(pp)[0][0])
        # 峰度
        retDict['kurt'] = float(pp.kurt())
        # 偏度
        retDict['skew'] = float(pp.skew())
        # 中位数
        retDict['median'] = pp.median()

        retDict['totalCount'] = int(countAll)

        totalCount = pp.count()
        # 标准差
        if totalCount == 1:
            retDict['stddev'] = 0
        else:
            std_data = pp.std()
            print(std_data)
            std_data = np.nan_to_num(std_data)
            print(std_data)
            retDict['stddev'] = std_data

        # 缺失值
        retDict['defectCount'] = int(countAll - totalCount)
        # 数据分布
        numDistArr = []
        if maxv != minv:
            interv = float(maxv - minv) / 10.0
            levels = []
            for i in range(0, 10):
                v = float(minv) + interv * (i + 1)
                levels.append(float('%.4f' % v))
            preCount = len(pp[pp >= minv])
            afCount = len(pp[pp >= levels[0]])
            numDistArr.append(
                {"{0}~{1}".format(minv, levels[0]): int(preCount - afCount)})
            preCount = afCount
            for i in range(1, len(levels) - 1):
                afCount = len(pp[pp >= levels[i]])
                numDistArr.append(
                    {"{0}~{1}".format(levels[i - 1], levels[i]): int(preCount - afCount)})
                preCount = afCount
            numDistArr.append(
                {"{0}~{1}".format(levels[8], str(maxv)): int(preCount)})
        elif totalCount > 0:
            numDistArr.append({str(maxv): int(totalCount)})

        # box异常率
        pp = df[fieldName].dropna()
        percentile = np.percentile(pp, [0, 25, 50, 75, 100])
        # percentile = np.percentile(pp, [0, 25, 50, 75, 100])
        retDict['quarter1'] = percentile[1]
        retDict['quarter3'] = percentile[3]

        iqr = percentile[3] - percentile[1]
        upLimit = percentile[3] + iqr * 1.5
        downLimit = percentile[1] - iqr * 1.5
        pp = pp[pp <= upLimit]
        pp = pp[pp >= downLimit]
        retDict['boxCount'] = int(countAll - pp.count())

        # segma的异常率
        pp = df[fieldName].dropna()
        mean = pp.mean()
        std = pp.std()
        meanUp = mean + 3 * std
        meanDown = mean - 3 * std
        pp = pp[pp <= meanUp]
        pp = pp[pp >= meanDown]
        retDict['segmaCount'] = int(countAll - pp.count())

        retDict['distData'] = numDistArr
        retDict['fieldName'] = fieldName
        retDict['dataType'] = "number"
        return retDict

    def dealDate(fieldName):
        '''
        时间类型处理
        :param fieldName:
        :return:
        '''
        retDict = {}

        # 空列的处理
        if df[fieldName].isnull().all():
            retDict['max'] = 0
            retDict['min'] = 0
            retDict['uniqueCount'] = 0
            retDict['defectCount'] = int(countAll)
            retDict['distData'] = []
            retDict['fieldName'] = fieldName
            retDict['dataType'] = "date"
            return retDict

        datep = df[fieldName].dropna()
        # 总数
        dateTotalCount = datep.count()
        maxv = datep.max()
        minv = datep.min()
        retDict['max'] = str(maxv)
        retDict['min'] = str(minv)
        # 久期
        dateSpan = (maxv - minv) if maxv and minv else datetime.timedelta(0)
        retDict['dateSpan'] = str(dateSpan)
        # 缺失值
        retDict['defectCount'] = int(countAll - dateTotalCount)
        # 数据分布
        dateDistArr = []
        if dateSpan.total_seconds() > 0:
            interv = float(dateSpan.total_seconds()) / 10.0
            levels = []
            dateDistArr = []
            for i in range(0, 10):
                v = (minv if minv else datetime.datetime(1970, 1, 1)) + datetime.timedelta(seconds=interv * (i + 1))
                levels.append(v)
            preCount = len(datep[datep >= minv])
            afCount = len(datep[datep >= levels[0]])
            dateDistArr.append({"{0}~{1}".format(minv.strftime('%Y-%m-%d %H:%M:%S'), levels[0].strftime('%Y-%m-%d %H:%M:%S')): int(preCount - afCount)})
            preCount = afCount
            for i in range(1, len(levels) - 1):
                afCount = len(datep[datep >= levels[i]])
                dateDistArr.append({"{0}~{1}".format(levels[i - 1].strftime('%Y-%m-%d %H:%M:%S'), levels[i].strftime('%Y-%m-%d %H:%M:%S')): int(preCount - afCount)})
                preCount = afCount
            dateDistArr.append({"{0}~{1}".format(levels[8].strftime('%Y-%m-%d %H:%M:%S'), maxv.strftime('%Y-%m-%d %H:%M:%S')): int(preCount)})
        elif dateTotalCount > 0:
            dateDistArr.append({str(maxv): int(dateTotalCount)})
        retDict['distData'] = dateDistArr
        retDict['fieldName'] = fieldName
        retDict['dataType'] = "date"
        return retDict

    def notDeal(fieldName):
        '''
        不处理的计算类型
        :param fieldName:
        :return:
        '''
        retDict = {}
        return retDict

    dataTypeCount = {"int": 0, "float": 0, "str": 0, "date": 0}
    dict = getDealFun(df)
    retDict = {}
    countAll = len(df)
    for fieldName, dealFun in dict.items():
        retDict[fieldName] = dealFun(fieldName)

    # retDict["totalTypeCount"] = dataTypeCount
    retDict.update(dataTypeCount)
    retDict['totalCount'] = int(countAll)
    return retDict
