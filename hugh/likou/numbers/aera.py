#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : aera.py
# Author: chen
# Date  : 2020-04-18

from typing import List

def maxArea(height: List[int]) -> int:
    first = 0
    last = len(height) - 1
    area = 0
    while first < last:
        area = max(area, min(height[first], height[last]) * (last - first))
        if height[first] < height[last]:
            first += 1
        else:
            last -= 1
    return area


def trap(height: List[int]) -> int:
    '''
    给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
    输入: [0,1,0,2,1,0,1,3,2,1,2,1]
    输出: 6
    :param height:
    :return:
    '''
    if len(height) == 0:
        return 0
    first = 0
    last = len(height) - 1
    water = 0
    while first < last and height[first] == 0:
        first += 1
    while first < last and height[last] == 0:
        last -= 1
    if first == last:
        return 0
    right = height[first]
    left = height[last]
    while first < last:
        if height[first] < height[last]:
            if right > height[first]:
                water += right - height[first]
            else:
                right = height[first]
            first += 1
        else:
            if height[last] < left:
                water += left - height[last]
            else:
                left = height[last]
            last -= 1
    return water


if __name__ == '__main__':
    print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))
    print(trap([0]))