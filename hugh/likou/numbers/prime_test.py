#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : prime_test.py
# Author: BBD
# Date  : 2020/5/29


from typing import List

def prime_list(n: int) -> List[int]:
    '''
    n以内的素数列表
    Eratosthenes求素数方法
    :param n:
    :return:
    '''
    if n <= 1: return []

    prime = [1 for i in range(n + 1)]
    prime[0], prime[1] = 0, 0

    i = 2
    while i * i <= n:
        if prime[i] == 1:
            for j in range(2 * i, n + 1):
                if prime[j] == 0:  continue
                if j % i == 0: prime[j] = 0
        i += 1
    rst = []
    for i in range(2, n + 1):
        if prime[i] == 1: rst.append(i)

    return rst


if __name__ == '__main__':
    '''
    '''
    print(prime_list(100))