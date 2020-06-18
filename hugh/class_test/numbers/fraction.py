#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : fraction.py
# Author: hugh
# Date  : 2020/6/4

class Fraction:

    def __init__(self, top, bottom):
        '''
        分数的实现 初始化
        :param top: 分子
        :param bottom: 分母
        '''
        self.num = top
        self.den = bottom

    def show(self):
        '''
        展示的方式
        :return:
        '''
        print(self.num, '/', self.den)

    def gcd(self, m, n):
        if n > m: m,n = n, m
        while m % n != 0:
            m,n = n, m % n
        return n

    def __str__(self):
        '''
        print的返回字符串复写
        :return:
        '''
        return str(self.num) + '/' + str(self.den)

    def __add__(self, other):
        new_num = self.num * other.den + self.den * other.num
        new_den = self.den * other.den
        common = self.gcd(new_num, new_den)
        return Fraction(new_num, new_den)

    def __eq__(self, other):
        first_num = self.num * other.den
        second_num = self.den * other.num
        return first_num == second_num