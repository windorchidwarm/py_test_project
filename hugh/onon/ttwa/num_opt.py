#!/usr/bin/env python
# -- coding: utf-8 --#
# @Time : 2019/12/21 22:34 
# @Author : Aries 
# @Site :  
# @File : num_opt.py 
# @Software: PyCharm

import re
import math


fib_num = dict()

def fib(num):
    '''
    斐波那契数列
    :param num:
    :return:
    '''
    if num == 1 or num == 2:
        return 1
    elif num in fib_num.keys():
        return fib_num.get(num)
    else:
        res = fib(num - 1) + fib(num - 2)
        fib_num[num] = res
        return res



def valid_perfect_num(n):
    '''
    判断n是否是完全数
    :param n:
    :return:
    '''
    # count = 0
    # for i in range(1, int(n / 2) + 1):
    #     if n % i == 0:
    #         count += i
    m = int(math.sqrt(n))
    count = 1
    for i in range(2, m+1):
        if n % i == 0:
            count += i
            count += int(n / i)
    if count == n:
        return True
    else:
        return False



def swap_data(num1, num2):
    '''
    交换两个数
    :param num1:
    :param num2:
    :return:
    '''
    tmp = num1
    num1 = num2
    num2 = tmp
    return num1, num2


def arange_right(data, left, right, k):
    '''
    获取前k个最小的数
    :param data:
    :param right:
    :param left:
    :param k:
    :return:
    '''
    if left >= right:
        return data

    i,j = left, right
    tmp = data[j]
    while i != j:
        while i < j and data[i] <= tmp:
            i += 1
        data[i], data[j] = swap_data(data[i], data[j])
        while i < j and data[j] > tmp:
            j -= 1
        data[i], data[j] = swap_data(data[i], data[j])

    tmp = 1 if data[i] <= tmp else 0
    # print(data)
    if i == right:
        return arange_right(data, left, right - 1, k)
    elif i - left + tmp == k:
        return data
    elif i - left + tmp < k:
        return arange_right(data, i + tmp, right, k - i - tmp + left)
    else:
        return arange_right(data, left, i + tmp, k)


if __name__ == '__main__':
    print('-----')
    # s = '47Aa'
    # for i in s:
    #     print(i)
    #     print(str(bin(int(i, 16))))
    #     i_s = str(bin(int(i, 16))).replace('0b', '')
    #     i_l = list(i_s)
    #     i_l.reverse()
    #     t_s = ''.join(i_l)
    #     print(t_s)
    #     if len(t_s) < 4:
    #         t_s += '0' * (4 - len(t_s))
    #     r_s = str(hex(int(t_s, 2))).replace('0x', '')
    #     print(r_s.upper())

    # line = input().strip()
    # data = line.replace(' ', '')
    # p = []
    # d = []
    # for i in range(len(data)):
    #     if i % 2 == 0:
    #         p.append(data[i])
    #     else:
    #         d.append(data[i])
    # p.sort()
    # d.sort()
    #
    # mes = ''
    # for i in range(len(p)):
    #     mes += (p[i] + d[i]) if i < len(d) else p[i]
    #
    # r_mes = ''
    # for r in mes:
    #     if bool(re.search('[a-fA-F0-9]', r)):
    #         r_list = list(str(bin(int(r, 16))).replace('0b', ''))
    #         r_list.reverse()
    #         r_r = ''.join(r_list)
    #         if len(r_list) < 4:
    #             r_r += '0' * (4 - len(r_list))
    #         r_mes += str(hex(int(r_r, 2))).replace('0x', '').upper()
    #     else:
    #         r_mes += r
    # print(r_mes)

    # count = 0
    # for i in range(2, 2670):
    #     if valid_perfect_num(i):
    #         count += 1
    #     print(i, valid_perfect_num(i), count)
    # print(count)
    # print(fib(9))

    line = input().strip()
    num, n = [int(i) for i in line.split(' ')]
    data = list(map(int, input().strip().split(' ')))
    print(len(data))
    n_data = arange_right(data, 0, num - 1, n)
    n_data = n_data[0:n]
    n_data = sorted(n_data)
    print(' '.join([str(j) for j in n_data]))