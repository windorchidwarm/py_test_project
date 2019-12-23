#!/usr/bin/env python
# -- coding: utf-8 --#

import pandas as pd
import seaborn as sns
import numpy as np
import sqlalchemy

if __name__ == '__main__':
    print('################################################')
    allDf = pd.read_csv(r'C:\Users\Administrator\Desktop\test\tmp\线性回归训练集.csv')

    selectColumn = ['label', 'no']

    for column in selectColumn:
        dm = pd.get_dummies(allDf[column], prefix=column)
        allDf = pd.concat([allDf, dm], axis=1)
        print(allDf)

    dm = pd.get_dummies(allDf['label'])
    # dm.columns = ['m', 'l']
    df0 = pd.concat([allDf, dm], axis=1)
    print(df0)

    ##############################################
    engienCmd = 'mysql+pymysql://{username}:{password}@{url}'.format(username='quant',
                                                                     password='bbd123',
                                                                     url='10.28.109.14:3306/sf_test')
    engine = sqlalchemy.create_engine(engienCmd, connect_args={'charset': 'utf8'})

    sql = 'select * from test'
    allDf =pd.read_sql_query(sql, engine)
    percentile = np.percentile(allDf['id'], [0, 25, 50, 75, 100])
    iqr = percentile[3] - percentile[1]
    upLimit = percentile[3] + iqr * 1.5
    downLimit = percentile[1] - iqr * 1.5
    for i in  range(5):
        print(percentile[i])
    print(upLimit, downLimit, iqr)
    def tt(x):
        if x > downLimit and x < upLimit:
            return x
        else:
            print("xxxxxx", x)
            return None
    # allDf['id'] = allDf['id'].map(lambda x: x if x > downLimit and x < upLimit else 0)
    # allDf = allDf[allDf['id'] > downLimit]
    # allDf = allDf[allDf['id'] < upLimit]
    # allDf['id'] = allDf['id'].apply(tt)

    df1 = allDf['id'].dropna()
    mean = df1.mean()
    meanUp = mean + 3*df1.std()
    meanDown = mean - 3*df1.std()
    print(mean, meanUp, meanDown)
    def ttt(x):
        if x > meanDown and x < meanUp:
            return x
        else:
            print("xxxxxx", x)
            return None
    # allDf['id'] = allDf['id'].apply(ttt)
    # allDf = allDf[allDf['id'] > meanDown]
    # allDf = allDf[allDf['id'] < meanUp]

    max = allDf['new'].max()
    min = allDf['new'].min()
    mul = max - min

    def MaxMinNormal(x):
        if x != None:
            return (x - min) / mul
        else:
            return x

    mean = allDf['new'].mean()
    std = allDf['new'].std()
    def ZscoreNormal(x):
        if x != None:
            return (x - mean)/std
        else:
            return x

    allDf['new'] = allDf['new'].apply(ZscoreNormal)
    print(allDf)