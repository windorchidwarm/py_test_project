#!/usr/bin/env python
# -- coding: utf-8 --#
# @Time : 2019/12/22 12:30 
# @Author : Aries 
# @Site :  
# @File : sort_word.py 
# @Software: PyCharm


import re


def sort_word(line):
    '''
    非a-zA-Z的字符作为空格，然后排序输出
    :param line:
    :return:
    '''
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
    return ' '.join(data)



def encry_line(en_key, en_str):
    '''
    有一种技巧可以对数据进行加密，它使用一个单词作为它的密匙。下面是它的工作原理：
    首先，选择一个单词作为密匙，如TRAILBLAZERS。如果单词中包含有重复的字母，只保留第1个，其余几个丢弃。
    现在，修改过的那个单词属于字母表的下面，如下所示：

    A B C D E F G H I J K L M N O P Q R S T U V W X Y Z

    T R A I L B Z E S C D F G H J K M N O P Q U V W X Y

    上面其他用字母表中剩余的字母填充完整。在对信息进行加密时，信息中的每个字母被固定于顶上那行，
    并用下面那行的对应字母一一取代原文的字母(字母字符的大小写状态应该保留)。
    因此，使用这个密匙，Attack AT DAWN(黎明时攻击)就会被加密为Tpptad TP ITVH。
    :param en_str:
    :param line:
    :return:

    nihao
    ni
    输出
    复制
    le
    '''
    key_list = []
    for i in range(26):
        key_list.append(chr(65 + i))

    en_key = en_key.upper()
    en_val = []
    for i in en_key:
        if not i in en_val:
            en_val.append(i)

    for i in key_list:
        if not i in en_val:
            en_val.append(i)
    # print(en_val)
    msg = ''
    for v in en_str:
        if not v in en_val:
            msg += en_val[ord(v) - 97].lower()
        else:
            msg += en_val[ord(v) - 65]
    return msg


if __name__ == '__main__':
    print('-----------')

    # line = input().strip()
    # print(sort_word(line))

    en_key = 'igtxbesmnyrehanvuvqhukrtmpynmpdvjlppuq'
    en_str = 'wiumbxibguwicjfyvkznbqzvo'
    # n_key = input().strip()
    # en_str = input().s
    print(encry_line(en_key, en_str))
    print(ord('A'))
    print(ord('a'))

