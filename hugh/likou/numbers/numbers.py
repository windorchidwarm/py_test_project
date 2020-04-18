#!/usr/bin/env python
# -- coding: utf-8 --#
# @Time : 2020/4/14 13:01 
# @Author : Aries 
# @Site :  
# @File : numbers.py 
# @Software: PyCharm

'''
一些数字相关的算法
'''

from typing import List

def merge(intervals: List[List[int]]) -> List[List[int]]:
    '''
    给出一个区间的集合，请合并所有重叠的区间。
    示例 1:
    输入: [[1,3],[2,6],[8,10],[15,18]]
    输出: [[1,6],[8,10],[15,18]]
    解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
    :param self:
    :param intervals:
    :return:
    '''
    intervals.sort(key=lambda x: x[0])
    merged = []
    for interval in intervals:
        # 如果列表为空，或者当前区间与上一区间不重合，直接添加
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            # 否则的话，我们就可以与上一区间进行合并
            merged[-1][1] = max(merged[-1][1], interval[1])

    return merged


