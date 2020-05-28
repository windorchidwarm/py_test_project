#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime, time

"""
qyxx_basic表相关通用函数
"""

def year_level(esdate, opento):
    """
    经营年限，保留2位小数
    :param esdate:  qyxx_basic  注册时间
    :param opento:  qyxx_basic  经营至
    :return:
    """
    to_date = datetime.date.today()
    try:
        # datatime.date 没有 strptime方法
        opento1 = datetime.datetime.strptime(opento, "%Y-%m-%d").date()
        if opento1 < to_date:
            to_date = opento1
    except:
        pass
    return round((to_date - esdate).days / 365, 2)