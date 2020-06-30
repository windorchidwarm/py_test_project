#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : svm_test.py
# Author: hugh
# Date  : 2020/6/30

from sklearn import svm
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.preprocessing import StandardScaler

base_path = os.path.dirname(os.path.realpath(__file__))\
    .replace(os.path.join('hugh', os.path.join('base_some', 'base_data_ana')), '')
print(base_path)

file_dir = os.path.join(os.path.join(base_path, 'files'), 'breast_cancer_data')


def get_data_clean():
    data = pd.read_csv(os.path.join(file_dir, 'data.csv'))

    # 数据探索
    # 显示所有列
    pd.set_option('display.max_columns', None)
    print(data.columns)
    print(data.head(5))
    print(data.describe())

    # 将特征字段分成3组 mean 代表平均值，se 代表标准差，worst 代表最大值
    features_mean = list(data.columns[2:12])
    features_se = list(data.columns[12:22])
    features_worst = list(data.columns[22:32])

    # 数据清洗
    # ID列没有用，删除该列
    data.drop('id', axis=1, inplace=True)
    # 将B良性替换为0，M恶性替换为1
    data['diagnosis'] = data['diagnosis'].map({'M': 1, 'B': 0})

    # 肿瘤诊断结果可视化
    sns.countplot(data['diagnosis'], label='Count')
    plt.show()

    # 用热力图呈现features_mean字段之间的相关性
    corr = data[features_mean].corr()
    plt.figure(figsize=(14, 14))
    # annot = True 显示每个方格的数据
    sns.heatmap(corr, annot=True)
    plt.show()
    return data

def test_svm():
    '''
    LinearSVC SVR SVC

    svc:model = svm.SVC(kernel=‘rbf’, C=1.0, gamma=‘auto’)
    kernel 代表核函数的选择，
    linear：线性核函数
    poly：多项式核函数
    rbf：高斯核函数（默认）
    sigmoid：sigmoid 核函数
    用 sigmoid 核函数时，SVM 实现的是多层神经网络。
    参数 C 代表目标函数的惩罚系数，惩罚系数指的是分错样本时的惩罚程度，默认情况下为 1.0。
    当 C 越大的时候，分类器的准确性越高，但同样容错率会越低，泛化能力会变差。
    相反，C 越小，泛化能力越强，但是准确性会降低。
    参数 gamma 代表核函数的系数，默认为样本特征数的倒数，即 gamma = 1 / n_features。

    :return:
    '''
    data = get_data_clean()

    # 特征选择
    features_remain = ['radius_mean', 'texture_mean', 'smoothness_mean', 'compactness_mean', 'symmetry_mean',
                       'fractal_dimension_mean']
    # 抽取30%的数据作为测试集，其余作为训练集
    train, test = train_test_split(data, test_size=0.3)  # in this our main data is splitted into train and test
    # 抽取特征选择的数值作为训练和测试数据
    train_X = train[features_remain]
    train_y = train['diagnosis']
    test_X = test[features_remain]
    test_y = test['diagnosis']
    # 采用Z-Score规范化数据，保证每个特征维度的数据均值为0，方差为1
    ss = StandardScaler()
    train_X = ss.fit_transform(train_X)
    test_X = ss.transform(test_X)

    # 创建svm分类器
    model = svm.SVC()
    # 训练和测试
    model.fit(train_X, train_y)
    pre = model.predict(test_X)
    print(metrics.accuracy_score(pre, test_y))

def test_svm_linear():
    data = get_data_clean()
    # 特征选择
    # features_remain = ['radius_mean','texture_mean', 'smoothness_mean','compactness_mean','symmetry_mean', 'fractal_dimension_mean']
    features_remain = data.columns[1:31]
    print(features_remain)
    print('-' * 100)
    # 抽取30%的数据作为测试集，其余作为训练集
    train, test = train_test_split(data, test_size=0.3)  # in this our main data is splitted into train and test
    # 抽取特征选择的数值作为训练和测试数据
    train_X = train[features_remain]
    train_y = train['diagnosis']
    test_X = test[features_remain]
    test_y = test['diagnosis']

    # 采用Z-Score规范化数据，保证每个特征维度的数据均值为0，方差为1
    ss = StandardScaler()
    train_X = ss.fit_transform(train_X)
    test_X = ss.transform(test_X)

    # 创建SVM分类器
    model = svm.LinearSVC()
    # 用训练集做训练
    model.fit(train_X, train_y)
    # 用测试集做预测
    prediction = model.predict(test_X)
    print('准确率: ', metrics.accuracy_score(prediction, test_y))


if __name__ == '__main__':
    '''
    svm support vector machine 支持向量机
    
    决策面的极限位置：如果越过这个位置，就会产生分类错误
    分类间隔：极限位置的分界位置就是最优决策面，极限位置到最优决策面之间的距离，就是“分类间隔”，margin
    可能存在多个最优决策面
    拥有最大间隔的决策面就是svm寻找的最优解
    
    超平面的数学公式： g(x)=ω^T*x+b 其中ω,x∈R^n
    公式中，ω x是n维空间里的向量，其中x是函数变量，ω是法向量。
    法向量这里指的是垂直于平面的直线所表示的向量，决定了超平面的方向。
    支持向量就是离分类超平面最近的样本点，实际上如果确定了支持向量也就确定了超平面。
    
    di表示点xi到超平面ωxi+b=0的欧式距离。要求di的最小值，即
    di = |ωxi+b|/||ω|| ||ω||为超平面的范数，di的公式可以用解析几何知识进行推导。
    
    最大间隔的优化模型
    目标是寻找出所有分类间隔中最大的那个值对应的超平面，在数学中是凸优化问题。
    中间求解过程会用到朗格朗日乘子和KKT(Karush-Kuhn-Tucker)条件
    
    硬间隔 软间隔 和 非线性svm
    硬间隔指的就是完全分类准确，不能存在分类错误的情况。软间隔，就是允许一定量的样本分类错误。
    核函数。它可以将样本从原始空间映射到一个更高维的特质空间中，使得样本在新的空间中线性可分。
    最常用的核函数有线性核、多项式核、高斯核、拉普拉斯核、sigmoid 核
    
    用 SVM 如何解决多分类问题
    svm是一个二值分类器，解决多分类器有“一对多法”和“一对一法”
    假设我们要把物体分成 A、B、C、D 四种分类，那么我们可以先把其中的一类作为分类 1，其他类统一归为分类 2。
    这样我们可以构造 4 种 SVM
    这种方法，针对 K 个分类，需要训练 K 个分类器，分类速度较快，但训练速度较慢，
    因为每个分类器都需要对全部样本进行训练，而且负样本数量远大于正样本数量，会造成样本不对称的情况，
    而且当增加新的分类，比如第 K+1 类时，需要重新对分类器进行构造。
    
    一对一法的初衷是想在训练的时候更加灵活。我们可以在任意两类样本之间构造一个 SVM，
    这样针对 K 类的样本，就会有 C(k,2) 类分类器
    当对一个未知样本进行分类时，每一个分类器都会有一个分类结果，即为 1 票，最终得票最多的类别就是整个未知样本的类别
    这样做的好处是，如果新增一类，不需要重新训练所有的 SVM，只需要训练和新增这一类样本的分类器。
    而且这种方式在训练单个 SVM 模型的时候，训练速度快
    但这种方法的不足在于，分类器的个数与 K 的平方成正比，所以当 K 较大时，训练和测试的时间会比较慢。
    
    '''
    test_svm()
    test_svm_linear()