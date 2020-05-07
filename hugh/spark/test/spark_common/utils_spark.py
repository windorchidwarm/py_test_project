#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyspark import SparkConf
from pyspark.sql import SparkSession
"""
spark相关工具类
"""
class SparkUtils:

    @staticmethod
    def getSparkSession(name, **kw):
        """
        获取spark会话实例
        :param name:
        :param kw:
        :return:
        """

        conf = SparkConf()
        conf.setMaster(kw.get("spark.master", "yarn-client"))
        conf.set('spark.dynamicAllocation.enabled', 'false')
        conf.set("spark.yarn.am.cores", kw.get("spark.yarn.am.cores", 5))
        conf.set("spark.yarn.am.memory", kw.get("spark.yarn.am.memory", '5g'))
        conf.set("spark.executor.memory", kw.get("spark.executor.memory", "40g"))
        conf.set("spark.executor.instances", kw.get("spark.executor.instances", 5))
        conf.set("spark.executor.cores", kw.get("spark.executor.cores", 6))
        conf.set("spark.sql.shuffle.partitions", kw.get("spark.sql.shuffle.partitions", 1000))
        conf.set("spark.shuffle.file.buffer", kw.get("spark.shuffle.file.buffer", '512k'))
        conf.set("spark.shuffle.io.maxRetries", kw.get("spark.shuffle.io.maxRetries", 5))
        conf.set("spark.sql.warehouse.dir", kw.get("spark.sql.warehouse.dir", "hdfs://user/hive/warehouse"))
        conf.set("spark.executor.extraJavaOptions", "-XX:+PrintGCDetails -XX:+PrintGCTimeStamps -XX:+UseG1GC")

        # 默认为1,cluster模式下有效
        # conf.set("spark.driver.cores", kw.get("spark.driver.cores", 5))
        # 默认为1G,cluster模式下有效
        # conf.set("spark.driver.memory", kw.get("spark.driver.memory", "10g"))
        # driver堆外内存
        # conf.set("spark.driver.memoryOverhead", kw.get("spark.driver.memoryOverhead", "15g"))
        # 每一个python的worker进程的内存大小，在运行期间，如果数据大小超过这个限制，数据将会被分片并保存在磁盘上
        # conf.set("spark.python.worker.memory", kw.get("spark.python.worker.memory", "4g"))
        # 推测执行
        # conf.set("spark.speculation", "true")
        # spark中每一个action计算所有分区的序列化结果大小，超出这个值，程序将会终止, 默认1G
        # conf.set("spark.driver.maxResultSize", "4g")

        spark = SparkSession.builder \
            .appName(name) \
            .config(conf=conf) \
            .enableHiveSupport() \
            .getOrCreate()
        return spark

