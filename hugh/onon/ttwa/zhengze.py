#!/usr/bin/env python
# -- coding: utf-8 --#
# @Time : 2019/12/20 22:17 
# @Author : Aries 
# @Site :  
# @File : zhengze.py 
# @Software: PyCharm

import re
import sys


# 二分搜索插入 用于获取一个数列中升序/降序等的数值统计
def binaryInsert(array, number):
    '''
    二分搜索插入 用于获取一个数列中升序/降序等的数值统计
    :param array:
    :param number:
    :return:
    '''
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


def move_people_less(h):

    '''
    一个队列中使得 t1<t2<n>n1>n2，最少移动
    最初的版本 但是经过测试 该方式运行速度比较慢 耗时太多
    :return:
    '''
    h_len = len(h)
    print(h_len)
    min_num = [1 for i in range(h_len)]
    max_num = [1 for i in range(h_len)]
    for i in range(h_len):
        for j in range(i):
            if h[i] > h[j] and min_num[i] < min_num[j] + 1:
                min_num[i] = min_num[j] + 1
            if h[h_len - 1 - i] > h[h_len - 1 - j] and max_num[h_len - 1 - i] < max_num[h_len - 1 - j] + 1:
                max_num[h_len - 1 - i] = max_num[h_len - 1 - j] + 1

    min_max = 0
    for i in range(h_len):
        min_max = max(min_max, min_num[i] + max_num[i] - 1)
    print(h_len - min_max)


def encry_pass_ph(line):
    '''
    一个加密函数
    如果是数字则保持不变
    如果是小写字母，则按照手机展示的九宫格规则转换为数字
    如果是大写字母，则转换为小写字母的下一位 Z则转换为a
    :param line:
    :return:
    '''
    mes = ''
    nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    ch = {'a': '2', 'b': '2', 'c': '2', 'd': '3', 'e': '3', 'f': '3', 'g': '4', 'h': '4', 'i': '4', 'j': '5',
          'k': '5', 'l': '5', 'm': '6', 'n': '6', 'o': '6', 'p': '7', 'q': '7', 'r': '7', 's': '7', 't': '8',
          'u': '8', 'v': '8', 'w': '9', 'x': '9', 'y': '9', 'z': '9'}
    print(mes + '--')
    for i in range(len(line)):
        print(line[i])
        print(line[i] in nums)
        print( bool(re.search('[a-z]', line[i])))
        if line[i] in nums:
            mes += line[i]
        elif bool(re.rearch('[a-z]', line[i])):
            mes += ch[line[i]]
        else:
            if line[i].lower() == 'z':
                mes += 'a'
            else:
                mes += chr(ord(line[i].lower()) + 1)
    return mes

def valid_repeat_mes(line):
    '''
    判断一个字符串中重复出现的最长子字符串的长度
    :param line:
    :return:
    '''
    line_len = len(line)
    for i in range(int(line_len / 2), -1, -1):
        print(i)
        for j in range(0, line_len - i):
            print(i, j)
            sample = line[j:i]
            left = line[i:]
            if left.find(sample) != -1:
                max_repeat = max(max_repeat, len(sample))
    return max_repeat


def valid_pass(line):
    '''
    校验密码
    位数大于8
    数字、小写字母、大写字母及其他三种以上
    重复的内容的长度不超过2
    :param line:
    :return:
    '''
    if len(line) < 9:
        print('NG')
        return
    print(line)
    count = 0

    if bool(re.search(r'\d', line)):
        count += 1

    if bool(re.search(r'[a-z]', line)):
        count += 1
    if bool(re.search(r'[A-Z]', line)):
        count += 1
    if bool(re.search(r'[^a-zA-Z\d]', line)):
        count += 1

    if count < 3:
        print('NG')
        return
    print(line)
    max_repeat = valid_repeat_mes(line)
    if max_repeat > 2:
        print('NG')
        return

    print('OK')


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
    #         valid_pass(line)
    #     except:
    #         break

    # while True:
    #     try:
    #         line = sys.stdin.readline().strip()
    #         if line == '':
    #             break
    #         print(encry_pass_ph(line))
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

    # 一个队列中使得 t1<t2<n>n1>n2，最少移动
    # 最初的版本 但是经过测试 该方式运行速度比较慢 耗时太多
    # num = input()
    # h = list(map(int, input().split(' ')))
    # move_people_less(h)


    # 一个队列中使得 t1<t2<n>n1>n2，最少移动
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
