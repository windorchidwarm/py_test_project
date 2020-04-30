#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : exam_test2.py
# Author: chen
# Date  : 2020-04-30



import sys
# for line in sys.stdin:
#     a = line.split()
#     print(int(a[0]) + int(a[1]))
#
# n = int(sys.stdin.readline().strip())
# ans = 0
# for i in range(n):
#     # 读取每一行
#     line = sys.stdin.readline().strip()
#     # 把每一行的数字分隔后转化成int列表
#     values = list(map(int, line.split()))
#     for v in values:
#         ans += v
# print(ans)


if __name__ == '__main__':
    '''
    a 到 b的立方和
    '''
    while True:
        # n = int(sys.stdin.readline().strip())
        line = sys.stdin.readline().strip()
        print(line)
        data = line.split(' ')
        a, b = int(data[0]), int(data[1])
        if a < 0 or b > 200:
            print(0)
        else:
            data = line.split()
            a, b = int(data[0]), int(data[1])
            cha = b - a
            sum_a_b = int((a + b) * (cha + 1) / 2)
            sum_aa_bb = int(((b + 1) ** 3 - a ** 3 - 3 * sum_a_b - cha - 1) / 3)
            res = int(((b + 1) ** 4 - a ** 4 - 6 * sum_aa_bb - 4 * sum_a_b - cha - 1) / 4)
            print(res, end='')