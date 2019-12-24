#!/usr/bin/env python
# -- coding: utf-8 --#
# @Time : 2019/12/24 14:39 
# @Author : Aries 
# @Site :  
# @File : num_combination.py 
# @Software: PyCharm



def combination_weight_nums(weights, nums):
    '''
    现有一组砝码，重量互不相等，分别为m1,m2,m3…mn；
    每种砝码对应的数量为x1,x2,x3...xn。现在要用这些砝码去称物体的重量(放在同一侧)，问能称出多少种不同的重量。
    注：
    称重重量包括0
    :param weights:
    :param nums:
    :return:
    '''
    max_weight = 0
    for i in range(len(weights)):
        max_weight += weights[i] * nums[i]

    h_comb = [0 for i in range(max_weight + 1)]
    h_comb[0] = 1

    for i in range(len(weights)):
        for j in range(max_weight, -1, -1):
            if h_comb[j] == 1:
                for k in range(nums[i]):
                    h_comb[j + (k + 1) * weights[i]] = 1
    count = 0
    for i in range(len(h_comb)):
        if h_comb[i] == 1:
            count += 1
    return count


def combination_weight_nums2(weights, nums):
    '''
    现有一组砝码，重量互不相等，分别为m1,m2,m3…mn；
    每种砝码对应的数量为x1,x2,x3...xn。现在要用这些砝码去称物体的重量(放在同一侧)，问能称出多少种不同的重量。
    注：
    称重重量包括0
    :param weights:
    :param nums:
    :return:
    '''
    w_dict = set()
    w_dict.add(0)

    for i in range(len(weights)):
        tmp_dict = w_dict.copy()
        for x in tmp_dict:
            for j in range(nums[i]):
                tmp = x + weights[i] * (j + 1)
                w_dict.add(tmp)
    return len(w_dict)


if __name__ == '__main__':
    print('-----------')
    num = input().strip()
    weights = list(map(int, input().strip().split(' ')))
    nums = list(map(int, input().strip().split(' ')))
    print(combination_weight_nums(weights, nums))
    print(combination_weight_nums2(weights, nums))