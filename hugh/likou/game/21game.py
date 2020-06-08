#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 21game.py
# Author: chen
# Date  : 2020-06-03

def new21Game(N: int, K: int, W: int) -> float:
    if K == 0:
        return 1.0
    dp = [0.0] * (K + W)
    for i in range(K, min(N, K + W - 1) + 1):
        dp[i] = 1.0
    for i in range(K - 1, -1, -1):
        for j in range(1, W + 1):
            dp[i] += dp[i + j] / W
    print(dp)
    return dp[0]

def new21Game2(N: int, K: int, W: int) -> float:
    if K == 0:
        return 1.0
    dp = [0.0] * (K + W)
    for i in range(K, min(N, K + W - 1) + 1):
        dp[i] = 1.0
    dp[K - 1] = float(min(N - K + 1, W)) / W
    for i in range(K - 2, -1, -1):
        dp[i] = dp[i + 1] - (dp[i + W + 1] - dp[i + 1]) / W
    return dp[0]


if __name__ == '__main__':
    '''
    '''
    print(new21Game(21, 17, 10))