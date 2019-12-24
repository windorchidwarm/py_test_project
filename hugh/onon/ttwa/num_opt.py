#!/usr/bin/env python
# -- coding: utf-8 --#
# @Time : 2019/12/21 22:34 
# @Author : Aries 
# @Site :  
# @File : num_opt.py 
# @Software: PyCharm

import re


fib_num = dict()

def fib(num):
    if num == 1 or num == 2:
        return 1
    elif num in fib_num.keys():
        return fib_num.get(num)
    else:
        res = fib(num - 1) + fib(num - 2)
        fib_num[num] = res
        return res


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

    print(fib(9))