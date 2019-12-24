#!/usr/bin/env python
# -- coding: utf-8 --#
# @Time : 2019/12/24 9:20 
# @Author : Aries 
# @Site :  
# @File : snake_metris.py 
# @Software: PyCharm


import math


def snake_metri(num):
    '''
    输入 4  输出
    1 3 6 10
    2 5 9
    4 8
    7
    :param num:
    :return:
    '''
    for i in range(num):
        base = 1 + int((i) * (i + 1) / 2) if i > 0 else 1
        msg = str(base) + ' '
        for j in range(1, num - i):
            msg += str(int(base + (j * (i + 2 + i + 2 + j - 1) / 2))) + ' '
        msg = msg[0:-1]
        print(msg)


def sport_line(hight, num):
    '''
    高度 hight
    第num次落地的距离和反弹高度
    :param hight:
    :param num:
    :return:
    '''
    if num == 1:
        return hight, hight/2
    else:
        return hight * 3 - hight / math.pow(2, num - 2), hight / math.pow(2, num)


if __name__ == '__main__':
    print('----')
    snake_metri(5)
    x,y = sport_line(38801, 5)
    print('%g' % x)
    print('%g' % y)
    print(x, y)