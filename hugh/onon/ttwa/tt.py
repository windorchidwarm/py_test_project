#!/usr/bin/env python
# -- coding: utf-8 --#
# @Time : 2019/12/20 9:25 
# @Author : Aries 
# @Site :  
# @File : tt.py 
# @Software: PyCharm


def calc_one(n):
    count = 0
    while n != 0:
        count += 1
        n = n & (n - 1)
    return count
# 1000 5
# 800 2 0
# 400 5 1
# 300 5 1
# 400 3 0
# 500 2 0

def buy_ticket(data, count):
    # 构造主 副数组
    data_len = len(data)
    for i in range(data_len):
        if data[i]['q'] != 0:
            child = data[data[i]['q'] - 1]['c']
            child.append(data[i])
            data[data[i]['q'] - 1]['c'] = child
    # print(data)
    data_new = []
    for i in range(data_len):
        if data[i]['q'] == 0:
            data_new_zhu = []
            pio = {}
            pio['v'] = data[i]['v']
            pio['j'] = data[i]['j']
            data_new_zhu.append(pio)
            child = data[i]['c']
            if len(child) == 1:
                pio1 = {}
                pio1['v'] = data[i]['v'] + child[0]['v']
                pio1['j'] = data[i]['j'] + child[0]['j']
                data_new_zhu.append(pio1)
            elif len(child) == 2:
                pio1 = {}
                pio1['v'] = data[i]['v'] + child[0]['v']
                pio1['j'] = data[i]['j'] + child[0]['j']
                data_new_zhu.append(pio1)
                pio2 = {}
                pio2['v'] = data[i]['v'] + child[1]['v']
                pio2['j'] = data[i]['j'] + child[1]['j']
                data_new_zhu.append(pio2)
                pio3 = {}
                pio3['v'] = data[i]['v'] + child[0]['v'] + child[1]['v']
                pio3['j'] = data[i]['j'] + child[0]['j'] + child[1]['j']
                data_new_zhu.append(pio3)
            data_new.append(data_new_zhu)
    data_new_len = len(data_new)
    n = [0 for zero in range(count + 1)]
    for i in range(data_new_len):
        for j in range(count, -1, -1):
                for k in range(len(data_new[i])):
                    if j >= data_new[i][k]['v']:
                        n[j] = max(n[j], n[j - data_new[i][k]['v']] + data_new[i][k]['j'])


def base_knapsack(data, count):
    data_len = len(data)
    m = [[0 for a in range(count + 1)] for b in range(data_len + 1)]
    print(m)
    for i in range(1, data_len + 1):
        for j in range(count + 1):
            if j < data[i - 1]['v']:
                m[i][j] = m[i - 1][j]
            else:
                m[i][j] = max(m[i - 1][j], m[i - 1][j - data[i - 1]['v']] + data[i - 1]['j'])
        print(m)

    # n = [0] * (count + 1)
    # print(data)
    # for i in range(data_len):
    #     for j in range(count, data[i]['v'] - 1, -1):
    #         if j >= data[i]['v']:
    #             n[j] = max(n[j], n[j - data[i]['v']] + data[i]['j'])
    #     print(n)
    # print(n)



if __name__ == '__main__':
    # s = input()
    # s_list = list(s)
    # s_list.reverse()
    # print(''.join(s_list))
    # n = int(input())
    # data = []
    # for i in range(n):
    #     data.append(input())
    # data.sort()
    # for i in range(n):
    #     print(data[i])

    # n = int(input())
    # print(calc_one(n))

    s = input().split(' ')
    N,m = int(s[0]), int(s[1])

    data = []
    for i in range(m):
        ss = input().split(' ')
        per = {}
        per['v'] = int(ss[0])
        per['j'] = int(ss[1]) * per['v']
        per['q'] = int(ss[2])
        per['c'] = []
        data.append(per)
    # base_knapsack(data, N)
    buy_ticket(data, N)