#!/usr/bin/env python
# -- coding: utf-8 --#
# @Time : 2019/12/20 22:17 
# @Author : Aries 
# @Site :  
# @File : zhengze.py 
# @Software: PyCharm

import re
import sys


def binaryInsert(array, number):
    if len(array) == 0:
        array.append(number)
        return 1
    if number < array[0]:
        array[0] = number
        return 1
    if number > array[-1]:
        array.append(number)
        return len(array)
    # 找到第一个大于等于number的位置
    low, high = 0, len(array) - 1
    while (low < high):
        mid = (low + high) // 2
        if array[mid] >= number:
            high = mid
        else:
            low = mid + 1
    array[low] = number
    return low + 1

if __name__ == '__main__':
    # line = 'xxx3$'
    # print(bool(re.search(r'\d', line)))
    # print(bool(re.search(r'[^a-zA-Z0-9]', line)))
    # print(line.find('3'))

    # while True:
    #     try:
    #         line = sys.stdin.readline().strip()
    #         print(line)
    #         if line == '':
    #             break
    #
    #         if len(line) < 9:
    #             print('NG')
    #             continue
    #         print(line)
    #         count = 0
    #
    #         if bool(re.search(r'\d', line)):
    #             count += 1
    #
    #         if bool(re.search(r'[a-z]', line)):
    #             count += 1
    #         if bool(re.search(r'[A-Z]', line)):
    #             count += 1
    #         if bool(re.search(r'[^a-zA-Z\d]', line)):
    #             count += 1
    #
    #         if count < 3:
    #             print('NG')
    #             continue
    #         print(line)
    #         max_repeat = 0
    #         line_len = len(line)
    #         print(line_len)
    #
    #         for i in range(int(line_len / 2), -1, -1):
    #             print(i)
    #             for j in range(0, line_len - i):
    #                 print(i, j)
    #                 sample = line[j:i]
    #                 left = line[i:]
    #                 if left.find(sample) != -1:
    #                     max_repeat = max(max_repeat, len(sample))
    #         print(line)
    #         if max_repeat > 2:
    #             print('NG')
    #             continue
    #
    #         print('OK')
    #     except:
    #         break

    # while True:
    #     try:
    #         line = sys.stdin.readline().strip()
    #         if line == '':
    #             break
    #
    #         mes = ''
    #         nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    #         ch = {'a': '2', 'b': '2', 'c': '2', 'd': '3', 'e': '3', 'f': '3', 'g': '4', 'h': '4', 'i': '4', 'j': '5',
    #               'k': '5', 'l': '5', 'm': '6', 'n': '6', 'o': '6', 'p': '7', 'q': '7', 'r': '7', 's': '7', 't': '8',
    #               'u': '8', 'v': '8', 'w': '9', 'x': '9', 'y': '9', 'z': '9'}
    #         print(mes + '--')
    #         for i in range(len(line)):
    #             print('xxx')
    #             print(line[i])
    #             print(line[i] in nums)
    #             print( bool(re.search('[a-z]', line[i])))
    #             if line[i] in nums:
    #                 print('xxx')
    #                 mes += line[i]
    #             elif bool(re.rearch('[a-z]', line[i])):
    #                 print('xxx')
    #                 mes += ch[line[i]]
    #             else:
    #                 print('xxx')
    #                 if line[i].lower() == 'z':
    #                     mes += 'a'
    #                 else:
    #                     mes += chr(ord(line[i].lower()) + 1)
    #         print(mes)
    #     except:
    #         break

    # num = sys.stdin.readline().strip()
    # h = sys.stdin.readline().strip().split(' ')
    #
    # min_num = len(h)
    # for i in range(len(h)):
    #     mv = 0
    #     tmp = i
    #     for j in range(i - 1, -1, -1):
    #         if int(h[tmp]) < int(h[j]):
    #             mv += 1
    #         else:
    #             tmp = j
    #     tmp = i
    #     for j in range(i + 1, len(h)):
    #         if int(h[tmp]) < int(h[j]):
    #             mv += 1
    #         else:
    #             tmp = j
    #     min_num = min(min_num, mv)
    # print(min_num)

    # num = input()
    # h = list(map(int, input().split(' ')))
    # h_len = len(h)
    # print(h_len)
    # min_num = [1 for i in range(h_len)]
    # max_num = [1 for i in range(h_len)]
    # for i in range(h_len):
    #     for j in range(i):
    #         if h[i] > h[j] and min_num[i] < min_num[j] + 1:
    #             min_num[i] = min_num[j] + 1
    #         if h[h_len - 1 - i] > h[h_len - 1 - j] and max_num[h_len - 1 - i] < max_num[h_len - 1 - j] + 1:
    #             max_num[h_len - 1 - i] = max_num[h_len - 1 - j] + 1
    #
    # min_max = 0
    # for i in range(h_len):
    #     min_max = max(min_max, min_num[i] + max_num[i] - 1)
    # print(h_len - min_max)

    n = int(input())
    array = list(map(int, input().split()))
    l, l_tmp, r, r_tmp = [], [], [], []
    for number in array:
        l.append(binaryInsert(l_tmp, number))
        print(l_tmp)
        print(l[-1])
    for i in range(len(array) - 1, -1, -1):
        r.append(binaryInsert(r_tmp, array[i]))
    maxer = 0
    r = r[::-1]
    for i in range(len(r)):
        maxer = max(l[i] + r[i] - 1, maxer)
    print(len(r) - maxer)
