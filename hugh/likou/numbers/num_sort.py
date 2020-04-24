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


if __name__ == '__main__':
    print(reversePairs2([7, 5, 6, 4]))