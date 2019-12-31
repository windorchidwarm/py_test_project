#!/usr/bin/env python
# -- coding: utf-8 --#
# @Time : 2019/12/27 22:22 
# @Author : Aries 
# @Site :  
# @File : char_opt.py 
# @Software: PyCharm


def first_only_char(line):
    '''
    查找第一个单独的字符在列中
    为空的处理 -1
    :param line:
    :return:
    '''
    res = ''
    print(line[10:])
    for i in range(len(line)):
        val = line[i]
        if i == 0:
            if not val in line[1:]:
                res = line[i]
                break
        elif i == len(line) - 1:
            if not val in line[0:len(line) - 1]:
                res = line[i]
                break
        else:
            if not (val in line[0:i] or val in line[i + 1:]):
                res = line[i]
                break
    return res


def z_char_opt(s, num):
    '''
    将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。
    比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：
    L   C   I   R
    E T O E S I I G
    E   D   H   N
    之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。

    请你实现这个将字符串进行指定行数变换的函数：

    string convert(string s, int numRows);
    :param s:
    :param num:
    :return:
    '''
    if num < 2 : return s
    s_list = []

    i = 0
    while i * (2 * num - 2) < len(s):
        s_list.append(s[i * (2 * num - 2) : (i + 1) * (2 * num - 2)])
        i += 1
    print(s_list)

    n_s = ''
    i = 0
    while i < num:
        for val in s_list:
            n_s += val[i] if i < len(val) else ''
            if not (i == 0 or i == num - 1):
                n_s += val[2 * num - 2 - i] if 2 * num - 2 - i < len(val) else ''
        i += 1
    print(n_s)
    return n_s

def z_char_opt2(s, numRows):
    if numRows < 2 : return s
    i = 0
    flag = -1
    s_l = ['' for i in range(numRows)]
    for val in s:
        s_l[i] += val
        if i == 0 or i == numRows - 1: flag = -flag
        i += flag
    print(s_l)
    print(''.join(s_l))
    return ''.join(s_l)






if __name__ == '__main__':
    print('-----------')

    # line = 'aabbccddeeff'
    # res = first_only_char(line)
    z_char_opt('LEETCODEISHIRING', 3)
    z_char_opt('LEETCODEISHIRING', 4)
    z_char_opt2('LEETCODEISHIRING', 4)
    z_char_opt2('AB', 1)
