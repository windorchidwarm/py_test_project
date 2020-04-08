#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : three_number_closest.py
# Author: chen
# Date  : 2020-04-08

import math

def three_number_closest(nums, target):
    '''
    num数组 最接近target的三数之和
    :param nums:
    :param target:
    :return:
    '''
    nums.sort()
    n_len = len(nums)
    i = 0
    ans = nums[0] + nums[1] + nums[2]
    while i < n_len:
        if target == ans: break
        start = i + 1
        end = n_len - 1

        while start < end:
            result = nums[i] + nums[start] + nums[end]
            if math.fabs(result - target) < math.fabs(ans - target):
                ans = result

            if result - target <= 0:
                while start < end and nums[start] == nums[start + 1]:
                    start += 1
                start += 1
            else:
                while start < end and nums[end] == nums[end - 1]:
                    end -= 1
                end -= 1
        while i < n_len - 1 and nums[i] == nums[i + 1]:
            i += 1
        i += 1
    return ans


if __name__ == '__main__':
    target = 1
    nums = [-1, 2, 1, -4]
    data = three_number_closest(nums, target)
    print(data)