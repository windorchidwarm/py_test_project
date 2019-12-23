#!/usr/bin/env python
# -- coding: utf-8 --#
# @Time : 2019/12/20 18:00 
# @Author : Aries 
# @Site :  
# @File : dd.py 
# @Software: PyCharm

import sys

if __name__ == '__main__':
    # s = r'E:\V1R2\product\fpgadrive.c'
    # ss = s.split('\\')
    # file_path = ss[len(ss) - 1]
    # print(file_path)
    # print(s.index('\\'))
    # pp = '12345678901234567'
    # pp = pp[-16:]
    # print(pp)
    #
    # ll = []
    # ll.append('dd')
    # print(ll[-8:])

    file_list = []
    file_dic = dict()
    while True:
        try:
            line = sys.stdin.readline().strip()
            if line == '':
                break
            err_data = line.split('\\')[-1]
            file_path = err_data.split(' ')[0]
            if len(file_path) > 16:
                file_path = file_path[-16:]
            line_code = err_data.split(' ')[1]

            key = file_path + '_' + line_code
            if key in file_dic.keys():
                res = file_dic.get(key)
                res['count'] += 1
                file_dic[key] = res
            else:
                file_list.append(key)
                res = {}
                res['count'] = 1
                res['name'] = file_path
                res['line'] = line_code
                file_dic[key] = res
        except:
            break
    print(file_list)
    print(file_dic)
    keys = file_list[-8:]
    for key in keys:
        res = file_dic.get(key)
        print(res['name'] + ' ' + res['line'] + ' ' + str(res['count']))
