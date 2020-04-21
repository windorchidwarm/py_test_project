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

def numberOfSubarrays(nums: List[int], k: int) -> int:
    '''
    给你一个整数数组 nums 和一个整数 k。
    如果某个 连续 子数组中恰好有 k 个奇数数字，我们就认为这个子数组是「优美子数组」。
    请返回这个数组中「优美子数组」的数目。
    输入：nums = [2,2,2,1,2,2,1,2,2,2], k = 2
    输出：16
    数学方式
    :param self:
    :param nums:
    :param k:
    :return:
    '''
    if len(nums) < k: return 0

    cnt = 0
    odd = [-1]
    for i in range(len(nums)):
        if nums[i] % 2 == 1:
            odd.append(i)
    odd.append(len(nums))
    if len(odd) < k: return 0
    for i in range(1, len(odd) - k):
        cnt += (odd[i] - odd[i - 1]) * (odd[i + k] - odd[i + k - 1])
    return cnt

def numberOfSubarrays2(nums: List[int], k: int) -> int:
    '''
    给你一个整数数组 nums 和一个整数 k。
    如果某个 连续 子数组中恰好有 k 个奇数数字，我们就认为这个子数组是「优美子数组」。
    请返回这个数组中「优美子数组」的数目。
    输入：nums = [2,2,2,1,2,2,1,2,2,2], k = 2
    输出：16
    前缀和+差分
    :param self:
    :param nums:
    :param k:
    :return:
    '''
    if len(nums) < k: return 0

    cnt = [0] * (len(nums) + 1)
    cnt[0] = 1
    odd, ans = 0, 0
    for i in range(len(nums)):
        if nums[i] % 2 == 1:
            odd += 1
        if odd >= k:
            ans += cnt[odd - k]
        cnt[odd] += 1
        print(cnt)
    return ans