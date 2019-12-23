#!/usr/bin/env python
# -- coding: utf-8 --#
# @Time : 2019/9/17 10:33 
# @Author : Aries 
# @Site :  
# @File : testspark.py 
# @Software: PyCharm


from pyspark import SparkConf
from pyspark.sql import SparkSession


def test_spark_session():
    warehouseLocation = "hdfs:///user/hive/warehouse"
    spark = SparkSession \
        .builder \
        .appName("index_fetch1") \
        .config("spark.sql.warehouse.dir", warehouseLocation) \
        .enableHiveSupport() \
        .getOrCreate()
    return spark


def get_spark_session():
    conf = SparkConf()
    conf.setMaster("yarn")
    conf.set("spark.executor.memory", "4g")
    conf.set("spark.executor.instances", 3)
    conf.set("spark.executor.cores", 4)
    conf.set("spark.python.worker.memory", "2g")
    conf.set("spark.default.parallelism", 1000)
    conf.set("spark.sql.shuffle.partitions", 1000)
    conf.set("spark.broadcast.blockSize", 1024)
    conf.set("spark.shuffle.file.buffer", '512k')
    conf.set("spark.speculation", True)
    conf.set("spark.speculation.quantile", 0.98)

    spark = SparkSession.builder \
        .appName('test-spark') \
        .config(conf=conf) \
        .enableHiveSupport() \
        .getOrCreate()

    return spark


if __name__ == '__main__':
    print('----------')
    spark = get_spark_session()
    wr = spark.read.format('jdbc').option('user', '').option('password', '').option('url', '')

    df = wr.option('dbtable', '').load()
    spark.sql('''
        select * from tetris_log
    ''')
    '''
    #!/usr/bin/env bash
    /opt/spark2/bin/spark-submit --master  yarn-client  --num-executors 5 --executor-memory 5g --executor-cores 2 --driver-memory 5g --driver-cores 2 --name JupyterNoteBook --queue root.project.dptest --conf spark.python.worker.memory=2G --conf spark.default.parallelism=2000 test_index_pool_basic.py
    '''