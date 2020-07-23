#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : comb.py
# Author: hugh
# Date  : 2020/7/23

from typing import List

def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    '''
    给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
    :param self:
    :param candidates:
    :param target:
    :return:
    '''
    def combine(candidates, max_num, conset, target):
        if target == 0:
            ans.append(conset.copy())
            return
        elif target < 0:
            return
        for i in range(max_num, -1, -1):
            if candidates[i] > target:
                continue
            else:
                conset.append(candidates[i])
                combine(candidates, i, conset, target - candidates[i])
                del conset[-1]
    if len(candidates) == 0: return []
    ans = []
    combine(candidates, len(candidates) - 1, [], target)
    ans.reverse()
    return ans

def combinationSum_2(candidates: List[int], target: int) -> List[List[int]]:
    '''
    用背包问题解
    :param candidates:
    :param target:
    :return:
    '''
    dp = [[[]] if j == 0 else [] for j in range(target + 1)]
    for candidate in candidates:
        for i in range(candidate, target + 1):
            print(dp)
            dp[i] += [res + [candidate] for res in dp[i - candidate]]
    return dp[-1]

def combinationSum2(candidates: List[int], target: int) -> List[List[int]]:
    '''
    给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
    candidates 中的每个数字在每个组合中只能使用一次。
    :param candidates:
    :param target:
    :return:
    '''
    dp = [[[]] if j == 0 else [] for j in range(target + 1)]
    candidates.sort()
    for candidate in candidates:
        for i in range(target, candidate - 1, -1):
            print(dp)
            for res in dp[i - candidate]:
                ret = res + [candidate]
                if ret not in dp[i]:
                    dp[i].append(ret)
            # dp[i] += [res + [candidate] for res in dp[i - candidate]]
    ans = dp[-1]
    ans.sort()
    return ans

if __name__ == '__main__':
    '''
    '''
    # print(combinationSum_2([2,3,6,7], 7))
    print(combinationSum2([2,5,2,1,2], 5))