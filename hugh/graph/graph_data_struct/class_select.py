#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : class_select.py
# Author: chen
# Date  : 2020-05-17


import collections
from typing import List

def findOrder(numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    '''
    选择numCourses课程
    :param numCourses:
    :param prerequisites:
    :return:
    '''
    # 存储有向图
    edges = collections.defaultdict(list)
    for info in prerequisites:
        edges[info[1]].append(info[0])
    # 标记每个节点的状态 0 未搜索 1 搜索中 2 已完成
    visited = [0] * numCourses
    # 数组模拟栈
    result = list()
    # 判断图中有无循环
    invalid = False

    def dfs(u:int):
        nonlocal invalid
        # 将节点标记为搜索中
        visited[u] = 1
        # 搜索相邻节点 只要有环 则停止搜索
        for v in edges[u]:
            # 如果未搜索 则搜索相邻节点
            if visited[v] == 0:
                dfs(v)
                if invalid:
                    return
            elif visited[v] == 1:
                # 如果搜索中 则找到了环
                invalid = True
                return
        visited[u] = 2
        result.append(u)
    for i in range(numCourses):
        if not invalid and not visited[i]:
            dfs(i)
    if invalid:
        return list()
    # 如果没有环，那么就有拓扑排序
    # 注意下标 0 为栈底，因此需要将数组反序输出
    return result[::-1]

def findOrder2(numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    # 存储有向图
    edges = collections.defaultdict(list)
    # 存储每个节点的入度
    indeg = [0] * numCourses
    # 存储答案
    result = list()

    for info in prerequisites:
        edges[info[1]].append(info[0])
        indeg[info[0]] += 1

    # 将所有入度为 0 的节点放入队列中
    q = collections.deque([u for u in range(numCourses) if indeg[u] == 0])

    while q:
        # 从队首取出一个节点
        u = q.popleft()
        # 放入答案中
        result.append(u)
        for v in edges[u]:
            indeg[v] -= 1
            # 如果相邻节点 v 的入度为 0，就可以选 v 对应的课程了
            if indeg[v] == 0:
                q.append(v)

    if len(result) != numCourses:
        result = list()
    return result


if __name__ == '__main__':
    findOrder(4, [[1,0],[2,0],[3,1],[3,2]])

