#!/usr/bin/env python
# -- coding: utf-8 --#
# @Time : 2019/12/28 13:19 
# @Author : Aries 
# @Site :  
# @File : exam_test.py 
# @Software: PyCharm
import sys

if __name__ == '__main__':
    '''
    N棵桃树 每棵Ni桃 H小时吃完
    每次吃的桃子数要么这颗树吃完等下一棵，要么吃K个
    问H小时吃完K的最小值
    '''
    while True:
        line = sys.stdin.readline().strip()
        if line == '':
            break
        try:
            data = list(map(int, line.split(' ')))
            H = data[-1]
            tao = data[:-1]
            N = len(tao)
            if N > H or N == 0 or (0 in tao):
                print(-1)
            elif N == H:
                print(max(tao))
            else:
                per = int(H / N)
                k = max(int(min(tao) / per), 1)
                while k <= max(tao):
                    hours = 0
                    res = True
                    for val in tao:
                        if val % k == 0:
                            hours += int(val / k)
                        else:
                            hours += int(val /  k) + 1
                        if hours > H:
                            res = False
                            break
                    if res:
                        break
                    else:
                        k += 1
                print(k)
        except:
            print(-1)
            break