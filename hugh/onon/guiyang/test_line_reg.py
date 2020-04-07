#!/usr/bin/env python
# -- coding: utf-8 --#
# @Time : 2020/4/1 13:40 
# @Author : Aries 
# @Site :  
# @File : test_line_reg.py 
# @Software: PyCharm


import pandas as pd
from sklearn import linear_model

def test_lasso(X, label):
    '''
    Lasso
    :return:
    '''
    model = linear_model.Lasso(random_state=9, alpha=1, tol=0.001, max_iter=1000)
    model.fit(X, label)
    print(model)
    pre_data = model.predict(X)
    print(pre_data)


def test_rideg(X, label):
    '''
    Lasso
    :return:
    '''
    model = linear_model.Ridge(random_state=9, alpha=1, solver='auto', tol=0.001, max_iter=1000)
    model.fit(X, label)
    print(model)
    pre_data = model.predict(X)
    print(pre_data)



if __name__ == '__main__':
    '''
    测试线性回归
    '''
    print('xxx')
    df = pd.read_csv(r'C:\Users\BBD\Desktop\test\tmp\Cshl0V1SGLeAb6opAABKW103UTU063.csv')
    print(df)

    # test_svm_svc()
    # updf = df.select(['编号', '商场ID', '商户ID', '单位面积营业额', '单位面积租金'], axis=1)
    # labels = ['编号', '商场ID', '商户ID', '单位面积营业额', '单位面积租金']
    updf = df[['编号', '商场ID', '商户ID', '单位面积营业额', '客流转换率变化情况']]
    label = '编号'
    y = updf['编号']
    X = updf[['商场ID', '商户ID', '单位面积营业额', '客流转换率变化情况']]
    test_lasso(X.values, y.values)
    test_rideg(X, y)
    print(updf)