#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : k_paishou_game.py
# Author: hugh
# Date  : 2020/4/30


def k_paishou_game(n:int, m:int, k:int) -> int:
    '''
     n个人站成一行玩一个报数游戏。所有人从左到右编号为1到n。游戏开始时，最左边的人报1，他右边的人报2，编号为3的人报3，等等。当编号为n的人（即最右边的人）报完n之后，轮到他左边的人（即编号为n-1的人）报n+1，然后编号为n-2的人报n+2，以此类推。当最左边的人再次报数之后，报数方向又变成从左到右，依次类推。
       为了防止游戏太无聊，报数时有一个特例：如果应该报的数包含数字7或者是7的倍数，他应当用拍手代替报数。下表是n=4的报数情况（X表示拍手）。当编号为3的人第4次拍手的时候，他实际上数到了35。
       给定n，m和k，你的任务是计算当编号为m的人第k次拍手时，他实际上数到了几。
    :param n:
    :param m:
    :param k:
    :return:
    '''
    if n == 0 or m == 0 or k == 0: return 0

    cur_m = 1
    cur_k = 0
    flag = 1
    cur_num = 1
    while cur_k < k:
        if cur_m <= 1:
            flag = 1
        if cur_m >= n:
            flag = -1

        cur_m += flag
        cur_num += 1
        if cur_m == m:
            if cur_num % 7 == 0 or '7' in str(cur_num):
                cur_k += 1
    return cur_num



if __name__ == '__main__':
    print(k_paishou_game(4, 3, 1))
