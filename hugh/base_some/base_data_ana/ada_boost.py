#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : ada_boost.py
# Author: hugh
# Date  : 2020/7/22

from sklearn.ensemble import AdaBoostClassifier,AdaBoostRegressor
import pandas as db
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn import metrics

import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.metrics import zero_one_loss
from sklearn.tree import DecisionTreeClassifier


def test_adb():
    data = datasets.load_boston()
    print(data)
    train_x, test_x, train_y, test_y = train_test_split(data.data, data.target, test_size=0.25, random_state=33)
    print(train_x)
    regressor = AdaBoostRegressor()
    print(regressor)
    regressor.fit(train_x, train_y)
    print(regressor)
    pre_y = regressor.predict(test_x)
    mse = metrics.mean_squared_error(test_y, pre_y)
    print(mse)

def show():
    # 设置AdaBoost迭代次数
    n_estimators = 200
    # 使用
    X, y = datasets.make_hastie_10_2(n_samples=12000, random_state=1)
    # 从12000个数据中取前2000行作为测试集，其余作为训练集
    train_x, train_y = X[2000:], y[2000:]
    test_x, test_y = X[:2000], y[:2000]
    # 弱分类器
    dt_stump = DecisionTreeClassifier(max_depth=1, min_samples_leaf=1)
    dt_stump.fit(train_x, train_y)
    dt_stump_err = 1.0 - dt_stump.score(test_x, test_y)
    # 决策树分类器
    dt = DecisionTreeClassifier()
    dt.fit(train_x, train_y)
    dt_err = 1.0 - dt.score(test_x, test_y)
    # AdaBoost分类器
    ada = AdaBoostClassifier(base_estimator=dt_stump, n_estimators=n_estimators)
    ada.fit(train_x, train_y)
    # 三个分类器的错误率可视化
    fig = plt.figure()
    # 设置plt正确显示中文
    plt.rcParams['font.sans-serif'] = ['SimHei']
    ax = fig.add_subplot(111)
    ax.plot([1, n_estimators], [dt_stump_err] * 2, 'k-', label=u'决策树弱分类器 错误率')
    ax.plot([1, n_estimators], [dt_err] * 2, 'k--', label=u'决策树模型 错误率')
    ada_err = np.zeros((n_estimators,))
    # 遍历每次迭代的结果 i为迭代次数, pred_y为预测结果
    for i, pred_y in enumerate(ada.staged_predict(test_x)):
        # 统计错误率
        ada_err[i] = zero_one_loss(pred_y, test_y)
    # 绘制每次迭代的AdaBoost错误率
    ax.plot(np.arange(n_estimators) + 1, ada_err, label='AdaBoost Test 错误率', color='orange')
    ax.set_xlabel('迭代次数')
    ax.set_ylabel('错误率')
    leg = ax.legend(loc='upper right', fancybox=True)
    plt.show()

if __name__ == '__main__':
    '''
    AdaBoost Adaptive Boosting 自适应提升算法
    
    设弱分类器为Gi(x) 在强分类器中权重为αi，则可以得到强分类器f(x)
    f(x)=∑αiGi(x)
    
    用弱分类器对样本的分类错误率来决定权重 错误率ei
    αi = 1/2*log[(1-ei)/ei]
    
    AdaBoost 会判断每次训练的样本是否正确分类，对于正确分类的样本，降低它的权重，对于被错误分类的样本，增加它的权重。
    再基于上一次得到的分类准确率，来确定这次训练样本中每个样本的权重。
    我们可以用 Dk+1​ 代表第 k+1 轮训练中，样本的权重集合，其中 Wk+1,1​ 
    代表第 k+1 轮中第一个样本的权重，以此类推 Wk+1,N​ 代表第 k+1 轮中第 N 个样本的权重
    Dk+1 = (Wk+1,1 ,Wk+1,2 , ....)
    第k+1论中的样本权重 是根据该样本在第 k 轮的权重以及第 k 个分类器的准确率而定
    Wk+1,i = Wk,i / Zk * exp(-αk Yi Gk(xi))
    '''
    test_adb()
    show()