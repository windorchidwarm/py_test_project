#!/usr/bin/env python
# -- coding: utf-8 --#
# @Time : 2019/12/21 16:51 
# @Author : Aries 
# @Site :  
# @File : sushubanli.py 
# @Software: PyCharm

import math


def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def find(a,used,matched,ou):
    for i in range(0,len(ou)):
        if is_prime(a+ou[i]) and used[i]==0:
            used[i]=1
            if matched[i]==0 or find(matched[i],used,matched,ou):
                matched[i] = a
                return True
    return False

if __name__ == '__main__':
    # print(int(math.sqrt(8)))
    n = input().strip()
    data = list(map(int, input().strip().split(' ')))

    ji, ou = [], []
    for i in range(int(n)):
        if data[i] % 2 == 0:
            ou.append(data[i])
        else:
            ji.append(data[i])
    result = 0
    match = [0 for i in range(len(ou))]
    for i in range(0, len(ji)):
        used = [0 for i in range(len(ou))]
        if find(ji[i], used, match, ou):
            result += 1
    print(result)

    # dp = [0 for i in range(int(n) + 1)]
    # cnt = 0
    # for i in range(int(n) - 2, -1, -1):
    #     for j in range(int(n) - 1, i, -1):
    #         cnt = (dp[j + 1] + dp[i + 1] - dp[j - 1] + 1) if is_prime(data[i] + data[j]) else dp[i + 1]
    #         dp[i] = max(dp[i], cnt)
    #         print('...' + str(dp))
    #     print(dp)
    # print(dp)
    # print(dp[0])