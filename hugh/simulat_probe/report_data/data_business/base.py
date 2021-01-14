#! /usr/bin/python3
# -*- coding: utf-8 -*-

"""
@Author: My_Jie
@File: base.py
@Time: 2021/1/8-15:03
"""


class CheckData:

    @staticmethod
    def yes_funcs(*, temp_data, func_name):
        """
        判断模板中的字段有没有相应的函数可调用，没有就抛错
        :param temp_data
        :param func_name
        :return:
        """
        for k in temp_data:
            if k not in func_name:
                raise KeyError(f'funcs中没有调用这个字段的调用：{k} 请设置')

    @staticmethod
    def funcs(*, temp_data, funcs):
        """
        通过函数名称匹配字典模板，匹配上就添加到列表，没有就pass
        :param temp_data:
        :param funcs:
        :return:
        """
        return [func for func in funcs if func.__name__ in temp_data]
