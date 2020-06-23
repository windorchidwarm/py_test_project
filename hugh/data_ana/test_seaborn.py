#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : test_seaborn.py
# Author: hugh
# Date  : 2020/6/23


import seaborn as sns
import matplotlib.pyplot as plt

import numpy as np
import pandas as pd

def get_data_n(N=1000):
    return np.random.rand(N)

def get_data_metris(*args):
    data = np.random.normal(size=(args))
    return data

def get_pd(**kwargs):
    df = pd.DataFrame()
    for key in kwargs:
        df[key] = kwargs[key]
    return df


def get_series(x):
    return pd.Series(x)


# 散点图
def show_scatter(x, y, data = None, label = 'label'):
    sns.jointplot(x = x, y = y , data = data, kind = 'scatter', color='green')
    plt.show()

# 折线图
def show_plot(x, y, data = None, label = 'label'):
    sns.lineplot(x = x, y = y, data = data)
    plt.legend(loc='upper right')
    plt.show()

# 直方图
def show_displots(s):
    sns.distplot(s, kde=False)
    plt.show()
    sns.distplot(s, kde=True)
    plt.show()

# 条形图
def show_barplot(x, y, data):
    sns.barplot(x=x, y=y, data=data)
    plt.show()

# 箱型图
def show_box(data):
    sns.boxplot(data = data)
    plt.show()

# 热力图
def show_heatmap(data):
    sns.heatmap(data)
    plt.show()

# 二元变量分布
def show_two():
    # 数据准备
    x, y = get_data_n(), get_data_n()
    df = get_pd(x = x, y = y)
    # 用Seaborn画二元变量分布图（散点图，核密度图，Hexbin图）
    sns.jointplot(x="x", y="y", data=df, kind='scatter')
    sns.jointplot(x="x", y="y", data=df, kind='kde')
    sns.jointplot(x="x", y="y", data=df, kind='hex')
    plt.show()


# 成对关系
def show_two_cominb():
    x, y, z = get_data_n(), get_data_n(), get_data_n()
    df = get_pd(x=x, y=y, z=x)
    sns.pairplot(df)
    plt.show()

if __name__ == '__main__':
    '''
    '''
    # x, y = get_data_n(), get_data_n()
    # df = get_pd(x = x, y = y)
    # show_scatter('x', 'y', data=df)

    # x = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
    # y = [5, 3, 6, 20, 17, 16, 19, 30, 32, 35]
    # df = get_pd(x = x, y = y)
    # show_plot('x', 'y', data=df)

    # x = get_data_n(100)
    # s = get_series(x)
    # show_displots(s)

    # x = ['Cat1', 'Cat2', 'Cat3', 'Cat4', 'Cat5']
    # y = [5, 4, 8, 12, 7]
    # df = get_pd(x=x, y=y)
    # show_barplot('x', 'y', data=df)

    # data = get_data_metris(10, 4)
    # lables = ['A', 'B', 'C', 'D']
    # df = pd.DataFrame(data, columns=lables)
    # show_box(df)

    # 内置的flights数据
    # flights = sns.load_dataset('flights')
    # print(flights)
    # data = flights.pivot('year', 'month', 'passengers')
    # print(data)
    # show_heatmap(data)

    # show_two()

    show_two_cominb()