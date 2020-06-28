#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : decision_tree_test.py
# Author: hugh
# Date  : 2020/6/28

import numpy as np
import pandas as pd

from sklearn import tree
from sklearn import datasets
from sklearn.model_selection import train_test_split,cross_val_score
from sklearn.metrics import accuracy_score
from sklearn.feature_extraction import DictVectorizer
import sys, os
import graphviz

base_path = os.path.dirname(os.path.realpath(__file__))\
    .replace(os.path.join('hugh', os.path.join('base_some', 'base_data_ana')), '')
print(base_path)


def export_graph(clf):
    dot_data = tree.export_graphviz(clf, out_file=None)
    os.environ["PATH"] += os.pathsep + r'E:\software\graphviz\bin'
    graph = graphviz.Source(dot_data)
    graph.view()

def test_titannic():
    file_base = os.path.join(os.path.join(base_path, 'files'), 'data')
    train_data = pd.read_csv(os.path.join(file_base, 'train.csv'))
    test_data = pd.read_csv(os.path.join(file_base, 'test.csv'))
    print(train_data.info())
    print(test_data.info())
    print(train_data.describe())
    print(test_data.describe())

    # 使用平均年龄来填充年龄中的nan值
    train_data['Age'].fillna(train_data['Age'].mean(), inplace=True)
    test_data['Age'].fillna(test_data['Age'].mean(),inplace=True)
    # 使用票价的均值填充票价中的nan值
    train_data['Fare'].fillna(train_data['Fare'].mean(), inplace=True)
    test_data['Fare'].fillna(test_data['Fare'].mean(),inplace=True)

    # 使用登录最多的港口来填充登录港口的nan值
    train_data['Embarked'].fillna('S', inplace=True)
    test_data['Embarked'].fillna('S', inplace=True)

    # 特征选择
    features = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']
    train_features = train_data[features]
    train_labels = train_data['Survived']
    test_features = test_data[features]

    dvec = DictVectorizer(sparse=False)
    train_features = dvec.fit_transform(train_features.to_dict(orient='record'))
    print(dvec.feature_names_)

    # 构造ID3决策树
    clf = tree.DecisionTreeClassifier(criterion='entropy')
    # 决策树训练
    clf.fit(train_features, train_labels)

    test_features = dvec.transform(test_features.to_dict(orient='record'))
    # 决策树预测
    pred_labels = clf.predict(test_features)

    # 得到决策树准确率
    # acc_decision_tree = round(clf.score(train_features, train_labels), 6)
    # print(u'score准确率为 %.4lf' % acc_decision_tree)

    # 使用K折交叉验证 统计决策树准确率
    print(u'cross_val_score准确率为 %.4lf' % np.mean(cross_val_score(clf, train_features, train_labels, cv=10)))

    export_graph(clf)


def test_cart_dtc():
    iris = datasets.load_iris()
    print(iris)
    features_array = iris['data']
    features_name = list(iris['target_names'])
    features_name.append('label')
    features = pd.DataFrame(features_array)
    print(features.info())
    print(features.describe())
    labels_array = iris['target']
    labels = pd.Series(labels_array)

    print(features)
    print(labels)
    print(features_name)

    train_feature, test_feature, train_label, test_label = \
        train_test_split(features, labels, test_size=0.33, random_state=0)
    clf = tree.DecisionTreeClassifier(criterion='gini')
    print(train_feature)

    print(clf)
    clf.fit(train_feature, train_label)
    test_pre = clf.predict(test_feature)
    score = accuracy_score(test_label, test_pre)
    print(score)
    export_graph(clf)


def test_id3_1():

    data = np.array([[1,1], [1,0], [0, 1], [0,0]])
    target = np.array([1,1,0,0])
    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(data, target)
    export_graph(clf)


def test_id3():
    '''
    测试id3算法
    :return:
    '''
    ent_d = -(3/7 * np.log2(3/7) + 4/7 * np.log2(4/7))
    ent_d1 = - (1/3 * np.log2(1/3) + 2/3 * np.log2(2/3))
    ent_d2 = ent_d3 = -(1/2 * np.log2(1/2) + 1/2 * np.log2(1/2))
    print(ent_d1, ent_d2, ent_d3)
    print(ent_d)
    print((3/7 * ent_d1 + 2/7*ent_d2 + 2/7 * ent_d3))
    gain_d_weather = ent_d - (3/7 * ent_d1 + 2/7*ent_d2 + 2/7 * ent_d3)
    print(gain_d_weather)


if __name__ == '__main__':
    '''
    决策树相关算法测试
    
    剪枝分为预剪枝和后剪枝
    
    纯度和信息熵
    信息熵：表示信息的不确定性
    Entropy(t) = - Σp(i|t)log2p(i|t)
    
    信息增益(ID3算法) 信息增益率(C4.5算法) 基尼指数(Cart算法)
    ID3 算法计算的是信息增益，信息增益指的就是划分可以带来纯度的提高，信息熵的下降。
    它的计算公式，是父亲节点的信息熵减去所有子节点的信息熵。在计算的过程中，
    我们会计算每个子节点的归一化信息熵，即按照每个子节点在父节点中出现的概率，
    来计算这些子节点的信息熵。所以信息增益的公式可以表示为
    Gain(D,a) = Entropy(D) - Σabs(Di)/abs(D) * Entropy(Di)
    后面表示归一化信息熵
    
    信息增益率=信息增益/属性熵
    属性熵
    IV(a) = - ΣDi/D * log2(Di/D)
    
    cart Classification and regression tree 分类回归树
    gini(t) = 1 - Σ[p(Ck|t)]^2
    gini(D,A) = D1/D*gini(D1) + D2/D*gini(D2)
    
    回归树
    最小绝对偏差 LAD |x-μ|
    最小二乘偏差 LSD 1/n * Σ(x-μ)^2
    
    决策树剪枝主要采用CCP法 cost-complexity prune 代价复杂度
    这种剪枝方式用到一个指标叫做节点的表面误差率增益值，以此作为剪枝前后误差的定义。
    α = [C(t)-C(Tt)]/(|T|-1)
    其中 Tt 代表以 t 为根节点的子树，C(Tt) 表示节点 t 的子树没被裁剪时子树 Tt 的误差，
    C(t) 表示节点 t 的子树被剪枝后节点 t 的误差，|Tt|代子树 Tt 的叶子数，剪枝后，
    T 的叶子数减少了|Tt|-1。
    '''
    # test_id3()
    # test_id3_1()
    # test_cart_dtc()
    test_titannic()