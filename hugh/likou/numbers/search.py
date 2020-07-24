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


def searchRange(nums: List[int], target: int) -> List[int]:
    '''
    给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
    你的算法时间复杂度必须是 O(log n) 级别。
    如果数组中不存在目标值，返回 [-1, -1]。
    :param self:
    :param nums:
    :param target:
    :return:
    '''
    if len(nums) == 0: return [-1, -1]
    min_l = max_l = 0
    min_r = max_r = len(nums) - 1
    while min_l < min_r:
        min_mid = (min_l + min_r) // 2
        if nums[min_mid] == target:
            min_r = min_mid
        elif nums[min_mid] > target:
            min_r = min_mid
        else:
            min_l = min_mid + 1

    while max_l < max_r:
        max_mid = (max_l + max_r) // 2
        if nums[max_mid] == target:
            max_l = max_mid + 1
        elif nums[max_mid] > target:
            max_r = max_mid - 1
        else:
            max_l = max_mid + 1
    if min_r < 0 or nums[min_r] != target:
        return [-1, -1]
    if nums[max_l] > target:
        max_l -= 1
    return [min_r, max_l]


def firstMissingPositive(nums: List[int]) -> int:
    '''
    给你一个未排序的整数数组，请你找出其中没有出现的最小的正整数。
    输入: [1,2,0]
    输出: 3
    输入: [7,8,9,11,12]
    输出: 1
    :param nums:
    :return:
    '''
    n = len(nums)
    # 我们将数组中所有小于等于 00 的数修改为 N+1N+1
    for i in range(n):
        if nums[i] <= 0:
            nums[i] = n + 1

    # 我们遍历数组中的每一个数 xx，它可能已经被打了标记，因此原本对应的数为 |x|∣x∣，
    # 其中 |\,|∣∣ 为绝对值符号。如果 |x| \in [1, N]∣x∣∈[1,N]，
    # 那么我们给数组中的第 |x| - 1∣x∣−1 个位置的数添加一个负号。
    # 注意如果它已经有负号，不需要重复添加；
    for i in range(n):
        num = abs(nums[i])
        if num <= n:
            nums[num - 1] = - abs(nums[num - 1])

    # 在遍历完成之后，如果数组中的每一个数都是负数，那么答案是 N+1N+1，否则答案是第一个正数的位置加 11。
    for i in range(n):
        if nums[i] > 0:
            return i + 1
    return n + 1

def firstMissingPositive2(nums: List[int]) -> int:
    n = len(nums)
    for i in range(n):
        while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
            nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1
    return n + 1

if __name__ == '__main__':
    # print(search([3,1], 1))
    # print(searchInsert([1,3,5,6], 7))
    # print(minArray([3,1,1]))
    # print(searchRange([5,7,7,8,8,10], 7))
    print(firstMissingPositive([1]))