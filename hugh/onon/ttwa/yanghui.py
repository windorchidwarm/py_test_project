#!/usr/bin/env python
# -- coding: utf-8 --#
# @Time : 2019/12/26 10:31 
# @Author : Aries 
# @Site :  
# @File : yanghui.py 
# @Software: PyCharm


def sanjiao_res(n):
    '''
    题目描述
                1

             1  1  1

          1  2  3  2  1

       1  3  6  7  6  3  1

    1  4  10 16 19  16 10  4  1

    以上三角形的数阵，第一行只有一个数1，以下每行的每个数，是恰好是它上面的数，左上角数到右上角的数，3个数之和（如果不存在某个数，认为该数就是0）。

    求第n行第一个偶数出现的位置。如果没有偶数，则输出-1。例如输入3,则输出2，输入4则输出3。
    :param n:
    :return:
    '''
    if n < 2:
        return -1
    data = []
    data.append([1])
    data.append([1,1])
    for i in range(2, n):
        raw = []
        for j in range(0, i + 1):
            if j == i:
                num = raw[-2]
                raw.append(num)
            else:
                num1 = data[i - 1][j - 2] if (j - 2 >= 0) else 0
                num2 = data[i - 1][j - 1] if (j - 1 >= 0) else 0
                num3 = data[i - 1][j]
                raw.append(num1 + num2 + num3)
        print(raw)
        data.append(raw)
    res = -1
    print(data)
    for i in range(len(data[n - 1])):
        if data[n - 1][i] % 2 == 0:
            res = (i + 1)
            break
    return res


if  __name__ == '__main__':
    while True:
        try:
            line = input().strip()
            if line == '':
                break
            n = int(line)

            print(sanjiao_res(n))
        except:
            break