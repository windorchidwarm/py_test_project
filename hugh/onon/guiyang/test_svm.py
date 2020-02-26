#!/usr/bin/env python
# -- coding: utf-8 --#
# @Time : 2020/2/26 13:56 
# @Author : Aries 
# @Site :  
# @File : test_svm.py 
# @Software: PyCharm


import pandas as pd
from sklearn import svm
import numpy as np
from scipy import stats


def svc_test(df, label):
    '''
    svm 分类模型
    :param df:
    :return:
    '''
    y = df[label]
    X = df.loc[:, df.columns != label]
    print('yyyyyyyyyyyyyyy')
    print(y)
    print(X)
    print(y.values)
    print(X.values)
    clf = svm.SVC(C=1, kernel='rbf', gamma=1, decision_function_shape='ovo')
    res = clf.fit(X.values, y.values)
    print(clf.fit_status_)
    print(res)
    dd = res.predict(X.values)
    print(dd)


def test_svm_svc():
    np.random.seed(0)
    N = 20
    x = np.empty((4 * N, 2))
    print('xxxxxxxxxxxxxxxxxxx')
    print("{}\n{}".format(x.shape, x))
    means = [(-1, 1), (1, 1), (1, -1), (-1, -1)]
    print(means)
    sigmas = [np.eye(2), 2 * np.eye(2), np.diag((1, 2)), np.array(((2, 1), (1, 2)))]
    print(sigmas)
    for i in range(4):
        mn = stats.multivariate_normal(means[i], sigmas[i] * 0.3)
        # print(mn)
        x[i * N:(i + 1) * N, :] = mn.rvs(N)
        # print(mn.rvs(N))
    a = np.array((0, 1, 2, 3)).reshape((-1, 1))
    print(a)
    y = np.tile(a, N).flatten()
    print('xxxxxxxxxxxxxxxxxxx')
    print(np.tile(a, N))
    print('xxxxxxxxxxxxxxxxxxx')
    print(y)
    print('xxxxxxxxxxxxxxxxxxx')
    print(x)
    clf = svm.SVC(C=1, kernel='rbf', gamma=1, decision_function_shape='ovo')
    # clf = svm.SVC(C=1, kernel='linear', decision_function_shape='ovr')
    clf.fit(x, y)
    print(clf)
    y_hat = clf.predict(x)


if __name__ == '__main__':
    print('xxx')
    df = pd.read_csv(r'C:\Users\BBD\Desktop\test\tmp\Cshl0V1SGLeAb6opAABKW103UTU063.csv')
    print(df)

    # test_svm_svc()
    # updf = df.select(['编号', '商场ID', '商户ID', '单位面积营业额', '单位面积租金'], axis=1)
    # labels = ['编号', '商场ID', '商户ID', '单位面积营业额', '单位面积租金']
    updf = df[['编号', '商场ID', '商户ID', '单位面积营业额', '客流转换率变化情况']]
    label = '编号'
    print(updf)
    svc_test(updf, label)