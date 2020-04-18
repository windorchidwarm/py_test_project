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

if __name__ == '__main__':
    print(canJump2([3, 2, 1, 0, 4]))
    print(canJump2([2, 3, 1, 1, 4]))
    print(canJump2([2,0,6,9,8,4,5,0,8,9,1,2,9,6,8,8,0,6,3,1,2,2,1,2,6,5,3,1,2,2,6,4,2,4,3,0,0,0,3,8,2,4,0,1,2,0,1,4,6,5,8,0,7,9,3,4,6,6,5,8,9,3,4,3,7,0,4,9,0,9,8,4,3,0,7,7,1,9,1,9,4,9,0,1,9,5,7,7,1,5,8,2,8,2,6,8,2,2,7,5,1,7,9,6]))