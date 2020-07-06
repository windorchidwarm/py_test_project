#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : pagerank_test.py
# Author: hugh
# Date  : 2020/7/6


import networkx as nx

import os

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict


base_path = os.path.dirname(os.path.realpath(__file__))\
    .replace(os.path.join('hugh', os.path.join('base_some', 'base_data_ana')), '')
print(base_path)
file_dir = os.path.join(os.path.join(base_path, 'files'),'pagerank')


def test_pagerank_emails():
    '''

    :return:
    '''
    emails = pd.read_csv(os.path.join(file_dir, 'Emails.csv'))

    # 读取别名文件
    file = pd.read_csv(os.path.join(file_dir, 'Aliases.csv'))
    aliases = {}
    for index, row in file.iterrows():
        aliases[row['Alias']]  = row['PersonId']
    # 读取人名文件
    file = pd.read_csv(os.path.join(file_dir, 'Persons.csv'))
    persons = {}
    for index, row in file.iterrows():
        persons[row['Id']] = row['Name']
    # 针对别名进行转换
    def unify_name(name):
        # 姓名统一小写
        name = str(name).lower()
        # 去掉, 和 @后面的内容
        name = name.replace(",","").split("@")[0]
        # 别名转换
        if name in aliases.keys():
            return persons[aliases[name]]
        return name

    def show_graph(graph, layout='spring_layout'):
        # 使用 Spring Layout 布局，类似中心放射状
        if layout == 'circular_layout':
            positions = nx.circular_layout(graph)
        else:
            positions = nx.spring_layout(graph)
        # 设置网络图中的节点大小，大小与 pagerank 值相关，因为 pagerank 值很小所以需要 *20000
        nodesize = [x['pagerank']*20000 for v,x in graph.nodes(data=True)]
        # 设置网络图中的边长度
        edgesize = [np.sqrt(e[2]['weight']) for e in graph.edges(data=True)]
        # 绘制节点
        nx.draw_networkx_nodes(graph, positions, node_size=nodesize, alpha=0.4)
        # 绘制边
        nx.draw_networkx_edges(graph, positions, edge_size=edgesize, alpha=0.2)
        # 绘制节点的 label
        nx.draw_networkx_labels(graph, positions, font_size=10)
        # 输出希拉里邮件中的所有人物关系图
        plt.show()
    # 将寄件人和收件人的姓名进行规范化
    emails.MetadataFrom = emails.MetadataFrom.apply(unify_name)
    emails.MetadataTo = emails.MetadataTo.apply(unify_name)
    # 设置遍的权重等于发邮件的次数
    edges_weights_temp = defaultdict(list)
    for row in zip(emails.MetadataFrom, emails.MetadataTo, emails.RawText):
        temp = (row[0], row[1])
        if temp not in edges_weights_temp:
            edges_weights_temp[temp] = 1
        else:
            edges_weights_temp[temp] = edges_weights_temp[temp] + 1
    # 转化格式 (from, to), weight => from, to, weight
    edges_weights = [(key[0], key[1], val) for key, val in edges_weights_temp.items()]
    # 创建一个有向图
    graph = nx.DiGraph()
    # 设置有向图中的路径及权重 (from, to, weight)
    graph.add_weighted_edges_from(edges_weights)
    # 计算每个节点（人）的 PR 值，并作为节点的 pagerank 属性
    pagerank = nx.pagerank(graph)
    # 将 pagerank 数值作为节点的属性
    nx.set_node_attributes(graph, name='pagerank', values=pagerank)
    # 画网络图
    show_graph(graph)

    # 将完整的图谱进行精简
    # 设置 PR 值的阈值，筛选大于阈值的重要核心节点
    pagerank_threshold = 0.005
    # 复制一份计算好的网络图
    small_graph = graph.copy()
    # 剪掉 PR 值小于 pagerank_threshold 的节点
    for n, p_rank in graph.nodes(data=True):
        if p_rank['pagerank'] < pagerank_threshold:
            small_graph.remove_node(n)
    # 画网络图,采用circular_layout布局让筛选出来的点组成一个圆
    show_graph(small_graph, 'circular_layout')

def test_pagerank():
    '''

    :return:
    '''
    G = nx.DiGraph()
    # 有向图之间边的关系
    edges = [("A", "B"), ("A", "C"), ("A", "D"), ("B", "A"), ("B", "D"), ("C", "A"), ("D", "B"), ("D", "C")]
    for edge in edges:
        G.add_edge(edge[0], edge[1])
    pagerank_list = nx.pagerank(G, alpha=1)
    print(pagerank_list)



if __name__ == '__main__':
    '''
    PageRank算法
    一个网页的影响力 = 所有入链集合的页面的加权影响力之和
    PR(u)=∑[PR(v)/L(v)]
    u 为待评估的页面，Bu​ 为页面 u 的入链集合。针对入链集合中的任意页面 v，
    它能给 u 带来的影响力是其自身的影响力 PR(v) 除以 v 页面的出链数量，
    即页面 v 把影响力 PR(v) 平均分配给了它的出链，这样统计所有能给 u 带来链接的页面 v，
    得到的总和就是网页 u 的影响力，即为 PR(u)。
    
    矩阵乘法：转义矩阵*权重矩阵
    们再用转移矩阵乘以 w1​ 得到 w2​ 结果，直到第 n 次迭代后 wn​ 影响力不再发生变化，
    可以收敛到 (0.3333，0.2222，0.2222，0.2222），也就是对应着 A、B、C、D 四个页面最终平衡状态下的影响力。
    问题：等级泄露（没有出链） 等级沉没(没有入链)
    
    PageRank 的随机浏览模型
    定义了阻尼因子 d，这个因子代表了用户按照跳转链接来上网的概率，通常可以取一个固定值 0.85，
    而 1-d=0.15 则代表了用户不是通过跳转链接的方式来访问网页的
    PR(u)=(1-d)/N + d∑[PR(v)/L(v)]
    一定程度上解决了等级泄露和等级沉没的问题。
    
    1. 关于图的创建
    图可以分为无向图和有向图，在 NetworkX 中分别采用不同的函数进行创建。
    无向图指的是不用节点之间的边的方向，使用 nx.Graph() 进行创建；
    有向图指的是节点之间的边是有方向的，使用 nx.DiGraph() 来创建。
    在上面这个例子中，存在 A→D 的边，但不存在 D→A 的边。
    2. 关于节点的增加、删除和查询
    如果想在网络中增加节点，可以使用 G.add_node(‘A’) 添加一个节点，也可以使用 G.add_nodes_from([‘B’,‘C’,‘D’,‘E’]) 添加节点集合。
    如果想要删除节点，可以使用 G.remove_node(node) 删除一个指定的节点，也可以使用 G.remove_nodes_from([‘B’,‘C’,‘D’,‘E’]) 删除集合中的节点。
    那么该如何查询节点呢？如果你想要得到图中所有的节点，就可以使用 G.nodes()，也可以用 G.number_of_nodes() 得到图中节点的个数。
    3. 关于边的增加、删除、查询
    增加边与添加节点的方式相同，使用 G.add_edge(“A”, “B”) 添加指定的“从 A 到 B”的边，也可以使用 add_edges_from 函数从边集合中添加。
    我们也可以做一个加权图，也就是说边是带有权重的，使用 add_weighted_edges_from 函数从带有权重的边的集合中添加。
    在这个函数的参数中接收的是 1 个或多个三元组[u,v,w]作为参数，u、v、w 分别代表起点、终点和权重。
    另外，我们可以使用 remove_edge 函数和 remove_edges_from 函数删除指定边和从边集合中删除。
    另外可以使用 edges() 函数访问图中所有的边，使用 number_of_edges() 函数得到图中边的个数。
    '''
    # test_pagerank()
    test_pagerank_emails()