#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : divide.py
# Author: chen
# Date  : 2020-04-26

import math

def divide(dividend: int, divisor: int) -> int:
    '''

    :param self:
    :param dividend:
    :param divisor:
    :return:
    '''
    def div(divid, divsor):
        if divid < divsor:
            return 0
        count = 1
        d_sor = divsor
        while d_sor + d_sor < divid:
            count += count
            d_sor += d_sor
        return count + div(divid - d_sor, divsor)
    if divisor == 0: return None
    if dividend == 0: return 0
    if divisor == 1: return dividend

    sign = 1
    if (divisor > 0 and dividend < 0) or (divisor < 0 and dividend > 0):
        sign = -1
    divisor = divisor if divisor > 0 else -divisor
    dividend = dividend if dividend > 0 else -dividend

    min_data = -2 ** 31
    if divisor == -1:
        if dividend > min_data:
            return -dividend
        else:
            return 2 ** 31 - 1
    res = div(dividend, divisor)
    if sign == -1:
        res = -res
    if res > 2 ** 31 - 1:
        res = 2 ** 31 - 1
    if res < -2 ** 31:
        res = -2 ** 31
    return res

def divisorGame(N: int) -> bool:
    '''
    爱丽丝和鲍勃一起玩游戏，他们轮流行动。爱丽丝先手开局。
    最初，黑板上有一个数字 N 。在每个玩家的回合，玩家需要执行以下操作：
    选出任一 x，满足 0 < x < N 且 N % x == 0 。
    用 N - x 替换黑板上的数字 N 。
    如果玩家无法执行这些操作，就会输掉游戏。
    只有在爱丽丝在游戏中取得胜利时才返回 True，否则返回 false。假设两个玩家都以最佳状态参与游戏。

    博弈类的问题常常让我们摸不着头脑。当我们没有解题思路的时候，不妨试着写几项试试
    1 失败
    2 拿1 成功
    3 拿1 失败
    4 拿1或2 2时失败 1时成功
    5 拿1 失败
    6 拿1 成功
    N 为奇数的时候 Alice（先手）必败，NN 为偶数的时候 Alice 必胜
    :param N:
    :return:
    '''
    return N % 2 == 0


def divisorGame2(N: int) -> bool:
    '''
    递推 动态规划
    :param N:
    :return:
    '''
    f = [False for i in range(N + 6)]
    f[1] = False
    f[2] = True
    for i in range(3, N + 1):
        for j in range(1, i // 2 + 1):
            if i % j == 0 and not f[i - j]:
                f[i] = True
                break
    return f[N]

if __name__ == '__main__':
    '''
    '''
    print(divisorGame2(6))