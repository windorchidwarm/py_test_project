#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : Huisu.py
# Author: chen
# Date  : 2019-11-21

import copy
from typing import List

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def permuteOne(tmp, nums):
            if len(tmp) == len(nums):
                tmpList.append(copy.deepcopy(tmp))
            else:
                for i in range(len(nums)):
                    if nums[i] in tmp:
                        continue
                    tmp.append(nums[i])
                    permuteOne(tmp, nums)
                    del tmp[len(tmp) - 1]

        tmpList = []
        tmp = []
        permuteOne(tmp, nums)
        print(tmpList)
        return tmpList

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, size, depth, path, used, res):
            if depth == size:
                res.append(path.copy())
                return
            for i in range(size):
                if not used[i]:
                    if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                        continue
                    used[i] = True
                    path.append(nums[i])
                    dfs(nums, size, depth + 1, path, used, res)
                    used[i] = False
                    path.pop()
        size = len(nums)
        if size == 0: return []
        nums.sort()
        used = [False] * size
        res = []
        dfs(nums, size, 0, [], used, res)
        return res

if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    test = Solution()
    test.permute(nums)
    test.permuteUnique([1,1,2])
