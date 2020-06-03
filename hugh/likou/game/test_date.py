#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : test_date.py
# Author: BBD
# Date  : 2020/6/3

import datetime, time

def get_date(version, days=7):
    dt_date = time.strptime(version, '%Y%m%d')
    delta = datetime.timedelta(days=days)
    dt_date_time = datetime.date(dt_date.tm_year, dt_date.tm_mon, dt_date.tm_mday)
    pre_date = dt_date_time - delta
    p_date_str = pre_date.strftime('%Y%m%d')
    return p_date_str

if __name__ == '__main__':
    get_date('20200602')