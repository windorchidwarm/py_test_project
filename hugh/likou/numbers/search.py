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

def searchInsert(nums: List[int], target: int) -> int:
    if len(nums) == 0:
        nums.append(target)
        return 0

    if target < nums[0]:
        nums.insert(0, target)
        return 0

    if target > nums[-1]:
        nums.append(target)
        return len(nums) - 1

    if target == nums[0]:
        return 0

    if target == nums[-1]:
        return len(nums) - 1

    l, r = 0, len(nums) - 1

    while l + 1 < r:
        mid = (l + r) // 2
        if nums[mid] == target:
            return mid
        elif target > nums[mid]:
            l = mid
        else:
            r = mid

    nums.insert(l + 1, target)
    return l + 1


def minArray(numbers: List[int]) -> int:
    '''
    把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输入一个递增排序的数组的一个旋转，
    输出旋转数组的最小元素。例如，数组 [3,4,5,1,2] 为 [1,2,3,4,5] 的一个旋转，该数组的最小值为1。
    :param numbers:
    :return:
    '''
    if len(numbers) == 0: return
    if len(numbers) == 1: return numbers[0]
    l = 0
    r = len(numbers) - 1
    if numbers[0] < numbers[-1]:
        return numbers[0]
    while l < r:
        mid = (l + r) // 2
        if numbers[l] > numbers[mid]:
            r = mid
        elif numbers[mid] > numbers[r]:
            l = mid + 1
        else:
            r -= 1
    return numbers[r]



if __name__ == '__main__':
    # print(search([3,1], 1))
    # print(searchInsert([1,3,5,6], 7))
    print(minArray([3,1,1]))
