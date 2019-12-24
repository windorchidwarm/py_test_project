#!/usr/bin/env python
# -- coding: utf-8 --#
# @Time : 2019/12/24 16:02 
# @Author : Aries 
# @Site :  
# @File : maze_pro.py 
# @Software: PyCharm



def maze(data, n, m):
    '''
    迷宫问题
    从0,0 到n,m
    :param data:
    :param n:
    :param m:
    :return:
    '''
    def move_track(x, y):
        data[x][y] = 1
        msg = '(' + str(x) + ',' + str(y) + ')'
        data_routs.append(msg)

        if x == n - 1 and y == m - 1:
            return True

        res = False

        if (y + 1 < m) and data[x][y + 1] == 0 and (not res):
            res = move_track(x, y + 1)
        if (x + 1 < n) and data[x + 1][y] == 0 and (not res):
            res = move_track(x + 1, y)
        if (x - 1 >= 0) and data[x - 1][y] == 0 and (not res):
            res = move_track(x - 1, y)
        if (y - 1 >= 0) and data[x][y - 1] == 0 and (not res):
            res = move_track(x, y - 1)


        if res:
            return True
        else:
            del data_routs[-1]
            return False
    data_routs = []
    # data_routs.append('(0,0)')
    move_track(0, 0)
    return data_routs




if __name__ == '__main__':
    print('--------------')

    nums = list(map(int, input().strip().split(' ')))

    data = [[0 for i in range(nums[1])] for j in range(nums[0])]
    for i in range(nums[0]):
        row = list(map(int, input().strip().split(' ')))
        data[i] = row
    print(maze(data, nums[0], nums[1]))
    print(data)