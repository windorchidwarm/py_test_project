#!/usr/bin/env python
# -- coding: utf-8 --#
# @Time : 2019/9/19 10:42 
# @Author : Aries 
# @Site :  
# @File : freq_stack.py 
# @Software: PyCharm

class FreqStack:

    def __init__(self):
        self.stack_map = {}
        self.max_seq = 0
        self.group = {}

    def push(self, value):
        f = self.stack_map[value] if value in self.stack_map else 0
        f += 1
        self.stack_map[value] = f
        if f > self.max_seq:
            self.max_seq = f
            self.group[f] = []
            self.group[f].append(value)
        else:
            self.group[f].append(value)


    def pop(self):
        # 获取最大频率
        x = self.group[self.max_seq].pop()
        self.stack_map[x] -= 1
        if len(self.group[self.max_seq]) == 0:
            self.max_seq -= 1
        return x


if __name__ == '__main__':
    print('----------')

    freq_stack = FreqStack()

    int_list = [5, 7, 5, 7, 4, 5]
    for i in int_list:
        freq_stack.push(i)

    for i in range(6):
        print(freq_stack.pop())
