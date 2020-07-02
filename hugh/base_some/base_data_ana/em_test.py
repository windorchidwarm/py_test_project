#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : em_test.py
# Author: hugh
# Date  : 2020/7/2


from sklearn.mixture import GaussianMixture
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import preprocessing
import seaborn as sns
from sklearn import metrics

import os

base_path = os.path.dirname(os.path.realpath(__file__))\
    .replace(os.path.join('hugh', os.path.join('base_some', 'base_data_ana')), '')
print(base_path)

file_dir = os.path.join(os.path.join(base_path, 'files'), 'em')

def test_gmm():
    '''
    GaussianMixture(covariance_type='full', init_params='kmeans', max_iter=100,
        means_init=None, n_components=1, n_init=1, precisions_init=None,
        random_state=None, reg_covar=1e-06, tol=0.001, verbose=0,
        verbose_interval=10, warm_start=False, weights_init=None)
    n_components:即高斯混合模型的个数，也就是我们要聚类的个数，默认值为 1
    covariance_type:代表协方差类型
    covariance_type=full，代表完全协方差，也就是元素都不为 0；
    covariance_type=tied，代表相同的完全协方差；
    covariance_type=diag，代表对角协方差，也就是对角不为 0，其余为 0；
    covariance_type=spherical，代表球面协方差，非对角为 0，对角完全相同，呈现球面的特性。

    :return:
    '''
    data_ori = pd.read_csv(os.path.join(file_dir, 'heros.csv'), encoding='gb18030')
    print(data_ori.describe())
    features = [u'最大生命', u'生命成长', u'初始生命', u'最大法力', u'法力成长', u'初始法力', u'最高物攻', u'物攻成长', u'初始物攻', u'最大物防', u'物防成长',
                u'初始物防', u'最大每5秒回血', u'每5秒回血成长', u'初始每5秒回血', u'最大每5秒回蓝', u'每5秒回蓝成长', u'初始每5秒回蓝', u'最大攻速', u'攻击范围']
    data = data_ori[features]
    # 设置plt正确显示中文
    plt.rcParams['font.sans-serif'] = ['SimHei'] # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    corr = data.corr()
    sns.heatmap(corr, annot=True)
    plt.show()
    print(data[u'最大攻速'])
    # x_data = data.copy()
    # x_data.loc[:, u'最大攻速'] = x_data.loc[:, u'最大攻速'].apply(lambda x: float(x.strip('%')) / 100)
    # x_data.loc[:, u'攻击范围'] = x_data.loc[:, u'攻击范围'] .map({'远程': 1, '近战': 0})
    # data.loc[:, u'最大攻速'] = x_data[u'最大攻速']
    # data.loc[:, u'攻击范围'] = x_data[u'攻击范围']
    data[u'最大攻速'] = data[u'最大攻速'].apply(lambda x: float(x.strip('%')) / 100)
    data[u'攻击范围'] = data[u'攻击范围'].map({'远程': 1, '近战': 0})
    ss = preprocessing.StandardScaler()
    data = ss.fit_transform(data)
    gmm = GaussianMixture(n_components=30, covariance_type='full')
    gmm.fit(data)
    predict = gmm.predict(data)
    print(predict)
    data_ori.insert(0, '分组', predict)
    print(data_ori)
    print(metrics.calinski_harabaz_score(data, predict))


if __name__ == '__main__':
    '''
    em Expectation Maximization 最大期望算法
    初始化参数、观察预期、重新估计
    “最大似然”：Maximum Likelihood 
    Likelihood 代表可能性
    
     K-Means 是通过距离来区分样本之间的差别的，且每个样本在计算的时候只能属于一个分类，称之为是硬聚类算法
     EM 聚类在求解的过程中，实际上每个样本都有一定的概率和每个聚类相关，叫做软聚类算法
    常用的 EM 聚类有 GMM 高斯混合模型和 HMM 隐马尔科夫模型
    
    通常，我们可以假设样本是符合高斯分布的（也就是正态分布）。每个高斯分布都属于这个模型的组成部分（component），
    要分成 K 类就相当于是 K 个组成部分。这样我们可以先初始化每个组成部分的高斯分布的参数，
    然后再看来每个样本是属于哪个组成部分。这也就是 E 步骤。
    
    '''
    test_gmm()