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


def getMaxRepetitions(s1: str, n1: int, s2: str, n2: int) -> int:
    '''
    由 n 个连接的字符串 s 组成字符串 S，记作 S = [s,n]。例如，["abc",3]=“abcabcabc”。
    如果我们可以从 s2 中删除某些字符使其变为 s1，则称字符串 s1 可以从字符串 s2 获得。例如，根据定义，"abc" 可以从 “abdbec” 获得，但不能从 “acbbe” 获得。
    现在给你两个非空字符串 s1 和 s2（每个最多 100 个字符长）和两个整数 0 ≤ n1 ≤ 106 和 1 ≤ n2 ≤ 106。现在考虑字符串 S1 和 S2，其中 S1=[s1,n1] 、S2=[s2,n2] 。
    请你找出一个可以满足使[S2,M] 从 S1 获得的最大整数 M
    :param self:
    :param s1:
    :param n1:
    :param s2:
    :param n2:
    :return:
    '''
    if n1 == 0:
        return 0

    s1cnt, index, s2cnt = 0, 0, 0
    # recall 是我们用来找循环节的变量，它是一个哈希映射
    # 我们如何找循环节？假设我们遍历了 s1cnt 个 s1，此时匹配到了第 s2cnt 个 s2 中的第 index 个字符
    # 如果我们之前遍历了 s1cnt' 个 s1 时，匹配到的是第 s2cnt' 个 s2 中同样的第 index 个字符，那么就有循环节了
    # 我们用 (s1cnt', s2cnt', index) 和 (s1cnt, s2cnt, index) 表示两次包含相同 index 的匹配结果
    # 那么哈希映射中的键就是 index，值就是 (s1cnt', s2cnt') 这个二元组
    # 循环节就是；
    #    - 前 s1cnt' 个 s1 包含了 s2cnt' 个 s2
    #    - 以后的每 (s1cnt - s1cnt') 个 s1 包含了 (s2cnt - s2cnt') 个 s2
    # 那么还会剩下 (n1 - s1cnt') % (s1cnt - s1cnt') 个 s1, 我们对这些与 s2 进行暴力匹配
    # 注意 s2 要从第 index 个字符开始匹配
    recall = dict()
    while True:
        s1cnt += 1
        for ch in s1:
            if ch == s2[index]:
                index += 1
                if index == len(s2):
                    s2cnt, index = s2cnt + 1, 0

        if s1cnt == n1:
            return s2cnt // n2

        if index in recall:
            s1cnt_prime, s2cnt_prime = recall[index]
            # 前 s1cnt' 个 s1 包含了 s2cnt' 个 s2
            pre_loop = (s1cnt_prime, s2cnt_prime)
            # 以后的每 (s1cnt - s1cnt') 个 s1 包含了 (s2cnt - s2cnt') 个 s2
            in_loop = (s1cnt - s1cnt_prime, s2cnt - s2cnt_prime)
            break
        else:
            recall[index] = (s1cnt, s2cnt)
    # ans 存储的是 S1 包含的 s2 的数量，考虑的之前的 pre_loop 和 in_loop
    ans = pre_loop[1] + (n1 - pre_loop[0]) // in_loop[0] * in_loop[1]
    # S1 的末尾还剩下一些 s1，我们暴力进行匹配
    rest = (n1 - pre_loop[0]) % in_loop[0]
    for i in range(rest):
        for ch in s1:
            if ch == s2[index]:
                index += 1
                if index == len(s2):
                    ans, index = ans + 1, 0
    # S1 包含 ans 个 s2，那么就包含 ans / n2 个 S2
    return ans // n2


if __name__ == '__main__':
    print(minDistance2('horse', 'ros'))
    print(minDistance2('intention', 'execution'))
    print(reverseWords('a good   example'))