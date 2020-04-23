#!/usr/bin/env python
# -- coding: utf-8 --#
# @Time : 2020/4/23 9:50 
# @Author : Aries 
# @Site :  
# @File : num_combine.py 
# @Software: PyCharm


def waysToChange(n: int) -> int:
    '''
    硬币。给定数量不限的硬币，币值为25分、10分、5分和1分，编写代码计算n分有几种表示法。(结果可能会很大，你需要将结果模上1000000007)
    :param self:
    :param n:
    :return:
    '''
    def ways_to_change_max(nums, max_nums_index):
        '''

        :param nums:
        :param max_nums_index:
        :return:
        '''
        if nums == 0: return 1
        if max_nums_index >= len(combi): return 0
        if nums < combi[max_nums_index]:
            max_nums_index += 1
            return ways_to_change_max(nums, max_nums_index)
        elif max_nums_index == 3:
            return 1
        else:
            return ways_to_change_max(nums - combi[max_nums_index], max_nums_index) + ways_to_change_max(nums, max_nums_index + 1)
    combi = [25, 10, 5, 1]
    return ways_to_change_max(n, 0)

def waysToChange2(n: int) -> int:
    mod = 10 ** 9 + 7

    ans = 0
    for i in range(n // 25 + 1):
        rest = n - i * 25
        a, b = rest // 10, rest % 10 // 5
        ans += (a + 1) * (a + b + 1)
    return ans % mod

def waysToChange3(n: int) -> int:
    mod = 10 ** 9 + 7
    coins = [25, 10, 5, 1]

    f = [1] + [0] * n
    for coin in coins:
        for i in range(coin, n + 1):
            f[i] += f[i - coin]
    return f[n] % mod

if __name__ == '__main__':
    print(waysToChange3(10))