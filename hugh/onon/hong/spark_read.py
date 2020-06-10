#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : spark_read.py
# Author: hugh
# Date  : 2020/5/7


import json,os
from pyspark import SparkContext,SparkConf
from pyspark.sql import SparkSession

from hugh.spark.test.second import spark_config

def read_file_by_line(file_path, line_num=None,
                      skip_empty_line=True, strip=True):

    content_list = list()
    count = 0
    with open(file_path, 'r', encoding='utf-8') as f:
        line = f.readline()
        while True:
            if line == '':  # 整行全空，说明到文件底
                break
            if line_num is not None:
                if count >= line_num:
                    break

            if line.strip() == '':
                if skip_empty_line:
                    count += 1
                    line = f.readline()
                else:
                    try:
                        cur_obj = json.loads(line.strip())
                        content_list.append(cur_obj)
                    except:
                        if strip:
                            content_list.append(line.strip())
                        else:
                            content_list.append(line)
                    count += 1
                    line = f.readline()
                    continue
            else:
                try:
                    cur_obj = json.loads(line.strip())
                    content_list.append(cur_obj)
                except:
                    if strip:
                        content_list.append(line.strip())
                    else:
                        content_list.append(line)
                count += 1
                line = f.readline()
                continue

    return content_list


def row_to_string(data):
    return data['value'].strip()


def read_file_by_line2(file_path, spark):
    data = spark.read.text(file_path)
    print(data)
    data_list = data.collect()
    line_list = []
    for data in data_list:
        line_list.append(data['value'].strip())
    return line_list



def get_spark():
    conf = SparkConf().setMaster('local').setAppName('first')

    spark = SparkSession.builder \
        .appName('first') \
        .config(conf=conf) \
        .enableHiveSupport() \
        .getOrCreate()
    return spark



if __name__ == '__main__':
    DIR_PATH = os.path.dirname(__file__)
    print(read_file_by_line(os.path.join(DIR_PATH, 'china_location.txt'), strip=False))
    print(read_file_by_line2(os.path.join(DIR_PATH, 'location_map.txt'), get_spark()))