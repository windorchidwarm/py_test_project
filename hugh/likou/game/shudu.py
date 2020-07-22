#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : shudu.py
# Author: hugh
# Date  : 2020/7/17

from typing import List

def isValidSudoku(board: List[List[str]]) -> bool:
    '''
    判断一个 9x9 的数独是否有效。只需要根据以下规则，验证已经填入的数字是否有效即可。

    数字 1-9 在每一行只能出现一次。
    数字 1-9 在每一列只能出现一次。
    数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。
    :param board:
    :return:
    '''
    row = [[0 for i in range(9)] for i in range(9)]
    line = [[0 for i in range(9)] for i in range(9)]
    three = [[0 for i in range(9)] for i in range(9)]

    for i in range(9):
        for j in range(9):
            val = board[i][j]
            if val in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                if row[i][int(val) - 1] != 0:
                    return False
                else:
                    row[i][int(val) - 1] = 1

                if line[j][int(val) - 1] != 0:
                    return False
                else:
                    line[j][int(val) - 1] = 1

                pre = (i // 3) * 3 + (j // 3)
                if three[pre][int(val) - 1] != 0:
                    return False
                else:
                    three[pre][int(val) - 1] = 1
    return True


def solveSudoku(board: List[List[str]]) -> None:
    '''
    数独游戏
    :param board:
    :return:
    '''
    def get_next(i, j):
        if j == 8:
            return i + 1, 0
        else:
            return i, j + 1

    def solveSudokuMain(board, i, j):
        m, n = get_next(i, j)
        if board[i][j] == '.':
            for k in range(9):
                board[i][j] = str(k + 1)
                if isValidSudoku(board):
                    if j == 8 and i == 8:
                        return True
                    elif solveSudokuMain(board, m, n):
                        return True
            board[i][j] = '.'
            return False
        else:
            if j == 8 and i == 8:
                return True
            else:
                return solveSudokuMain(board, m, n)

    solveSudokuMain(board, 0, 0)
    print(board)



if __name__ == '__main__':
    # data = [
    #   ["5","3",".",".","7",".",".",".","."],
    #   ["6",".",".","1","9","5",".",".","."],
    #   [".","9","8",".",".",".",".","6","."],
    #   ["8",".",".",".","6",".",".",".","3"],
    #   ["4",".",".","8",".","3",".",".","1"],
    #   ["7",".",".",".","2",".",".",".","6"],
    #   [".","6",".",".",".",".","2","8","."],
    #   [".",".",".","4","1","9",".",".","5"],
    #   [".",".",".",".","8",".",".","7","9"]
    # ]
    # data = [
    #     ["8","3",".",".","7",".",".",".","."],
    #     ["6",".",".","1","9","5",".",".","."],
    #     [".","9","8",".",".",".",".","6","."],
    #     ["8",".",".",".","6",".",".",".","3"],
    #     ["4",".",".","8",".","3",".",".","1"],
    #     ["7",".",".",".","2",".",".",".","6"],
    #     [".","6",".",".",".",".","2","8","."],
    #     [".",".",".","4","1","9",".",".","5"],
    #     [".",".",".",".","8",".",".","7","9"]
    # ]
    # print(isValidSudoku(data))
    data = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    print(solveSudoku(data))