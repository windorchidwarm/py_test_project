#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : jump_game.py
# Author: chen
# Date  : 2020-04-17

from typing import List

def canJump(nums: List[int]) -> bool:
    if nums[0] == 0:
        if len(nums) == 1:
            return True
        else:
            return False
    if nums[0] >= len(nums):
        return True
    else:
        for i in range(nums[0] - 1, -1 , -1):
            print(i)
            if canJump(nums[i + 1:]):
                return True
    return False


def canJump2(nums: List[int]) -> bool:
    n, right = len(nums), 0
    for i in range(n):
        if i <= right:
            right = max(right, nums[i] + i)
            if right >= n - 1:
                return True
    return False


def jump(nums: List[int]) -> int:
    '''
    给定一个非负整数数组，你最初位于数组的第一个位置。
    数组中的每个元素代表你在该位置可以跳跃的最大长度。
    你的目标是使用最少的跳跃次数到达数组的最后一个位置。
    示例:
    输入: [2,3,1,1,4]
    输出: 2
    解释: 跳到最后一个位置的最小跳跃数是 2。
     从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
    暴力法 超出时间限制
    :param self:
    :param nums:
    :return:
    '''
    if not nums or len(nums) == 0: return 0
    nums_len = len(nums)
    dp = [nums_len] * nums_len

    dp[0] = 0
    for i in range(0, nums_len - 1):
        for j in range(1, nums[i] + 1):
            if i + j < nums_len:
                dp[i + j] = min(dp[i + j], dp[i] + 1)
    print(dp)
    return dp[-1]


def jump2(nums: List[int]) -> int:
    '''
    贪心算法
    :param nums:
    :return:
    '''
    nums_len = len(nums)
    end = 0
    max_position = 0
    steps = 0
    for i in range(0, nums_len - 1):
        max_position = max(max_position, nums[i] + i)
        if i == end:
            end = max_position
            steps += 1
    return steps


if __name__ == '__main__':
    print(canJump2([3, 2, 1, 0, 4]))
    print(canJump2([2, 3, 1, 1, 4]))
    print(canJump2([2,0,6,9,8,4,5,0,8,9,1,2,9,6,8,8,0,6,3,1,2,2,1,2,6,5,3,1,2,2,6,4,2,4,3,0,0,0,3,8,2,4,0,1,2,0,1,4,6,5,8,0,7,9,3,4,6,6,5,8,9,3,4,3,7,0,4,9,0,9,8,4,3,0,7,7,1,9,1,9,4,9,0,1,9,5,7,7,1,5,8,2,8,2,6,8,2,2,7,5,1,7,9,6]))
    print(jump2([2,3,1,1,4]))