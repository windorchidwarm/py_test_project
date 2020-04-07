#!/usr/bin/env python
# -- coding: utf-8 --#
# @Time : 2020/4/7 16:17 
# @Author : Aries 
# @Site :  
# @File : neural_network.py 
# @Software: PyCharm


import pandas as pd
from sklearn.neural_network import MLPClassifier


def test_neural_network(df, label):
    '''
    神经网络
    :param df:
    :param label:
    :return:
    '''
    y = df[label]
    X = df.loc[:, df.columns != label]
    #  {'identity', 'logistic', 'tanh', 'relu'}, default='relu'
    activation = 'identity'
    n = [2]
    randomState = 9
    maxIter = 3
    # 初始化模型
    mlp = MLPClassifier(activation=activation, hidden_layer_sizes=n,
                        random_state=randomState, max_iter=maxIter)
    # 训练
    mlp.fit(X, y)
    # 保存模型

    # 输出 1 coefficients
    coefs_ = mlp.coefs_
    # 输出 2： intercepts
    intercepts_ = mlp.intercepts_
    # 输出 3 损失函数
    loss_curve_ = mlp.loss_curve_
    print(mlp)
    print(coefs_)
    print(intercepts_)
    print(loss_curve_)



if __name__ == '__main__':
    print('xxx')
    df = pd.read_csv(r'C:\Users\BBD\Desktop\test\tmp\Cshl0V1SGLeAb6opAABKW103UTU063.csv')
    print(df)

    # test_svm_svc()
    # updf = df.select(['编号', '商场ID', '商户ID', '单位面积营业额', '单位面积租金'], axis=1)
    # labels = ['编号', '商场ID', '商户ID', '单位面积营业额', '单位面积租金']
    updf = df[['编号', '商场ID', '商户ID', '单位面积营业额', '客流转换率变化情况', '是否掉铺']]
    label = '是否掉铺'
    updf = updf.append(updf, ignore_index=True, sort=False)
    updf = updf.append(updf, ignore_index=True, sort=False)
    print(updf)

    # svc_test(updf, label)
    test_neural_network(updf, label)