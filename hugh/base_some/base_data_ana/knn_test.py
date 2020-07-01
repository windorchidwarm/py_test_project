#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : knn_test.py
# Author: hugh
# Date  : 2020/7/1

from sklearn.neighbors import KNeighborsClassifier

from sklearn.datasets import load_digits
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt


def load_test_data():
    digits = load_digits()
    # print(digits)
    data = digits['data']
    target = digits['target']
    print(data.shape, target)
    print(data[0])
    print(digits['images'][0])

    # plt.gray()
    # plt.imshow(digits['images'][0])
    # plt.show()
    return data, target

def test_knn():
    data, target = load_test_data()

    # 分割数据，将25%的数据作为测试集，其余作为训练集（你也可以指定其他比例的数据作为训练集）
    train_x, test_x, train_y, test_y = train_test_split(data, target, test_size=0.25, random_state=33)
    # 采用Z-Score规范化
    ss = preprocessing.StandardScaler()
    train_ss_x = ss.fit_transform(train_x)
    test_ss_x = ss.transform(test_x)

    # 创建KNN分类器
    knn = KNeighborsClassifier()
    knn.fit(train_ss_x, train_y)
    predict_y = knn.predict(test_ss_x)
    print("KNN准确率: %.4lf" % accuracy_score(test_y, predict_y))



if __name__ == '__main__':
    '''
    knn K-Nearest Neighbor 
    1.计算待分类物体与其他物体之间的距离
    2.统计距离最近的K个邻居
    3.对于K个最近邻居，它们属于哪个分类最多，待分类物体就属于哪一类
    距离计算的方式：
    1.欧氏距离 d=√∑(xi-yi)2
    2.曼哈顿距离 d=∑|xi-yi| 点为(x1,x2,...)和(y1,y2,...)
    3.闵可夫斯基距离 d=(p√)∑(xi-yi)^p p√:开p次方 
    4.切比雪夫距离 p=∞时的距离 即max(|xi-yi|)
    5.余弦距离 计算的是两个向量的夹角，是在方向上计算两者之间的差异，对绝对数值不敏感
      用于角度关系比较重要的领域，比如搜索引擎搜索的关键词等
    
    KD树 K-Dimensional 
    KD 树是对数据点在 K 维空间中划分的一种数据结构。在 KD 树的构造中，每个节点都是 k 维数值点的二叉树。
    既然是二叉树，就可以采用二叉树的增删改查操作，这样就大大提升了搜索效率。
    
    KNeighborsClassifier(n_neighbors=5, weights=‘uniform’, algorithm=‘auto’, leaf_size=30)
    n_neighbors：即 KNN 中的 K 值，代表的是邻居的数量。K 值如果比较小，会造成过拟合。
    如果 K 值比较大，无法将未知物体分类出来。一般我们使用默认值 5
    weights：是用来确定邻居的权重，有三种方式：
    weights=uniform，代表所有邻居的权重相同；
    weights=distance，代表权重是距离的倒数，即与距离成反比；
    自定义函数，你可以自定义不同距离所对应的权重。大部分情况下不需要自己定义函数。
    algorithm：用来规定计算邻居的方法，它有四种方式：
    algorithm=auto，根据数据的情况自动选择适合的算法，默认情况选择 auto；
    algorithm=kd_tree，也叫作 KD 树，是多维空间的数据结构，方便对关键数据进行检索，
    不过 KD 树适用于维度少的情况，一般维数不超过 20，如果维数大于 20 之后，效率反而会下降；
    algorithm=ball_tree，也叫作球树，它和 KD 树一样都是多维空间的数据结果，
    不同于 KD 树，球树更适用于维度大的情况；
    algorithm=brute，也叫作暴力搜索，它和 KD 树不同的地方是在于采用的是线性扫描，
    而不是通过构造树结构进行快速检索。当训练集大的时候，效率很低。
    leaf_size：代表构造 KD 树或球树时的叶子数，默认是 30，调整 leaf_size 会影响到树的构造和搜索速度。
    '''
    test_knn()