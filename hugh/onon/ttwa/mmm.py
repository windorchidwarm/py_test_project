#!/usr/bin/env python
# -- coding: utf-8 --#
# @Time : 2019/12/21 22:21 
# @Author : Aries 
# @Site :  
# @File : mmm.py 
# @Software: PyCharm


if __name__ == '__main__':
    print(ord('9'))

    en_str = input().strip()
    de_str = input().strip()

    en_str_d = ''
    for i in range(len(en_str)):
        if ord(en_str[i]) in range(65, 91):
            if en_str[i] == 'Z':
                en_str_d += 'a'
            else:
                en_str_d += chr(ord(en_str[i]) + 1).lower()
        elif ord(en_str[i]) in range(97, 123):
            if en_str[i] == 'z':
                en_str_d += 'A'
            else:
                en_str_d += chr(ord(en_str[i]) + 1).upper()
        elif ord(en_str[i]) in range(48, 58):
            if en_str[i] == '9':
                en_str_d += '0'
            else:
                en_str_d += str(int(en_str[i]) + 1)
    print(en_str_d)

    de_str_d = ''
    for i in range(len(de_str)):
        if ord(de_str[i]) in range(65, 91):
            if de_str[i] == 'A':
                de_str_d += 'z'
            else:
                de_str_d += chr(ord(de_str[i]) - 1).lower()
        elif ord(de_str[i]) in range(97, 123):
            if de_str[i] == 'a':
                de_str_d += 'Z'
            else:
                de_str_d += chr(ord(de_str[i]) - 1).upper()
        elif ord(de_str[i]) in range(48, 58):
            if de_str[i] == '0':
                de_str_d += '9'
            else:
                de_str_d += str(int(de_str[i]) - 1)
    print(de_str_d)