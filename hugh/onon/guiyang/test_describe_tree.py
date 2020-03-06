#!/usr/bin/env python
# -- coding: utf-8 --#
# @Time : 2020/2/27 16:25 
# @Author : Aries 
# @Site :  
# @File : test_describe_tree.py 
# @Software: PyCharm


import pandas as pd
from sklearn import tree, metrics
import numpy as np



def decision_tree_classifier(df, label):
    '''
    决策树 分类模型
    :param df:
    :param label:
    :return:
    '''
    y = df[label]
    X = df.loc[:, df.columns != label]
    cls = tree.DecisionTreeClassifier()
    cls.fit(X.values, y.values)
    print(cls)
    y_p = cls.predict(X.values)
    print(y.values)
    print(y_p)
    pre = pd.DataFrame(y_p)
    pre.columns = ['prediction']
    print(metrics.mean_squared_error(np.array(y), np.array(pre['prediction'])))



if __name__ == '__main__':
    '''
    决策树测试
    '''
    print('xxx')
    df = pd.read_csv(r'C:\Users\BBD\Desktop\test\tmp\Cshl0V1SGLeAb6opAABKW103UTU063.csv')
    print(df)

    # test_svm_svc()
    # updf = df.select(['编号', '商场ID', '商户ID', '单位面积营业额', '单位面积租金'], axis=1)
    # labels = ['编号', '商场ID', '商户ID', '单位面积营业额', '单位面积租金']
    updf = df[['编号', '商场ID', '商户ID', '单位面积营业额', '客流转换率变化情况']]
    label = '编号'
    print(updf)
    decision_tree_classifier(updf, label)