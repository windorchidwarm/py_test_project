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
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
import pickle
import os


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

    csv = svm.SVC()
    parmaters = { 'C':[1,2,3,4]}
    # gsc = GridSearchCV(csv, parmaters, cv=2, verbose=2)
    # print(gsc)
    # gsc.fit(X.values, y.values)
    # print(gsc.cv_results_)

    param_search = RandomizedSearchCV(estimator=csv,
                                      param_distributions=parmaters,
                                      cv=2,
                                      verbose=2)
    param_search.fit(X.values, y.values)
    print(param_search.best_estimator_)
    print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')

    pickle_file = r'C:\Users\BBD\Desktop\test\test\test.pkl'

    # if not os.path.isfile(pickle_file):
    #     os.mknod(pickle_file)
    f = open(pickle_file, 'wb')
    pickle.dump(param_search, f)
    f.close()

    f1 = open(pickle_file, 'rb')
    test_param_search = pickle.load(f1)
    print(test_param_search.predict(X.values))


def test_svm_svr(df, label):
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
    # clf = svm.SVC(C=1, kernel='rbf', gamma=1, decision_function_shape='ovo')
    # res = clf.fit(X.values, y.values)
    # print(clf.fit_status_)
    # print(res)
    # dd = res.predict(X.values)
    # print(dd)

    svr = svm.SVR()
    svr.kernel = 'rbf'
    svr.gamma = 'scale'
    svr.random_state = 3
    parmaters = {'C': [1, 2, 3, 4], 'degree':[1, 2, 3, 4]}
    # cls = svm.SVR(C=C, kernel=kernel, degree=degree, tol=tol, class_weight=class_weight, max_iter=max_iter,
    #               gamma=gamma)
    param_search = RandomizedSearchCV(estimator=svr,
                                      param_distributions=parmaters,
                                      cv=2,
                                      verbose=2)
    param_search.fit(X.values, y.values)
    print(param_search.best_estimator_)
    print(svr)
    svr.degree = param_search.best_estimator_.degree
    print(svr)
    print(param_search.estimator)
    print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')




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
    updf = updf.append(updf, ignore_index=True, sort=False)
    updf = updf.append(updf, ignore_index=True, sort=False)
    print(updf)

    svc_test(updf, label)
    # test_svm_svr(updf, label)