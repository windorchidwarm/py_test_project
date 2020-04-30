#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : wu_fu.py
# Author: chen
# Date  : 2020-04-30

from typing import List


def wu_fu(nums_str: str) -> int:
    '''
        集五福作为近年来大家喜闻乐见迎新春活动，集合爱国福、富强福、和谐福、友善福、敬业福即可分享超大红包
    以0和1组成的长度为5的字符串代表每个人所得到的福卡，每一位代表一种福卡，1表示已经获得该福卡，单类型福卡不超过1张，随机抽取一个小于10人团队，求该团队最多可以集齐多少套五福？
    输入描述:
    输入若干个"11010"、”00110"的由0、1组成的长度等于5位字符串,代表的指定团队中每个人福卡获得情况
    注意1：1人也可以是一个团队
    注意2：1人可以有0到5张福卡，但福卡不能重复
    :param nums:
    :return:
    '''
    nums = nums_str.split(',')
    ret = [0] * 5
    for data in nums:
        print(len(data))
        for i in range(len(data)):
            if data[i] == '1':
                ret[i] += 1
    ret.sort()
    return ret[0]


if __name__ == '__main__':
    print(wu_fu('11101,10111'))