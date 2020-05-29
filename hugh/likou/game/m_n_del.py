#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : m_n_del.py
# Author: BBD
# Date  : 2020/5/29



def m_n_del(n:int, m:int):
    '''
    据说著名历史学家Josephus（约瑟夫）经历过以下故事：在罗马人占领乔塔帕特后，
    40个犹太人和Josephus躲在一个山洞中。40个犹太人决定宁死也不被敌人抓到，于是决定集体自杀。
    大家经过讨论决定了一个自杀方式，41个人围成一个圆圈，由第1个人开始报数，每报数到3的人就必须自杀，
    然由再由下一个人重新开始报数，直到所有人都自杀身亡为止。
    最后一个人最初的编号
    f(1) = 0
    f(2) = (f(1) + m) % 2
    f(n) = [f(n-1) + m ] % n
    :param m:
    :param n:
    :return:
    '''
    print(n, m)
    if n == 1:
        return 0
    else:
        return (m_n_del(n-1, m) + m) % n

if __name__ == '__main__':
    '''
    '''
    print(m_n_del(8, 3))