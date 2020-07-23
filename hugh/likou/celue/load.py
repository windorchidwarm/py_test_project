#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : load.py
# Author: hugh
# Date  : 2020/7/23

from typing import List

def minPathSum(grid: List[List[int]]) -> int:
    '''
    给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
    :param grid:
    :return:
    '''
    m = len(grid)
    if m == 0: return 0
    n = len(grid[0])
    if n == 0: return 0
    route = [0 for i in range(n)]
    route[0] = grid[0][0]
    for j in range(1, n):
        route[j] = grid[0][j] + route[j - 1]

    for i in range(1, m):
        for j in range(n):
            route[j] = min(grid[i][j] + route[j], grid[i][j] + route[j - 1]) if j > 0 else grid[i][j] + route[j]
    return route[-1]


if __name__ == '__main__':
    '''
    '''
    data = [
      [1,3,1],
      [1,5,1],
      [4,2,1]
    ]
    print(minPathSum(data))