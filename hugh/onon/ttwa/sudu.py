#!/usr/bin/env python
# -- coding: utf-8 --#
# @Time : 2019/12/24 17:25 
# @Author : Aries 
# @Site :  
# @File : sudu.py 
# @Software: PyCharm


def sudu(data):
    '''
    数独 0为待填充数字
    :param data:
    :return:
    '''
    def check(x, y, key):

        # 横列
        for i in range(9):
            if i != y:
                if data[x][i] == key:
                    return False
            if i != x:
                if data[i][y] == key:
                    return False
        # 九宫格
        x_x = (x // 3) * 3

        y_y = (y // 3) * 3
        for i in range(3):
            for j in range(3):
                if not(x_x + i == x and y_y + j == y):
                    if data[x_x + i][y_y + j] == key:
                        return False
        return True

    def next_x_y(x, y):
        if y == 8:
            return x + 1, 0
        else:
            return x, y + 1

    def DFS(data, x, y):
        # print(x, y)
        # print(data)
        print(data)
        if x > 8 or y > 8:
            return True

        if data[x][y] != 0:
            x,y = next_x_y(x, y)
            return DFS(data, x, y)
        else:
            for i in range(1, 10):
                # print(data[x], x, y)
                if check(x, y, i):
                    data[x][y] = i
                    n_x, n_y = next_x_y(x, y)
                    if DFS(data, n_x, n_y):
                        return True
                    data[x][y] = 0
            return False

    DFS(data, 0, 0)
    return data



if __name__ == '__main__':
    '''
    0 9 2 4 8 1 7 6 3
    4 1 3 7 6 2 9 8 5
    8 6 7 3 5 9 4 1 2
    6 2 4 1 9 5 3 7 8
    7 5 9 8 4 3 1 2 6
    1 3 8 6 2 7 5 9 4
    2 7 1 5 3 8 6 4 9
    3 8 6 9 1 4 2 5 7
    0 4 5 2 7 6 8 3 1
    '''
    print('---------------')
    data = []
    for i in range(9):
        raw = list(map(int, input().strip().split(' ')))
        data.append(raw)
    # print(data)
    # data = [[0, 9, 2, 4, 8, 1, 7, 6, 3], [4, 1, 3, 7, 6, 2, 9, 8, 5], [8, 6, 7, 3, 5, 9, 4, 1, 2], [6, 2, 4, 1, 9, 5, 3, 7, 8], [7, 5, 9, 8, 4, 3, 1, 2, 6], [1, 3, 8, 6, 2, 7, 5, 9, 4], [2, 7, 1, 5, 3, 8, 6, 4, 9], [3, 8, 6, 9, 1, 4, 2, 5, 7], [0, 4, 5, 2, 7, 6, 8, 3, 1]]
    n_data = sudu(data)
    for i in range(9):
        msg = ''
        for j in range(9):
            msg += str(n_data[i][j]) + ' '
        msg = msg[:-1]
        print(msg)