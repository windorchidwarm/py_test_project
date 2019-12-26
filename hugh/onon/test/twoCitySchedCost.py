#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : twoCitySchedCost.py
# Author: chen
# Date  : 2019-09-27


def twoCitySchedCost(consts):
    # 计算从B到A调换的差价
    pri_list = []
    prices = 0
    for i in range(len(consts)):
        pri_list.append(consts[i][1] - consts[i][0])
        prices += consts[i][0]

    pri_list.sort()
    print(pri_list)
    for i in range(int(len(consts)/2)):
        prices += pri_list[i]
    print(prices)


if __name__ == '__main__':
    consts = [[10, 20], [30, 200], [400, 50], [30, 20]]
    twoCitySchedCost(consts)
