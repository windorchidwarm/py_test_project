#!/usr/bin/env python
# -- coding: utf-8 --#
# @Time : 2020/4/14 13:01 
# @Author : Aries 
# @Site :  
# @File : numbers.py 
# @Software: PyCharm

'''
一些数字相关的算法
'''

from typing import List

def merge(intervals: List[List[int]]) -> List[List[int]]:
    '''
    给出一个区间的集合，请合并所有重叠的区间。
    示例 1:
    输入: [[1,3],[2,6],[8,10],[15,18]]
    输出: [[1,6],[8,10],[15,18]]
    解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
    :param self:
    :param intervals:
    :return:
    '''
    intervals.sort(key=lambda x: x[0])
    merged = []
    for interval in intervals:
        # 如果列表为空，或者当前区间与上一区间不重合，直接添加
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            # 否则的话，我们就可以与上一区间进行合并
            merged[-1][1] = max(merged[-1][1], interval[1])

    return merged

def numberOfSubarrays(nums: List[int], k: int) -> int:
    '''
    给你一个整数数组 nums 和一个整数 k。
    如果某个 连续 子数组中恰好有 k 个奇数数字，我们就认为这个子数组是「优美子数组」。
    请返回这个数组中「优美子数组」的数目。
    输入：nums = [2,2,2,1,2,2,1,2,2,2], k = 2
    输出：16
    数学方式
    :param self:
    :param nums:
    :param k:
    :return:
    '''
    if len(nums) < k: return 0

    cnt = 0
    odd = [-1]
    for i in range(len(nums)):
        if nums[i] % 2 == 1:
            odd.append(i)
    odd.append(len(nums))
    if len(odd) < k: return 0
    for i in range(1, len(odd) - k):
        cnt += (odd[i] - odd[i - 1]) * (odd[i + k] - odd[i + k - 1])
    return cnt

def numberOfSubarrays2(nums: List[int], k: int) -> int:
    '''
    给你一个整数数组 nums 和一个整数 k。
    如果某个 连续 子数组中恰好有 k 个奇数数字，我们就认为这个子数组是「优美子数组」。
    请返回这个数组中「优美子数组」的数目。
    输入：nums = [2,2,2,1,2,2,1,2,2,2], k = 2
    输出：16
    前缀和+差分
    :param self:
    :param nums:
    :param k:
    :return:
    '''
    if len(nums) < k: return 0

    cnt = [0] * (len(nums) + 1)
    cnt[0] = 1
    odd, ans = 0, 0
    for i in range(len(nums)):
        if nums[i] % 2 == 1:
            odd += 1
        if odd >= k:
            ans += cnt[odd - k]
        cnt[odd] += 1
        print(cnt)
    return ans

def maxSubArray(nums: List[int]) -> int:
    '''
    给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
    示例:
    输入: [-2,1,-3,4,-1,2,1,-5,4],
    输出: 6
    解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。\
    动态规划
    :param self:
    :param nums:
    :return:
    '''
    if not nums or len(nums) < 1: return 0

    dp = [0] * len(nums)
    dp[0] = nums[0]
    result = dp[0]
    for i in range(1, len(nums)):
        dp[i] = max(dp[i - 1] + nums[i], nums[i])
        result = max(result, dp[i])
    return result

def maxSubArray2(nums: List[int]) -> int:
    '''
    给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
    示例:
    输入: [-2,1,-3,4,-1,2,1,-5,4],
    输出: 6
    解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。\
    贪心算法
    :param self:
    :param nums:
    :return:
    '''
    if not nums or len(nums) < 1: return 0

    result = nums[0]
    sum = 0
    for i in range(0, len(nums)):
        sum += nums[i]
        result = max(result, sum)
        if sum < 0: sum = 0
    return result


def maxSubArray3(nums: List[int]) -> int:
    '''
    给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
    示例:
    输入: [-2,1,-3,4,-1,2,1,-5,4],
    输出: 6
    解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。\
    分治算法
    :param self:
    :param nums:
    :return:
    '''
    def get(nums, l, r):
        if l == r: return nums[l],nums[l],nums[l],nums[l]

        mid = int((l + r) / 2)
        l_sum_l, r_sum_l, m_sum_l, i_sum_l = get(nums, l, mid)
        l_sum_r, r_sum_r, m_sum_r, i_sum_r = get(nums, mid + 1, r)
        return max(l_sum_l, i_sum_l + l_sum_r),max(r_sum_r, i_sum_r + r_sum_l),max(m_sum_l, m_sum_r, r_sum_l + l_sum_r),(i_sum_l + i_sum_r)
    if not nums or len(nums) < 1: return 0

    l_sum, r_sum, m_sum, i_sum = get(nums, 0, len(nums) - 1)
    return m_sum


def add_two_nums(nums1:List[int], nums2:List[int]) -> List[int]:
    '''

    :param nums1:
    :param nums2:
    :return:
    '''
    def get_a_sign(a):
        if a > 9:
            return a % 10, 1
        else:
            return a, 0
    if not nums1: return nums2
    if not nums2: return nums1

    i = 1
    sign = 0
    lst = []
    while i <= len(nums1) and i <= len(nums2):
        a = sign + nums1[-i] + nums2[-i]
        a, sign = get_a_sign(a)
        lst.append(a)
        i += 1
    while i <= len(nums1):
        a = sign + nums1[-i]
        a, sign = get_a_sign(a)
        lst.append(a)
        i += 1
    while i <= len(nums2):
        a = sign + nums2[-i]
        a, sign = get_a_sign(a)
        lst.append(a)
        i += 1

    if sign == 1:
        lst.append(1)
    lst.reverse()
    return lst

def myPow(x: float, n: int) -> float:
    def quick_muk_N(N):
        if N == 0: return 1.0
        y = quick_muk_N(N // 2)
        return y * y if N % 2 == 0 else y * y * x

    if x == 0: return 0
    return quick_muk_N(n) if n > 0 else 1.0 / quick_muk_N(-n)

def myPow2(x: float, n: int) -> float:
    '''
    时间复杂度：O(\log n)O(logn)，即为对 nn 进行二进制拆分的时间复杂度。
    :param x:
    :param n:
    :return:
    '''
    def quick_muk_N(N):

        ans = 1.0
        x_contribute  = x
        while N > 0:
            if N % 2 == 1:
                ans *= x_contribute
            x_contribute *= x_contribute
            # 舍弃 N 二进制表示的最低位，这样我们每次只要判断最低位即可
            N //= 2
        return ans

    if x == 0: return 0
    return quick_muk_N(n) if n > 0 else 1.0 / quick_muk_N(-n)



if __name__ == '__main__':
    print(maxSubArray3([-2,1,-3,4,-1,2,1,-5,4]))