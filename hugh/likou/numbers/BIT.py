#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : BIT.py
# Author: chen
# Date  : 2020-04-24

class BIT:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)


    @staticmethod
    def lowbit(x):
        return x & (-x)


    def query(self, x):
        ret = 0
        while x > 0:
            ret += self.tree[x]
            x -= BIT.lowbit(x)
        return ret


    def update(self, x):
        while x <= self.n:
            self.tree[x] += 1
            x += BIT.lowbit(x)
