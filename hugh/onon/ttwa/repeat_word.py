#!/usr/bin/env python
# -- coding: utf-8 --#
# @Time : 2019/12/23 14:58 
# @Author : Aries 
# @Site :  
# @File : repeat_word.py 
# @Software: PyCharm


import sys


def max_huiwen_word_baoli(line):
    '''
    暴力破解法
    :param line:
    :return:
    '''
    max_len = 1
    for i in range(len(line)):
        if i + 2 < len(line):
            if line[i] == line[i + 2]:
                j = 1
                while (i - j > -1) and (i + 2 + j < len(line)):
                    if line[i - j] == line[i + 2 + j]:
                        j += 1
                        continue
                    else:
                        break
                max_len = max(max_len, (j - 1) * 2 + 3)
        if i + 1 < len(line):
            if line[i] == line[i + 1]:
                j = 1
                while (i - j > -1) and (i + 1 + j < len(line)):
                    if line[i - j] == line[i + 1 + j]:
                        j += 1
                        continue
                    else:
                        break
                max_len = max(max_len, (j - 1) * 2 + 2)
    return max_len


def manacher(line):
    '''
    “马拉车”算法，可以在时间复杂度为O(n)的情况下求解一个字符串的最长回文子串长度的问题。
    :param line:
    :return:
    '''
    msg = '#'
    for i in line:
        msg += i + '#'

    m = [0 for i in range(len(msg))]

    R = -1
    c = -1
    max_val = -1

    for i in range(len(m)):
        m[i] = min(m[2 * c - i], R - i + 1) if (R > i) else 1
        while (i + m[i] < len(m)) and (i - m[i] > -1):
            if msg[i - m[i]] == msg[i + m[i]]:
                m[i] += 1
            else:
                break
        if i + m[i] > R:
            R = i + m[i] - 1
            c = i
        max_val = max(max_val, m[i])
    return max_val - 1



if __name__ == '__main__':
    print('------------')
    '''
    Catcher是MCA国的情报员，他工作时发现敌国会用一些对称的密码进行通信，
    比如像这些ABBA，ABA，A，123321，但是他们有时会在开始或结束时加入一些无关的字符以防止别国破解。
    比如进行下列变化 ABBA->12ABBA,ABA->ABAKK,123321->51233214　。
    因为截获的串太长了，而且存在多种可能的情况（abaaab可看作是aba,或baaab的加密形式），
    Cathcer的工作量实在是太大了，他只能向电脑高手求助，你能帮Catcher找出最长的有效密码串吗？
    '''

    line = input().strip()

    # 暴力破解
    # print(max_huiwen_word_baoli(line)
    print(manacher(line))