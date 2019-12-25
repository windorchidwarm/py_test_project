#!/usr/bin/env python
# -- coding: utf-8 --#
# @Time : 2019/12/25 14:14 
# @Author : Aries 
# @Site :  
# @File : measure.py 
# @Software: PyCharm

def insert_num(x, y, num_list):
    p_x, p_y = [i for i in num_list[-1]]
    diff = x - p_x
    for i in range(p_x + 1, x):
        val = p_y + int((y - p_y)/ diff) * (i - p_x)
        num_list.append([i, val])


def measure(nums, sig):
    '''
    信号测量的结果包括测量编号和测量值。存在信号测量结果丢弃及测量结果重复的情况。



      1.测量编号不连续的情况，认为是测量结果丢弃。对应测量结果丢弃的情况，需要进行插值操作以更准确的评估信号。

      采用简化的一阶插值方法,由丢失的测量结果两头的测量值算出两者中间的丢失值。

      假设第M个测量结果的测量值为A，第N个测量结果的测量值为B。则需要进行(N-M-1)个测量结果的插值处理。进行一阶线性插值估计的第N+i个测量结果的测量值为A+( (B-A)/(N-M) )*i  (注：N的编号比M大。)

      例如：只有测量编号为4的测量结果和测量编号为7的测量结果，测量值分别为4和10

        则需要补充测量编号为5和6的测量结果。

         其中测量编号为5的测量值=4 + ((10-4)/(7-4))*1 = 6

         其中测量编号为6的测量值=4 + ((10-4)/(7-4))*2 = 8



      2.测量编号相同，则认为测量结果重复，需要对丢弃后来出现的测量结果。


    :param nums:
    :param sig:
    :return:
    '''
    while True:
        try:
            line = input().strip()
            if line == '':
                break
            m, n = [int(i) for i in line.split(' ')]

            num_list = []
            for i in range(m):
                x, y = [int(i) for i in input().strip().split(' ')]

                if len(num_list) > 0:
                    if num_list[-1][0] == x:
                        continue
                    elif num_list[-1][0] + 1 < x:
                        insert_num(x, y, num_list)
                        num_list.append([x, y])
                    else:
                        num_list.append([x, y])
                else:
                    num_list.append([x, y])
            for data in num_list:
                print(str(data[0]) + ' ' + str(data[1]))
        except:
            break


def tree_list():
    while True:
        try:
            line = input().strip()
            if line == '':
                break

            num = int(line)
            num_list = []
            num_list.append(int(input().strip()))
            for i in range(num - 1):
                x,y = [int(i) for i in input().strip().split(' ')]
                index = num_list.index(y)
                num_list.insert(index + 1, x)

            d_val = int(input().strip())
            # index = num_list.index(d_val)

            num_list.remove(d_val)

            msg = ''
            for val in num_list:
                msg += str(val) + ' '
            msg = msg[:-1]
            print(msg)
        except:
            break


if __name__ == '__main__':
    print('------')
    tree_list()

