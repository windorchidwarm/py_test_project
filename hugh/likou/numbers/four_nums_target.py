#!/usr/bin/env python
# -- coding: utf-8 --#
# @Time : 2020/4/14 10:55 
# @Author : Aries 
# @Site :  
# @File : four_nums_target.py 
# @Software: PyCharm

from typing import List

def four_nums_target(nums: List[int], target: int) -> List[List[int]]:
    '''
    给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/4sum
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
    :param nums:
    :param target:
    :return:
    '''
    n = len(nums)
    if n < 4:
        return []

    nums.sort()

    lst = []
    i = 0
    while i < n - 3:
        if nums[i] * 4 > target: break
        i_target = target - nums[i]
        j = i + 1
        while j < n - 2:
            if nums[j] * 3 > i_target: break
            first = j + 1
            last = n - 1
            while first < last:
                if first >= last  or nums[last] * 4 < target: break
                result = nums[j] + nums[first] + nums[last]
                if result == i_target:
                    lst.append([nums[i], nums[j], nums[first], nums[last]])
                if result <= i_target:
                    while first < last and nums[first] == nums[first + 1]:
                        first += 1
                    first += 1
                else:
                    while first < last and nums[last] == nums[last - 1]:
                        last -= 1
                    last -= 1
            while nums[j] == nums[j + 1] and j < n - 2: j += 1
            j += 1
        while nums[i] == nums[i + 1] and i < n - 3: i += 1
        i += 1
    return lst


def n_sum(nums, target, n):
    def dfs(pos: int, cur: List[int], n: int, target: int):
        if n == 2:
            j = pos
            k = len(nums) - 1
            while j < k:
                sum = nums[j] + nums[k]
                if sum < target:
                    j += 1
                elif sum > target:
                    k -= 1
                else:
                    solution = cur[:] + [nums[j], nums[k]]
                    ans.append(solution)
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                    j += 1
                    k -= 1
            return
        i = pos
        while i < len(nums) - n + 1:
            # 剪枝的一种情况
            if nums[i] * n > target or nums[-1] * n < target:
                break
            # 排除重复数字
            if i > pos and nums[i] == nums[i - 1]:
                i += 1
                continue
            cur.append(nums[i])
            dfs(i + 1, cur, n - 1, target - nums[i])  # 回溯
            cur.pop()
            i += 1

    ans = []
    nums.sort()
    dfs(0, [], n, target)
    return ans


if __name__ == '__main__':
    nums =  [1,-2,-5,-4,-3,3,3,5]
    target = -11
    l = four_nums_target(nums, target)
    print(l)
    ll = n_sum(nums, target, 4)
    print(ll)