#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : num_sort.py
# Author: chen
# Date  : 2020-04-24

from typing import List
from hugh.likou.numbers.BIT import BIT
import bisect

def merge_sort(nums, tmp, l, r):
    if l >= r: return 0

    mid = (l + r) // 2
    inv_count = merge_sort(nums, tmp, l, mid) + merge_sort(nums, tmp, mid + 1, r)
    i, j, pos = l, mid + 1, l
    while i <= mid and j <= r:
        if nums[i] <= nums[j]:
            tmp[pos] = nums[i]
            i += 1
            inv_count += (j - (mid + 1))
        else:
            tmp[pos] = nums[j]
            j += 1
        pos += 1

    for k in range(i, mid + 1):
        tmp[pos] = nums[k]
        inv_count += (j - (mid + 1))
        pos += 1
    for k in range(j, r + 1):
        tmp[pos] = nums[k]
        pos += 1
    nums[l:r + 1] = tmp[l:r + 1]
    return inv_count


def reversePairs(nums: List[int]) -> int:
    '''
    逆序对
    :param nums:
    :return:
    '''
    n = len(nums)
    tmp = [0] * n
    return merge_sort(nums, tmp, 0, n - 1)


def reversePairs2(nums: List[int]) -> int:
    n = len(nums)
    # 离散化
    tmp = sorted(nums)
    for i in range(n):
        nums[i] = bisect.bisect_left(tmp, nums[i]) + 1
    # 树状数组统计逆序对
    bit = BIT(n)
    ans = 0
    for i in range(n - 1, -1, -1):
        ans += bit.query(nums[i] - 1)
        bit.update(nums[i])
    return ans



def swap(nums, i, j):
    tmp = nums[i]
    nums[i] = nums[j]
    nums[j] = tmp


def next_reverse(nums, start):
    i = start
    j = len(nums) - 1
    while i < j:
        swap(nums, i, j)
        i += 1
        j -= 1


def nextPermutation(nums: List[int]) -> None:
    '''
    实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。
    如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。
    必须原地修改，只允许使用额外常数空间。
    1,2,3 → 1,3,2
    3,2,1 → 1,2,3
    1,1,5 → 1,5,1
    :param self:
    :param nums:
    :return:
    '''
    i = len(nums) - 2
    while i >= 0 and nums[i + 1] <= nums[i]:
        i -= 1
    if i >= 0:
        j = len(nums) - 1
        while j >= 0 and nums[j] <= nums[i]:
            j -= 1
        swap(nums, i, j)
    print(i)
    next_reverse(nums, i + 1)



if __name__ == '__main__':
    print(reversePairs2([7, 5, 6, 4]))
    nums = [3, 2, 1]
    nums = [1, 2, 3]
    nextPermutation(nums)
    print(nums)