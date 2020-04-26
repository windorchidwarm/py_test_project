#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : spark_session.py
# Author: chen
# Date  : 2020-04-16


from pyspark import SparkContext,SparkConf
from hugh.spark.test.second import spark_config
from pyspark.sql import SparkSession
import json
from pyspark.sql.types import Row
from pyspark.rdd import PipelinedRDD

from operator import add
import re

def get_session():
    conf = SparkConf().setMaster('local').setAppName('first')
    sc = SparkContext(conf=conf)
    return sc

def get_spark():
    conf = SparkConf().setMaster('local').setAppName('first')

    spark = SparkSession.builder \
        .appName('first') \
        .config(conf=conf) \
        .enableHiveSupport() \
        .getOrCreate()
    return spark


def not_contain_chinese(data):
    '''
    判断是否不包含中文
    :param data:
    :return:
    '''
    exp = re.compile('[^\u4e00-\u9fa5]+')
    res = exp.fullmatch(data)
    print(res)
    if res is not None:
        return False
    else:
        return True

def test_opt(data):
    print(data)
    print(not_contain_chinese(data))
    data += '1'
    return data


def wind_some(sc):
    test_rdd = sc.textFile(r'C:\Users\yhchen\Desktop\test\tmp\434.txt').cache()
    data = test_rdd.flatMap(lambda value: value.split(' ')).foreach(print)

    num_rdd = sc.parallelize([i for i in range(10)])
    print(num_rdd.filter(lambda x: x % 2 == 0).reduce(add))


def wind_some2(sc):
    path = r'C:\Users\BBD\Desktop\test\test\test2\tt.txt'
    test_rdd = sc.textFile(path)
    test_rdd.map(test_opt).collect()

    csv_path = r'C:\Users\BBD\Desktop\test\tmp\Cshl0V1SGTmALptAAAAi230xNmU755.csv'
    test_rdd_csv = sc.textFile(csv_path)
    print('---------------')
    print(type(test_rdd_csv))
    df = sc.textFile
    print(df)


def groupby_map(row):
    print(type(row))
    row_dict = row.asDict()
    print(row_dict)
    print(type(row_dict))

    return row

    # value = json.loads(data)
    # print(value)
    # if '编号' in value.keys():
    #     return (
    #         value['编号'],
    #         data.value)
    # else:
    #     return ('null', 'null')





def spark_some(spark):
    def df_map(data):
        print(data)
        (key1, key2 ), data2 = data
        print(type(data))
        print(key1, key2, data2)
        data3 = {}
        data3['kye1'] = key1
        data3['key2'] = key2
        for mm in data2:
            print(mm)
        print(type(data2))
        return data3
    csv_path = r'C:\Users\BBD\Desktop\test\tmp\Cshl0V1SGTmALptAAAAi230xNmU755.csv'
    df = spark.read.csv(csv_path, header=True, inferSchema=True, sep='\u0001')
    print(df)
    print(type(df.rdd))
    df_new = df.rdd.map(
        lambda r: ((r['商场名称'], r['商场ID']), r.asDict())
    ).groupByKey(
    ).map(
        df_map
    )
    print(df_new)
    print(type(df_new))
    df_new_df = df_new.toDF()
    print(df_new_df.schema)
    print(df_new_df)


if __name__ == '__main__':
    '''
    spark session 相关的测试
    '''
    # sc = get_session()
    # print(sc)
    # wind_some2(sc)
    spark = get_spark()
    print(spark)
    spark_some(spark)
    # wind_some(sc)