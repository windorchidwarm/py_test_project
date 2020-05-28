#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
from hugh.spark.test.spark_common.utils_json import JsonUtils
from hugh.spark.test.spark_common.utils_spark import SparkUtils
from hugh.spark.test.spark_common.gen_id import GenId

"""
脚本基础类
    适用于spark和非spark脚本
    
使用说明：
    1、在目标脚本引入该文件的所以内容，
        eg:
            from spark_common.spark_base import *
        
    2、从args_dict字典变量获取传入参数，
        args_dict从submit传入，
        args_dict已经在改代码中初始化，可直接使用：
        eg:
            args_dict.get("参数名",默认值)
        
    3、通过get_spark函数获取spark会话
"""

def get_args():
    """
    获取submit时传入的参数，以json字符串格式
    :return:
    """
    parser = argparse.ArgumentParser(description='app args')
    parser.add_argument( '--app_args', type=str)
    args = parser.parse_args()
    app_args = JsonUtils.toObject(args.app_args ) or {}
    return app_args

def get_spark():
    """
    获取spark会话
    :param params:
    :return:
    """
    app_name = args_dict.get("app_name","app-"+GenId.uuid())
    #从配置文件中获取资源配置
    spark_conf = args_dict.get("spark_source",{})
    return SparkUtils.getSparkSession(app_name,**spark_conf)

args_dict = get_args()



