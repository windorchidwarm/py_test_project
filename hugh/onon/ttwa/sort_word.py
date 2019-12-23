#!/usr/bin/env python
# -- coding: utf-8 --#
# @Time : 2019/12/22 12:30 
# @Author : Aries 
# @Site :  
# @File : sort_word.py 
# @Software: PyCharm


import re


if __name__ == '__main__':
    line = input().strip()
    msg = ''
    data = []
    for i in line:
        print(i)
        if bool(re.search('[a-zA-Z]', i)):
            msg += i
        else:
            if msg != '':
                data.append(msg)
                msg = ''
    if msg != '':
        data.append(msg)
    data.reverse()
    print(' '.join(data))