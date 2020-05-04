#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : search.py
# Author: chen
# Date  : 2020-05-04

from typing import List

def search(nums: List[int], target: int) -> int:
    '''
    假设按照升序排序的数组在预先未知的某个点上进行了旋转。
    ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
    搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。
    你可以假设数组中不存在重复的元素。
    你的算法时间复杂度必须是 O(log n) 级别。
    示例 1:
    输入: nums = [4,5,6,7,0,1,2], target = 0
    输出: 4
    :param nums:
    :param target:
    :return:
    '''
    if not nums: return -1
    if len(nums) == 1:
        if nums[0] == target:
            return 0
        else:
            return -1

    l, r = 0, len(nums) - 1

    while l <= r:

        mid = (r + l) // 2
        print(r, l, mid)
        if target == nums[mid]: return mid
        if nums[l] <= nums[mid]:
            if nums[l] <= target and target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        else:
            if nums[r] >= target and target > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
        print(r, l, mid)
    return -1


if __name__ == '__main__':
    print(search([3,1], 1))
