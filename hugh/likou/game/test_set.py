#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : test_set.py
# Author: BBD
# Date  : 2020/6/3


if __name__ == '__main__':
    '''
    '''

    lset = {1 ,2 ,3}
    rset = {2,3,4}
    print(lset | rset)
    print(lset & rset)
    print(lset - rset)
    print(lset <= rset)

    print(lset.union(rset))
    print(lset.intersection(rset))
    print(lset.difference(rset))
    print(lset.add(4))
    print(lset)
    print(rset.issubset(lset))
    # print(lset.intersection_update(rset))
    # print(lset)