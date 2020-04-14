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

if __name__  ==  '__main__':
    print(letter_combinations('23'))