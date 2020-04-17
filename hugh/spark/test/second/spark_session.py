#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : spark_session.py
# Author: chen
# Date  : 2020-04-16


from pyspark import SparkContext,SparkConf
from hugh.spark.test.second import spark_config

from operator import add


def get_session():
    conf = SparkConf().setMaster('local').setAppName('first')
    sc = SparkContext(conf=conf)
    return sc

def wind_some(sc):
    test_rdd = sc.textFile(r'C:\Users\yhchen\Desktop\test\tmp\434.txt').cache()
    data = test_rdd.flatMap(lambda value: value.split(' ')).foreach(print)

    num_rdd = sc.parallelize([i for i in range(10)])
    print(num_rdd.filter(lambda x: x % 2 == 0).reduce(add))


def wind_some2(sc):
    path = r'C:\Users\yhchen\Desktop\test\tmp\434.txt'
    test_rdd = sc.textFile(path)


if __name__ == '__main__':
    '''
    spark session 相关的测试
    '''
    sc = get_session()
    print(sc)
    wind_some2(sc)
    # wind_some(sc)