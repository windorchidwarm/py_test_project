#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : Huisu.py
# Author: chen
# Date  : 2019-11-21

import copy

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

if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    test = Solution()
    test.permute(nums)
