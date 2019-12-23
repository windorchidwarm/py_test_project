#!/usr/bin/env python
# -- coding: utf-8 --#

import pandas as pd
from decimal import Decimal

def parseDecimal(var):
    return Decimal(var)

def dealNum(fieldName):
    '''
    数值类型的处理
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
        retDict['dataType'] = "number"
        return retDict

    pp = df[fieldName]

    # print(max(pp))
    maxv = Decimal(0)
    minv = Decimal(0)
    print("----------------")
    print(pp.str.isdecimal())
    print(isinstance(pp[1], (Decimal,)))
    print(isinstance(pp, (Decimal,)))
    print("----------------")
    def maxDeciaml(var):
        global maxv
        print(maxv, '---->', var)
        if var is not None and maxv < Decimal(var):
            maxv = Decimal(var)
    pp.apply(maxDeciaml)
    print(isinstance(pp, (Decimal,)))
    print(maxv)
    minv = pp.min()
    retDict['max'] = str(maxv)
    retDict['min'] = int(minv)
    retDict['mean'] = int(pp.mean())

    totalCount = pp.count()
    # 标准差
    if totalCount == 1:
        retDict['stddev'] = 0
    else:
        retDict['stddev'] = int(pp.std())

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
        numDistArr.append({"{0}-{1}".format(minv, levels[0]): int(preCount - afCount)})
        preCount = afCount
        for i in range(1, len(levels) - 1):
            afCount = len(pp[pp >= levels[i]])
            numDistArr.append({"{0}-{1}".format(levels[i - 1], levels[i]): int(preCount - afCount)})
            preCount = afCount
        numDistArr.append({"{0}-{1}".format(levels[8], str(maxv)): int(preCount)})
    elif totalCount > 0:
        numDistArr.append({str(maxv): int(totalCount)})
    retDict['distData'] = numDistArr
    retDict['fieldName'] = fieldName
    retDict['dataType'] = "number"
    return retDict

df = pd.read_csv(r'C:\Users\Administrator\Desktop\test\tmp\company_name_join_3.csv')
for i in range(len(df.columns)):
    print(i)
countAll = len(df)
for column in df.columns:
    print(column)
    print(df[column].dtype)
    if df[column].dtype == 'object':
        print(df[column].dropna().str.isdecimal())

df['company_gis_lat'].apply(parseDecimal)
for i,v in df.iterrows():
    print(type(v))
print(df['company_gis_lat'])
dict = dealNum('company_gis_lat')
print(dict)
