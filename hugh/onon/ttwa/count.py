#!/usr/bin/env python
# -- coding: utf-8 --#
# @Time : 2019/12/21 11:33 
# @Author : Aries 
# @Site :  
# @File : count.py 
# @Software: PyCharm

from collections import defaultdict

import math

if __name__ == '__main__':

    # i_str = input().split(' ')
    # i_list = []
    # for i in range(1, len(i_str)):
    #     i_list.append(i_str[i])
    #
    # r_str = input().split(' ')
    # r_list = []
    # for i in range(1, len(r_str)):
    #     r_list.append(int(r_str[i]))
    #
    # r_list = list(set(r_list))
    # r_list.sort()
    #
    # count = 0
    # msg = ''
    # for r in r_list:
    #     r_count = 0
    #     r_data = []
    #     r_str = ''
    #     for i in range(len(i_list)):
    #         if i_list[i].find(str(r)) > -1:
    #             r_count += 1
    #             r_str += ' ' + str(i) + ' ' + i_list[i]
    #     if r_count > 0:
    #         count += (r_count + 1) * 2
    #         msg += ' ' + str(r) + ' ' + str(r_count) + r_str
    #
    # msg = str(count) + msg
    # print(msg)

    # print(ord('z'))
    # print(ord('a'))
    # print(ord('Z'))
    # print(ord('A'))
    # print(ord('B'))

    # line = input().strip()
    # ord_dict = {}
    # for i in range(97, 123):
    #     ord_dict[chr(i)] = ''
    #
    # for ch in line:
    #     if ord(ch) in range(97, 123):
    #         ord_dict[ch] += ch
    #     if ord(ch) in range(65, 91):
    #         ord_dict[chr(ord(ch) + 32)] += ch
    # dic_str = ''
    # for i in range(97, 123):
    #     dic_str += ord_dict[chr(i)]
    # out_str = ''
    # k = 0
    # for ch in line:
    #     if ord(ch) in range(97, 123) or ord(ch) in range(65, 91):
    #         out_str += dic_str[k]
    #         k += 1
    #     else:
    #         out_str += ch
    # print(out_str)

    # str = "abc"
    # str1 = 'bca'
    # str_list = list(str1)
    # str_list.sort()
    # print(''.join(str_list))
    # print(str1)

    # input_str = input().strip()
    # data = input_str.split(' ')
    # dic_len = int(data[0])
    #
    # br_dic = dict()
    # dic = dict()
    # for i in range(dic_len):
    #     s = data[i + 1]
    #     if s in dic.keys():
    #         continue
    #
    #     s_list = list(s)
    #     s_list.sort()
    #     n_s = ''.join(s_list)
    #     if n_s in br_dic.keys():
    #         br_list = br_dic.get(n_s)
    #         br_list.append(s)
    #         br_dic[n_s] = br_list
    #     else:
    #         br_list = []
    #         br_list.append(s)
    #         br_list.sort()
    #         br_dic[n_s] = br_list
    # search = data[dic_len + 1]
    # s_len = int(data[dic_len + 2])
    # s_l = list(search)
    # s_l.sort()
    # s_n_s = ''.join(s_l)
    # if s_n_s in br_dic.keys():
    #     br_list = br_dic.get(s_n_s)
    #     br_list.remove(search)
    #     print(br_list[s_len - 1])

    input_str = input().strip()
    data = input_str.split(' ')
    dic_len = int(data[0])

    dic_list = data[1:dic_len + 1]
    search = data[-2]
    s_len = int(data[-1])
    bro = []

    d = defaultdict(list)

    for i in dic_list:
        d[''.join(sorted(i))].append(i)

    for i in d[''.join(sorted(search))]:
        if i != search:
            bro.append(i)
    if bro and s_len <= len(bro):
        print(sorted(bro)[s_len - 1])

