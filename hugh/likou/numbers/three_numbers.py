#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : three_numbers.py
# Author: chen
# Date  : 2020-04-07


def three_sum(nums):
    '''
    三数之和为0
    :param nums:
    :return:
    超时
    '''
    lst = []
    n_len = len(nums)
    for i in range(n_len):
        for j in range(i + 1, n_len):
            if j + 1 < n_len and (0 - nums[i] - nums[j]) in nums[j + 1:]:
                n_data = []
                n_data.append(nums[i])
                n_data.append(nums[j])
                n_data.append(0 - nums[i] - nums[j])
                n_data.sort()
                if n_data not in lst:
                    lst.append(n_data)
    return lst


def three_num2(nums):
    '''
    三数之和为0
    :param nums:
    :return:
    先排序
    然后首尾同号则肯定大于0
    处理相同的数字
    左边正数也肯定大于0
    '''
    nums.sort()
    n_len = len(nums)
    lst = []
    i = 0
    while i < n_len:
        if nums[i] > 0: break # 左边正数 则退出
        first = i + 1
        last = n_len - 1
        while first < last:
            if first >= last or nums[i] * nums[last] > 0: break
            result = nums[i] + nums[first] + nums[last]
            if result == 0:
                lst.append([nums[i], nums[first], nums[last]])
            if result <= 0:
                while first < last and nums[first] == nums[first + 1]:
                    first += 1
                first += 1
            else:
                while first < last and nums[last] == nums[last - 1]:
                    last -= 1
                last -= 1
        while nums[i] == nums[i+1]: i +=1
        i += 1
        print(i)
    return lst


if __name__ == '__main__':
    print('xxxx')
    nums = [-1, 0, 1, 2, -1, -4]
    print(three_num2(nums))