#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : test_delete_any.py
# Author: hugh
# Date  : 2020/9/2


import os

from pyhive import hive
from TCLIService.ttypes import TOperationState

from impala.dbapi import connect
import pyhs2

import pandas as pd
from sqlalchemy import create_engine
import pyhdfs


def getCreateSql(df, tableName, dataPath, executeVersion):
    sql = 'CREATE TABLE IF NOT EXISTS `' + tableName + '` ('
    fields = []
    for i, j in zip(df.columns, df.dtypes):
        if i != 'executeVersion':
            if "object" in str(j):
                sql += '`' + i + '` string, '
                fields.append(i + ' string' )
            elif "float" in str(j):
                sql += '`' + i + '` double, '
                fields.append(i + ' double')
            elif "int" in str(j):
                sql += '`' + i + '` int, '
                fields.append(i + ' int')
            elif "date" in  str(j) or "time" in str(j):
                sql += '`' + i + '` timestamp, '
                fields.append(i + ' timestamp')
            else:
                sql += '`' + i + '` string, '
                fields.append(i + ' string')

    data_sq = '''
                    CREATE TABLE IF NOT EXISTS {TB_NAME} ({FIELDS}) PARTITIONED BY (execute_version STRING) row format delimited fields terminated by \'|\'  lines terminated by \'\n\'
                    '''.format(
                               TB_NAME=tableName,
                               FIELDS=','.join(fields))

    sql = sql[:-2]
    # sql += ') partitioned by (`executeVersion` string)'
    sql += ') partitioned by (`executeVersion` string) row format delimited fields terminated by \'|\'  lines terminated by \'\n\' '
    sql += 'location \'' + dataPath + '\''
    return data_sq


if __name__ == '__main__':
    '''
    spring.datasource.hive.url=jdbc:hive2://10.28.103.17:10000/db_finance
    spring.datasource.hive.username=bbders
    spring.datasource.hive.password=waAqMKuamwaasags
    spring.datasource.hive.driver-class-name=org.apache.hive.jdbc.HiveDriver
    '''
    print(os.path.join('da', 'da', 'da'))

    conn = hive.Connection(host='10.28.103.17', port=10000, auth='LDAP',
                           username='bbders', password='waAqMKuamwaasags', database='db_finance')
    cursor = conn.cursor()

    # conn = connect(host='10.28.103.17', port=10000, user='bbders', password='waAqMKuamwaasags',
    #                database='db_finance', auth_mechanism='PLAIN')
    #
    # cursor = conn.cursor()
    # cursor.execute('show tables')
    #
    # for result in cursor.fetchall():
    #     print(result)
    #
    # df = pd.read_sql('select * from t_mori_company_area_info', conn)
    #
    # print(df.info())
    db_host = '10.28.103.17'
    port = 10000
    authMechanism = 'PLAIN'
    user = 'bbders'
    password = 'waAqMKuamwaasags'
    database = 'db_finance'

    # engine = create_engine('impala://bbders:waAqMKuamwaasags@10.28.103.17:10000/db_finance?auth_mechanism=PLAIN')
    engine = create_engine('hive://bbders:waAqMKuamwaasags@10.28.103.17:10000/db_finance?auth=CUSTOM')
    # engine = create_engine('impala://', creator=conn)
    oldTableName = 't_mori_company_area_info'
    df = pd.read_sql('select * from ' + oldTableName, conn)
    execute_version = '20200903'
    df.insert(len(df.columns), 'executeVersion', execute_version)
    # executeVersion = '20200904'
    df.info()
    print(df)

    newColumns = []
    for col in df.columns:
        newColumns.append(col.split('.')[-1])
    df.columns = newColumns
    print(df.dtypes)
    dataPath = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'test.txt')
    df.to_csv(dataPath, sep='|', index=False)

    home_dir = '/user/bbders/ssehometest'
    # hdfs_client = pyhdfs.HdfsClient(hosts=['10.28.103.17,22','10.28.103.18,22','10.28.103.19,22','10.28.103.20,22','10.28.103.21,22'], randomize_hosts=True, user_name='bbders', retry_delay=30, max_tries=5)
    hdfs_client = pyhdfs.HdfsClient(hosts='10.28.103.18,8020', randomize_hosts=True, user_name='bbders', retry_delay=30, max_tries=5)

    print(hdfs_client.get_home_directory())
    data_base_dir = home_dir + '/test'
    hdfs_path = home_dir + '/test/' + execute_version + '/data.txt'
    if not hdfs_client.exists(home_dir + '/test/' + execute_version):
        hdfs_client.mkdirs(home_dir + '/test/' + execute_version)
    # hdfs_client.set_permission(hdfs_path)
    # hdfs_client.delete(hdfs_path)
    if hdfs_client.exists(hdfs_path):
        hdfs_client.delete(hdfs_path)
    hdfs_client.copy_from_local(dataPath, hdfs_path)
    # print(hdfs_client.listdir(home_dir))

    tableName = 'test_ins'
    sql = getCreateSql(df, tableName, home_dir + '/test', execute_version)
    print(sql)
    nSql = 'load data inpath \'' + hdfs_path + '\' into table ' + tableName + ' partition (execute_version=\'' + execute_version +'\')'
    print(nSql)
    # df.to_sql('test_pd_inds', engine, if_exists='append', index=False)
    # db_conn = engine.connect()
    # engine.execute(sql)
    # engine.execute(nSql)
    cursor.execute(sql)
    # conn.commit()
    cursor.execute(nSql)
    print(sql)



