#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : test_plot.py
# Author: hugh
# Date  : 2020/6/23

import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

import numpy as np

def get_data_n(N=1000):
    data = np.random.rand(N)
    return data


def get_data_metris(*args):
    data = np.random.normal(size=(args))
    return data

# 散点图
def show_scatter(x, y, marker='x'):
    '''
    marker 标记的符合 可选为 x > o
    :param x:
    :param y:
    :param marker:
    :return:
    '''
    plt.scatter(x, y, marker=marker)
    plt.show()

# 折线图
def show_plot(x, y):
    plt.plot(x, y)
    plt.show()

# 直方图
def show_hist(x):
    plt.hist(x)
    plt.show()


# 条形图
def show_bar(x, y):
    plt.bar(x, y)
    plt.show()


# 箱型图
def show_box(data, lables):
    plt.boxplot(data, labels = lables)
    plt.show()

# 饼图
def show_pie(x, labels):
    # wedgeprops width 设置饼图半径 小于1时显示为环形
    plt.pie(x = x, labels = labels, wedgeprops={'width': 0.4})
    plt.show()


# 蜘蛛图
def show_spider_data(stats, labels):
    '''

    :return:
    '''
    # 画图数据准备，角度、状态值
    angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False)
    stats = np.concatenate((stats, [stats[0]]))
    angles = np.concatenate((angles, [angles[0]]))  # 用Matplotlib画蜘蛛图
    fig = plt.figure()
    ax = fig.add_subplot(111, polar=True)
    ax.plot(angles, stats, 'o-', linewidth=2)
    ax.fill(angles, stats, alpha=0.25)  # 设置中文字体
    font = FontProperties(fname=r"C:\Windows\Fonts\simhei.ttf", size=14)
    ax.set_thetagrids(angles * 180 / np.pi, labels, FontProperties=font)
    plt.show()


if __name__ == '__main__':
    '''
    '''
    # x, y = get_data_n(), get_data_n()
    # show_scatter(x, y, 'o')

    # x = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
    # y = [5, 3, 6, 20, 17, 16, 19, 30, 32, 35]
    # show_plot(x, y)

    # x = get_data_n(100)
    # show_hist(x)

    # x = ['Cat1', 'Cat2', 'Cat3', 'Cat4', 'Cat5']
    # y = [5, 4, 8, 12, 7]
    # show_bar(x, y)

    # data = get_data_metris(10, 4)
    # lables = ['A','B','C','D']
    # show_box(data, lables)

    # nums = [25, 37, 33, 37, 6]
    # labels = ['High-school', 'Bachelor', 'Master', 'Ph.d', 'Others']  # 用Matplotlib画饼图
    # show_pie(nums, labels)

    labels = np.array([u"推进", "KDA", u"生存", u"团战", u"发育", u"输出"])
    stats = [83, 61, 95, 67, 76, 88]

    show_spider_data(stats, labels)
