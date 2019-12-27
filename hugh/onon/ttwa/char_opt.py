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


if __name__ == '__main__':
    line = 'aabbccddeeff'
    res = first_only_char(line)
