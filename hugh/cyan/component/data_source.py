# #!/usr/bin/env python
# # -- coding: utf-8 --#
# '''
# 1、sqoop导入  输出全量数据 输出显示
# 2、spark读取计算每列 均值方差，最大，最小，数据分布占比
#
#
# spark2-submit --master yarn   --driver-memory 20g --driver-cores 2  --executor-memory 20g --executor-cores 5 --num-executors 20 --py-files /home/bbders/etl/spark_common.zip data_source.py
# '''
#
# import os
# import sys
#
# import argparse
# import json
# from pyspark.conf import SparkConf
# from pyspark.sql import SparkSession
# from pyspark.sql import functions as F
# from spark_common.spark_utils import *
# from spark_common.data_utils import *
# from spark_common.execute_status_enum import ExecuteStatusEnum
# from spark_common.httpUtils import reportState
#
#
#
#
# # dataSourceMeta={"nid":"1","eid":"2","type": "11", "isEnd": "0","dbType":"mysql","username":"quant","password":"bbd123",
# #                 "url":"jdbc:mysql://10.28.109.14:3306/bbd_quant_v2",
# #                 "sql":"select remote_addr,method,request_uri,type,create_by,create_date from sys_log",
# #                 "outTableMeta":
# #                     [{"fieldName":"remote_addr","valueType":"VARCHAR"},
# #                       {"fieldName":"method","valueType":"VARCHAR"},
# #                      {"fieldName":"request_uri","valueType":"VARCHAR"},
# #                      {"fieldName":"type","valueType":"CHAR"} ,
# #                      {"fieldName":"create_by","valueType":"INT"} ,
# #                      {"fieldName":"create_date","valueType":"DATETIME"}]}
# parser = argparse.ArgumentParser(description='node args')
# parser.add_argument('-na', '--nodeArgs', type=str)
# args = parser.parse_args()
# print(args.nodeArgs)
# dataSourceMeta = json.loads(args.nodeArgs)
# # dataSourceMeta = {"nid": "1", "eid": "4", "type": "11", "isEnd": "0", "dbType": "hive",
# #                   "sql": "select city_code,statistics_date,company_type ,score ,company_name,region_code,new_economy_type ,financing,patent_num from test.com_new_economy",
# #                   "outTableMeta":
# #                       [{"fieldName": "city_code", "valueType": "VARCHAR"},
# #                        {"fieldName": "statistics_date", "valueType": "DATETIME"},
# #                        {"fieldName": "company_type", "valueType": "INT"},
# #                        {"fieldName": "score", "valueType": "FLOAT"},
# #                        {"fieldName": "company_name", "valueType": "VARCHAR"},
# #                        {"fieldName": "region_code", "valueType": "VARCHAR"},
# #                        {"fieldName": "new_economy_type", "valueType": "VARCHAR"},
# #                        {"fieldName": "financing", "valueType": "FLOAT"},
# #                        {"fieldName": "patent_num", "valueType": "INT"},
# #                        ]}
#
#
# # def hiveImport(sql,path,oneFile=0):
# #     '''
# #     hive 表导入
# #     Args:
# #         sql:
# #         path:
# #         display:
# #
# #     Returns:
# #
# #     '''
# #     if oneFile == 0:
# #         spark.sql(sql).write.mode('overwrite').csv(path=path,sep='\001')
# #     else:
# #         spark.sql(sql).repartition(1).write.mode('overwrite').csv(path=path,sep='\001')
#
# # def sqoopImport(sql,targetDir,hiveType,splitColum):
# #     '''
# #     sqoop导入
# #     Returns:
# #     '''
# #     sqoopCmd =  "kinit -kt /home/bbders/bbders.keytab bbders && sqoop import --connect {url} " \
# #                 "--username {username} --password  {password} " \
# #                 "--mapreduce-job-name data_mining_sqoop_{eid}_{nid} " \
# #                 "--as-parquetfile  " \
# #                 "--null-string '\\\\N' " \
# #                 "--null-non-string '\\\\N' " \
# #                 "--target-dir {targetDir} " \
# #                 "--num-mappers 100 " \
# #                 "--delete-target-dir " \
# #                 "--map-column-hive {hiveType} " \
# #                 "--split-by '`{splitColum}`' " \
# #                 "--query '{sql}' ".format(
# #                                 url = dataSourceMeta.get("url"),
# #                                 username = dataSourceMeta.get("username"),
# #                                 password = dataSourceMeta.get("password"),
# #                                 eid = dataSourceMeta.get("eid"),
# #                                 nid = dataSourceMeta.get("nid"),
# #                                 targetDir = targetDir,
# #                                 hiveType=hiveType,
# #                                 splitColum=splitColum,
# #                                 sql = sql
# #                             )
# #     return HbaseUtils.excSubprocessCommand(sqoopCmd,"sqoop import ===> ")
#
#
# def dataImport():
#     dbType = dataSourceMeta.get("dbType")
#     eCode = True
#     alldf = None
#     if dbType == "hive":
#         alldf = spark.sql(dataSourceMeta.get("sql"))
#     elif dbType =="mysql":
#         splitColum = outTableMetaDict.get("0", [])[0].get("fieldName")
#         hiveType,dateField = getHiveTypeSchema(outTableMetaDict.get("0", []))
#         sqoopAllSql = "select * from ({sql}) as t where 1=1 and $CONDITIONS".format(sql=dataSourceMeta.get("sql"))
#         ptDir = targetAllDir + "_pt"
#         eCode = sqoopImport(sqoopAllSql, ptDir,hiveType,splitColum)
#         alldf = spark.read.parquet(ptDir)
#         for f,type in dateField.items():
#             alldf = alldf.withColumn(f,F.from_unixtime(F.col(f)/1000.0, format='yyyy-MM-dd HH:mm:ss'))
#             if type=="DATE":
#                 alldf = alldf.withColumn(f,F.to_date(F.col(f),format='yyyy-MM-dd HH:mm:ss'))
#             else:
#                 alldf = alldf.withColumn(f, F.to_timestamp(F.col(f), format='yyyy-MM-dd HH:mm:ss'))
#
#     writeTarget(alldf, targetAllDir, targetDisplayDir, targetDownloadDir)
#     return eCode
#
# if __name__ == '__main__':
#     #展示和下载数
#     display_num = getDisplayNum()
#     download_num = getDownloadNum()
#
#     NODE_RESULT_CALLBACK_URL = dataSourceMeta.get("NODE_RESULT_CALLBACK_URL")
#     excuteId = dataSourceMeta.get("eid")
#     nodeId = dataSourceMeta.get("nid")
#     isEnd = dataSourceMeta.get("isEnd")
#     nodeType = dataSourceMeta.get("type")
#     outTableMetaDict = dataSourceMeta.get("outTableMeta", {})
#
#     spark,applicationId = getSparkSession(excuteId,nodeId, "data_source")
#     targetAllDir, targetDisplayDir, targetDownloadDir = getOutputPath(excuteId,nodeId)
#
#     # 上报状态，开始执行
#     reportState(excuteId, nodeId, isEnd, nodeType, ExecuteStatusEnum.RUNING.value, "开始执行", NODE_RESULT_CALLBACK_URL)
#     try:
#         if dataImport():
#             dataDist = dataDistribution(spark,targetAllDir,outTableMetaDict.get("0",[]))
#             dataDistJson = json.dumps({"0":dataDist})
#             print(dataDistJson)
#
#             # 发布到hbase
#             publishConfig = dataSourceMeta.get("publishConfig")
#             executeVersion = dataSourceMeta.get("executeVersion")
#             if isEnd == 1 and publishConfig:
#                 publishNode(spark, nodeId, excuteId, publishConfig, executeVersion, outTableMetaDict)
#
#
#             # 最后没有异常，执行成功
#             reportState(excuteId, nodeId, isEnd, nodeType, ExecuteStatusEnum.SUCCESS.value, "执行成功",
#                         NODE_RESULT_CALLBACK_URL, statisticData=dataDistJson)
#         else:
#             raise Exception("数据导入失败")
#     except Exception as e:
#         import traceback
#         print("#########################################Exception############################################")
#         traceback.print_exc()
#         info = traceback.format_exc()
#         reportState(excuteId, nodeId, isEnd, nodeType, ExecuteStatusEnum.FAILED.value, info, NODE_RESULT_CALLBACK_URL)
#         sys.stderr(str(info))
#         raise e
#
