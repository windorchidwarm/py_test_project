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


def trap2(height: List[int]) -> int:
    '''
    给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
    输入: [0,1,0,2,1,0,1,3,2,1,2,1]
    输出: 6
    我们可以不用像方法 2 那样存储最大高度，而是用栈来跟踪可能储水的最长的条形块。使用栈就可以在一次遍历内完成计算。

    我们在遍历数组时维护一个栈。如果当前的条形块小于或等于栈顶的条形块，我们将条形块的索引入栈，意思是当前的条形块被栈中的前一个条形块界定。如果我们发现一个条形块长于栈顶，我们可以确定栈顶的条形块被当前条形块和栈的前一个条形块界定，因此我们可以弹出栈顶元素并且累加答案到 \text{ans}ans 。
    :param height:
    :return:
    '''
    if len(height) == 0:
        return 0
    water = 0
    height_lst = []
    current = 0
    while current < len(height):
        while len(height_lst) > 0 and height[current] > height[height_lst[-1]]:
            top = height_lst[-1]
            height_lst = height_lst[:-1]
            if len(height_lst) == 0:
                break
            distance = current - height_lst[-1] - 1
            bound_height = min(height[current], height[height_lst[-1]]) - height[top]
            water += distance * bound_height

        height_lst.append(current)
        current += 1
    return water

def corpFlightBookings(bookings: List[List[int]], n: int) -> List[int]:
    res = [0] * (n + 1)
    for i, j, k in bookings:
        res[i - 1] += k
        res[j] -= k
        print(res)
    for i in range(1, len(res)):
        res[i] += res[i - 1]
    return res[:-1]

if __name__ == '__main__':
    print(trap2([0,1,0,2,1,0,1,3,2,1,2,1]))
    print(trap2([0]))
    print(corpFlightBookings([[1,2,10],[2,3,20],[2,5,25]], 5))