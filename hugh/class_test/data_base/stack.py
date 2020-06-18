#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : stack.py
# Author: hugh
# Date  : 2020/6/17

class Stack:

    def __init__(self):
        '''
        栈的数据结构 后进先出
        '''
        self.items = []

    def isEmpty(self):
        '''
        判断是否为空
        :return:
        '''
        return self.items == []

    def push(self, item):
        '''
        加入一个元素
        :param item:
        :return:
        '''
        self.items.append(item)

    def pop(self):
        '''
        空栈出栈跑出一次
        移除并返回最后一个元素
        :return:
        '''
        if len(self.items) == 0:
            raise Exception('空栈')
        return self.items.pop()

    def peek(self):
        '''
        空栈出栈跑出一次
        返回但并部移除最后一个元素
        :return:
        '''
        if len(self.items) == 0:
            raise Exception('空栈')
        return self.items[-1]

    def size(self):
        '''
        返回len的大小
        :return:
        '''
        return len(self.items)

    def __str__(self):
        '''
        复写str的方法
        :return:
        '''
        return str(self.items)
