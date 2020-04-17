#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : letter_combinations.py
# Author: chen
# Date  : 2020-04-13

from typing import List

def letter_combinations(digits: str) -> List[str]:
    '''
    给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。

    给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
    输入："23"
    输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
    :param digits:
    :return:
    '''
    l_list = []
    def letter_combi(letter, index):
        if index >= d_len:
            l_list.append(letter)
            return
        else:
            if digits[index] == '1':
                index += 1
                letter_combi(letter, index)
            elif digits[index] == '0':
                index += 1
                letter += ' '
                letter_combi(letter, index)
            else:
                tmp = num_letter[int(digits[index])]
                index += 1
                for l in tmp:
                    letter += l
                    letter_combi(letter, index)
                    letter = letter[0:len(letter) - 1]

    num_letter = [' ', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
    d_len = len(digits)
    letter_combi('', 0)
    return l_list


def generateParenthesis(n: int) -> List[str]:
    '''
    数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
    :param self:
    :param n:
    :return:
    '''
    if n == 0:
        return ['']
    lst = []
    def generate_per(first, last, par_str, n):
        print(first, last, par_str, n, lst)
        if first < n:
            par_str += '('
            first += 1
            generate_per(first, last, par_str, n)
            par_str = par_str[:-1]
            first -= 1

        if last < first:
            par_str += ')'
            last += 1
            if last == n:
               lst.append(par_str)
            else:
                generate_per(first, last, par_str, n)
                par_str = par_str[:-1]
                last -= 1
    generate_per(0, 0, '', n)
    return lst


def generateParenthesis2(n: int) -> List[str]:
    '''
    数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
    :param self:
    :param n:
    :return:
    '''
    if n == 0:
        return ['']
    ans = []
    for i in range(n - 1, -1 , -1):
        for left in generateParenthesis2(i):
            for right in generateParenthesis2(n - i - 1):
                ans.append('({}){}'.format(left, right))
    return ans


if __name__  ==  '__main__':
    print(letter_combinations('23'))
    print(generateParenthesis(3))
    print(generateParenthesis2(3))