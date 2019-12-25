#!/usr/bin/env python
# -- coding: utf-8 --#
# @Time : 2019/12/25 16:06 
# @Author : Aries 
# @Site :  
# @File : cal_num.py 
# @Software: PyCharm


import re

def cal_num(cal_str):
    '''
    简单四则运算
    :param cal_str:
    :return:
    '''
    cal_list = []
    print(cal_str)
    cal_str = cal_str.replace('[', '(').replace('{', '(').replace(']', ')').replace('}', ')').replace(' ', '')
    print(cal_str)
    num = ''
    for i in cal_str:
        if re.match('[0-9]', i):
            num += i
        elif i == ' ':
            continue
        else:
            if i == '-' and num == '' and cal_list[-1] == '(':
                num += i
            else:
                cal_list.append(num)
                cal_list.append(i)
                num = ''
    if len(num) > 0:
        cal_list.append(num)
    print(cal_list)

    num_list = []
    stack = []
    for val in cal_list:
        if val == '(':
            stack.append(val)
        elif val == ')':
            tmp = stack.pop()
            while not (tmp == '('):
                num_list.append(tmp)
                tmp = stack.pop()
        elif val == '*' or val == '/':
            while len(stack) > 0:
                tmp = stack[-1]
                if tmp == '*' or tmp == '/':
                    stack.pop()
                    num_list.append(tmp)
                else:
                    break
            stack.append(val)
        elif val == '+' or val == '-':

            while len(stack) > 0:
                tmp = stack[-1]
                if tmp != '(':
                    stack.pop()
                    num_list.append(tmp)
                else:
                    break
            stack.append(val)
        else:
            num_list.append(val)
    while len(stack) > 0:
        num_list.append(stack.pop())

    new_stack = []
    for val in num_list:
        print(new_stack, val)
        if val in ['+', '-', '*', '/']:
            num2 = new_stack.pop()
            num1 = new_stack.pop()
            if val == '+':
                new_stack.append(num1 + num2)
            elif val == '-':
                new_stack.append(num1 - num2)
            elif val == '*':
                new_stack.append(num1 * num2)
            elif val == '/':
                new_stack.append(num1 / num2)
        else:
            new_stack.append(int(val))
        print(num_list)

    print(new_stack[0])



if __name__ == '__main__':
    '''
    [‘0’-‘9’],‘+’,‘-’, ‘*’,‘/’ ,‘(’， ‘)’,‘[’, ‘]’,‘{’ ,‘}’。
    3+2*{1+2*[-4/(8-6)+7]}
    '''
    cal = '3-10+(0+(10+5+3)-10)'
    cal_num(cal)
