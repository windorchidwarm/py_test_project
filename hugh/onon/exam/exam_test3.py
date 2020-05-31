#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : exam_test3.py
# Author: chen
# Date  : 2020-05-29


#coding=utf-8
# 本题为考试单行多行输入输出规范示例，无需提交，不计分。
# import sys
# for line in sys.stdin:
#     a = line.split()
#     print(int(a[0]) + int(a[1]))

# import sys
# if __name__ == "__main__":
#     # 读取第一行的n
#     n = int(sys.stdin.readline().strip())
#     ans = 0
#     for i in range(n):
#         # 读取每一行
#         line = sys.stdin.readline().strip()
#         # 把每一行的数字分隔后转化成int列表
#         values = list(map(int, line.split()))
#         for v in values:
#             ans += v
#     print(ans)

import sys

def get_letter(l, num):
    n = ord(l) - ord('a')
    n = (n + num) % 26
    return chr(n + ord('a'))

def cal_str(line):
    r_line = ''
    i, j, k = 1, 2, 4
    for v in range(len(line)):
        if v < 3:
            if v == 0:
                r_line += get_letter(line[0], 1)
            elif v == 1:
                r_line += get_letter(line[1], 2)
            elif v == 2:
                r_line += get_letter(line[2], 4)
        else:
            i, j, k = j, k, i + j + k
            r_line += get_letter(line[v], k)
    print(r_line)

def cal_wu_fu(data):
    lst = [0 for i in range(5)]
    for val in data:
        for c in range(len(val)):
            if int(val[c]) == 1:
                lst[c] += 1
    lst.sort()
    print(lst[0])


if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    for i in range(n):
        line = sys.stdin.readline().strip()
        cal_str(line)

    line = sys.stdin.strip()
    data = line.split(',')

import sys

if __name__ == "__main__":
    m = int(sys.stdin.readline().strip())
    n = int(sys.stdin.readline().strip())
    lst = []
    for i in range(n):
        line = sys.stdin.readline().strip().split(' ')
        lst.append((int(line[0]), int(line[1])))
    lst.sort()
    ans = 0
    rst = []
    for start, end in lst:
        if len(rst) == 0 or ans < n // m:
            ans += 1
            rst.append((end, 1))
        else:
            flag = False
            for i in range(len(rst)):
                last, count = rst[i]
                if last > start:
                    continue
                else:
                    flag = True
                    last = end
                    count += 1
                    rst.pop(i)
                    if count < m:
                        rst.append((last, count))
                    break
            if not flag:
                ans += 1
                rst.append((end, 1))
            rst.sort(reverse=False)

    print(ans)

