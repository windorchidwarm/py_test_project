#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : divide.py
# Author: chen
# Date  : 2020-04-26

import math

def divide(dividend: int, divisor: int) -> int:
    '''

    :param self:
    :param dividend:
    :param divisor:
    :return:
    '''
    def div(divid, divsor):
        if divid < divsor:
            return 0
        count = 1
        d_sor = divsor
        while d_sor + d_sor < divid:
            count += count
            d_sor += d_sor
        return count + div(divid - d_sor, divsor)
    if divisor == 0: return None
    if dividend == 0: return 0
    if divisor == 1: return dividend

    sign = 1
    if (divisor > 0 and dividend < 0) or (divisor < 0 and dividend > 0):
        sign = -1
    divisor = divisor if divisor > 0 else -divisor
    dividend = dividend if dividend > 0 else -dividend

    min_data = -2 ** 31
    if divisor == -1:
        if dividend > min_data:
            return -dividend
        else:
            return 2 ** 31 - 1
    res = div(dividend, divisor)
    if sign == -1:
        res = -res
    if res > 2 ** 31 - 1:
        res = 2 ** 31 - 1
    if res < -2 ** 31:
        res = -2 ** 31
    return res