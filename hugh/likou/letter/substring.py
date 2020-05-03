#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : substring.py
# Author: chen
# Date  : 2020-05-03

from typing import List
from collections import Counter


def findSubstring(s: str, words: List[str]) -> List[int]:
    '''

    :param s:
    :param words:
    :return:
    '''
    if not s or not words: return []

    one_len = len(words[0])
    all_len = one_len * len(words)

    if len(s) < all_len: return []

    word_count = Counter(words)
    print(word_count)
    result = []
    for i in range(0, len(s) - all_len + 1):
        tmp_str = s[i:i+all_len]
        c_tmp = []
        for j in range(0, all_len, one_len):
            c_tmp.append(tmp_str[j: j + one_len])
        print(c_tmp)
        if Counter(c_tmp) == word_count:
            result.append(i)
    return result

if __name__ == '__main__':
    print(findSubstring("wordgoodgoodgoodbestword", ["word","good","best","good"]))
