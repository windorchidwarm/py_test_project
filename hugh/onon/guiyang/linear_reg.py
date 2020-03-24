#!/usr/bin/env python
# -- coding: utf-8 --#
# @Time : 2020/3/24 17:05 
# @Author : Aries 
# @Site :  
# @File : linear_reg.py 
# @Software: PyCharm


import pandas as pd
import statsmodels.api as sm



def getDataFrameResTable(res, i):
    resHtml = res.tables[i].as_html()
    temp = pd.read_html(resHtml)[0]
    return temp.to_json(orient='index')

def test_linear(X, y):
    '''

    :param X:
    :param y:
    :return:
    '''
    X = sm.add_constant(X)
    model = sm.OLS(y, X)
    est = model.fit()
    res = est.summary()
    trainDf = pd.DataFrame(est.fittedvalues)
    trainDf.columns = ['prediction']
    print(res)
    table0 = getDataFrameResTable(res, 0)
    table1 = getDataFrameResTable(res, 1)
    table2 = getDataFrameResTable(res, 2)
    print(table0)



if __name__ == '__main__':
    print('xxx')
    df = pd.read_csv(r'C:\Users\BBD\Desktop\test\tmp\Cshl0V1SGLeAb6opAABKW103UTU063.csv')
    print(df)
    y = df['商场ID']
    X = df[['编号', '商户ID', '单位面积营业额', '客流转换率变化情况']]
    test_linear(X, y)
