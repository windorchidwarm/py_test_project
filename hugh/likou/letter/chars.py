#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : chars.py
# Author: chen
# Date  : 2020-04-18


def minDistance(word1: str, word2: str) -> int:
    '''
    给你两个单词 word1 和 word2，请你计算出将 word1 转换成 word2 所使用的最少操作数 。

    你可以对一个单词进行如下三种操作：

    插入一个字符
    删除一个字符
    替换一个字符
    :param word1:
    :param word2:
    :return:
    '''
    if len(word1) == 0: return len(word2)
    if len(word2) == 0: return len(word1)

    if word1[0] == word2[0]:
        return minDistance(word1[1:], word2[1:])
    else:
        return min(minDistance(word1, word2[1:]), minDistance(word1[1:], word2), minDistance(word1[1:], word2[1:])) + 1


def minDistance2(word1: str, word2: str) -> int:
    if len(word1) == 0: return len(word2)
    if len(word2) == 0: return len(word1)
    min_distance = [[ 0 for i in range(len(word1) + 1)] for j in range(len(word2) + 1)]
    for i in range(len(word1)): min_distance[0][i + 1] = i + 1
    for j in range(len(word2)): min_distance[j + 1][0] = j + 1
    for i in range(len(word2)):
        for j in range(len(word1)):
            if word1[j] == word2[i]:
                min_distance[i + 1][j + 1] = min_distance[i][j]
            else:
                min_distance[i + 1][j + 1] = min(min_distance[i][j], min_distance[i + 1][j], min_distance[i][j + 1]) + 1
    return min_distance[len(word2)][len(word1)]

def reverseWords( s: str) -> str:
    '''
    给定一个字符串，逐个翻转字符串中的每个单词。
    示例 1：

    输入: "the sky is blue"
    输出: "blue is sky the"
    :param s:
    :return:
    '''
    if s == '' or len(s) == 0:
        return ''
    s_list = s.split(' ')
    res = ''
    print(s_list)
    for value in s_list:
        if not value == '':
            if res:
                res = value + ' ' + res
            else:
                res += value
    return res


if __name__ == '__main__':
    print(minDistance2('horse', 'ros'))
    print(minDistance2('intention', 'execution'))
    print(reverseWords('a good   example'))