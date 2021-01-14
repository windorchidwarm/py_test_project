#! /usr/bin/python3
# -*- coding: utf-8 -*-

"""
@Author: My_Jie
@File: main.py
@Time: 2021/1/8-15:42
"""

from hugh.simulat_probe.report_data.data_temp.type_one import TempTypeOne
from hugh.simulat_probe.report_data.data_temp.type_two import TempTypeTwo
from hugh.simulat_probe.report_data.data_temp.type_three import TempTypeThree
from hugh.simulat_probe.report_data.data_business.type_one import BusinessTypeOne
from hugh.simulat_probe.report_data.data_business.type_two import BusinessTypeTwo
from hugh.simulat_probe.report_data.data_business.type_three import BusinessTypeThree
from hugh.simulat_probe.report_data.data_assemble.assemble import Assemble
from hugh.simulat_probe.common.res_url import ResUrl


def run():
    """
    主函数入口
    :return:
    """
    # 获取模板数据
    temp_type_one = TempTypeOne().temp_data
    temp_type_two = TempTypeTwo().temp_data
    temp_type_three = TempTypeThree().temp_data
    # 获取按规则生成后的数据
    business_type_one = BusinessTypeOne(temp_type_one).probe_data()
    business_type_two = BusinessTypeTwo(temp_type_two).probe_data()
    business_type_three = BusinessTypeThree(temp_type_three).probe_data()
    # 获取组装好的上报list
    report_data = Assemble(business_type_one, business_type_two, business_type_three).single_element()
    print(report_data)
    # http请求
    res = ResUrl(host='10.0.0.184:8082/cbav2', path='/dialTest/issue')
    res.post(report_data)


if __name__ == '__main__':
    run()
