#!/usr/bin/env python
# -- coding: utf-8 --#
# @Time : 2019/12/23 18:24 
# @Author : Aries 
# @Site :  
# @File : some.py 
# @Software: PyCharm


import re
import math
import sys
import time

if __name__ == '__main__':
    # format格式对于数字的用法
    print('{:032}'.format(8))
    print(3 // 3)

    test_str = 'this我ren神'
    print(len(test_str))

    num_list = []
    num_list.append([1, 2])
    num_list.append([2, 4])
    num_list.append([1, 5])
    print(num_list)

    data = []
    data.append(('a', 3))
    data.append(('b', 5))
    data.append(('c', 4))
    data.append(('d', 3))
    new_data = sorted(data, key = lambda x:x[1], reverse = True)
    print(new_data)

    print(0 and 1)
    print(0 and 0)
    print(1 and 1)
    print(1 and True)
    print(0 and True)

    line = 'gqpj /lrl d:\ a:\ c:\ /nkb'
    res = True
    mes = ''
    l = []
    for val in line:
        if val == ' ':
            if res:
                if mes != '':
                    l.append(mes)
                    mes = ''
            else:
                mes += val
        elif val == '"':
            if not res:
                l.append(mes)
                mes = ''
                res = True
            else:
                res = False
        else:
            mes += val
    if mes != '':
        l.append(mes)
    print(len(l))
    for val in l:
        print(val)
    print(99999999999999999999999999999999999999999999999999 + 1)
    print('234'.endswith('3'))

    m = {}
    m['a'] = 1
    m['f'] = 3
    m['e'] = 3
    m['d'] = 1
    print(list(m.items()))
    l = list(m.items())
    l = sorted(l, key = lambda x:(0 - x[1], x[0]), reverse=True)
    l.reverse()
    print(l)


    num = float(12)
    t = 2.0
    while math.fabs(t * t * t - num) > 0.01:
        t =t - (t * t * t * 0.1 - num * 0.1) / (3 * t * t)
        print(t)
    print(t)
    print()
    print('%.1f' % t)
    n = 6
    print(n >> 1)

    print('9xx'.startswith(('[0-9]', '-')))
    print(bool(re.match('^[+\-]?[1-9]\d*', '  0000000000012345678'.strip())))
    dd = re.match('^-?[0-9]\d*', '  0000000000012345678'.strip())
    print(dd.group())
    print(bool(dd))
    print('3' in '[0-9]')
    print(sys.maxsize)
    print(time.ctime())
    print((2 ** 32) -1)
    print(time.ctime())
    print((2 << 31) -1)
    print(time.ctime())



    # num = 0
    # for i in test_str:
    #     if re.match('[\x00-\xff]', i):
    #         print(i, 1)
    #     else:
    #         print(i ,2)

    # line = ''
    # msg = ''
    # count = 0
    # for i in test_str:
    #     if re.match('[\x00-\x99]', i):
    #         if (count + 1 > num):
    #             break
    #         else:
    #             count += 1
    #             msg += i
    #     else:
    #         if (count + 2 > num):
    #             break
    #         else:
    #             count += 2
    #             msg += i
    # print(msg)

    # mm = {}
    # mm[0, 0] = True
    # mm[0, 1] = False
    # if (0, 0) in mm and mm[0, 0] : print('1')
    # if mm[0, 1] : print('2')
    # if (0, 2) in mm and mm[0, 2] : print('3')