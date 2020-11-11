#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : hive_utils.py
# Author: hugh
# Date  : 2020/11/11

from pyspark.sql import SparkSession
from pyspark.conf import SparkConf


def get_spark():
    return SparkSession\
        .builder\
        .appName('test_hive')\
        .enableHiveSupport()\
        .getOrCreate()


def current_partition(table, spark, data_valid=False):
    """
    获取最近分区
    :param table: 查询的表
    :param spark: spark session
    :param data_valid: 是否校验数据条数
    :return:
    """
    partitions = spark.sql("show partitions {table}".format(table=table)).collect()
    dt = sorted([partition.partition[3:] for partition in partitions], reverse=True)[0]
    if data_valid and len(spark.sql("select 1 from {table} where dt={dt} limit 10".format(
        table=table,
        dt=dt
    )).rdd.collect()) < 10:
        dt = sorted([partition.partition[3:] for partition in partitions], reverse=True)[1]
    return dt
