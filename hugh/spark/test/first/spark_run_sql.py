#!/usr/bin/env python
# -- coding: utf-8 --#

import pandas as pd
import numpy as np
import sqlalchemy
import datetime
from fdfs_client.client import *
import re
from pyspark.sql.functions import udf
from pyspark.sql.types import StringType
from pyspark.conf import SparkConf
from pyspark.ml.linalg import VectorUDT
from pyspark.sql import SparkSession
import os

if __name__ == '__main__':
    os.environ['JAVA_HOME'] = '/usr/java/jdk1.8.0_144'
    os.environ['PYSPARK_PYTHON'] = '/home/bbders/anaconda3/bin/python'
    os.environ['SPARK_HOME'] = '/opt/cloudera/parcels/CDH-5.13.3-1.cdh5.13.3.p0.2/'
    sys.path.append('/home/bbders/anaconda3/bin/python')
    os.system('kinit -kt /home/bbders/bbders.keytab bbders && PYSPARK_PYTHON=/home/bbders/anaconda3/bin/python spark2-submit \
        --master yarn \
        --deploy-mode client \
        --driver-memory 1g \
        --queue users.bbders \
        --driver-cores 2  --executor-memory 4g --executor-cores 4 --num-executors 5')
    conf = SparkConf()
    appName = "data_mining_{type}_{eid}_{nid}".format(eid=9033, nid=1032, type='data_source')
    # conf.setMaster('yarn-client')
    # conf.set("spark.yarn.keytab", "/home/bbders/bbders.keytab")
    # conf.set("spark.yarn.keytab", "E://config//tetris-datamining//bbders.keytab")
    # conf.set("spark.yarn.am.cores", 2)
    # conf.set("spark.executor.memory", "16g")
    # conf.set("spark.executor.cores", 4)
    # conf.set("spark.num.executors", 5)
    # conf.set("spark.python.worker.memory", "2g")
    conf.set("spark.sql.warehouse.dir", "/user/hive/warehouse/")
    conf.set("hive.exec.dynamic.partition", "true")
    conf.set("hive.exec.dynamic.partition.mode", "nonstrict")
    conf.set("spark.hadoop.dfs.replication", "2")
    conf.set("spark.debug.maxToStringFields", "1000")
    spark = SparkSession \
        .builder \
        .appName(appName) \
        .config(conf=conf) \
        .enableHiveSupport() \
        .getOrCreate()

    sql = '''select * from (select * from tetris.qyxx_basic) a limit 10000'''
    alldf = spark.sql(sql)
    print(alldf)
    # alldf = convertToCsvFormatHive(alldf)
    # alldf.repartition(1).write.csv(path=targetAllDir, sep=',', header=True, mode="overwrite", nullValue="null")
    # alldf.limit(getDownloadNum()).repartition(1).write.csv(path=targetDownloadDir, sep=',', header=True,
    #                                                        mode="overwrite", nullValue="null")
    # alldf.limit(getDisplayNum()).repartition(1).write.csv(path=targetDisplayDir, sep=',', header=True, mode="overwrite",
    #                                                       nullValue="null")
    #
    # client = Fdfs_client(FDFSDATA)
    # allPath = client.upload_by_filename(targetAllDir)
    # displayPath = client.upload_by_filename(targetDisplayDir)
    # downPath = client.upload_by_filename(targetDownloadDir)
    #