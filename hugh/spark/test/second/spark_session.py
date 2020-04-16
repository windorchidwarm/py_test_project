#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : spark_session.py
# Author: chen
# Date  : 2020-04-16


from pyspark import SparkContext,SparkConf
from hugh.spark.test.second import spark_config


def get_session():
    conf = SparkConf().setMaster('local').setAppName('first')
    sc = SparkContext(conf=conf)
    return sc


if __name__ == '__main__':
    '''
    spark session 相关的测试
    '''
    sc = get_session()
    print(sc)
    test_rdd = sc.textFile(r'C:\Users\yhchen\Desktop\test\tmp\434.txt').cache()
    data = test_rdd.flatMap(lambda value: value.split(' ')).foreach(print)