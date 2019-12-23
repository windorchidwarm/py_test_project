#!/usr/bin/env python
# -- coding: utf-8 --#

import pandas as pd
import sqlalchemy
import datetime
import re

if __name__ == '__main__':
    engineCmd = 'mysql+pymysql://{username}:{password}@{url}'.format(username='quant',
                                                                password='bbd123',
                                                                url='10.28.109.14:3306/bbd_tetris')
    engine = sqlalchemy.create_engine(engineCmd, connect_args={'charset': 'utf8'})
    db_conn = engine.connect()
    url = '''jdbc:mysql://10.28.109.14:3306/bbd_tetris'''
    url = url.replace("jdbc:mysql://", "")
    schemaName = url.split('/')[1]
    print(schemaName)

    sqlStr = '''select t.* from gxyh_process t left join gxyh_operate_log b on t.id = b.process_id '''

    tempTableName = 'tetris_local_1019_9323'
    createTmep = '''create table {tableName} select * from ( {sqlStr} ) tt_test limit 1'''.format(tableName=tempTableName,sqlStr=sqlStr)
    createTmep = '''create table {tableName} select * from ( {sqlStr} ) tt_test limit 1'''.format(tableName=tempTableName,sqlStr=sqlStr)

    tempTableColType = '''select column_name, column_comment, data_type from information_schema.columns where table_name = "{tableName}" and table_schema = "{tableSchema}"'''.format(tableName=tempTableName,tableSchema=schemaName)

    delTempTable = '''drop table if exists {tempTableName}'''.format(tempTableName=tempTableName)
    print(createTmep)
    print(tempTableColType)
    print(delTempTable)

    print(db_conn)

    db_conn.execute(createTmep)
    df = pd.read_sql(tempTableColType, con=db_conn)
    print(df)
    db_conn.execute(delTempTable)
    tableName = 'local_temp_%s_%s_%s' % (str(1243), str(124), str(0))
    print(tableName)
    # pd.read_sql(delTempTable, engine)
    columnType = {}
    for i in range(len(df)):
        if df['data_type'][i].lower() in ('varchar', 'varchar2', 'char','binary','varbinary','blob','text','enum','set','mediumblob','mediumtext','longblob','longtext'):
            columnType[df['column_name'][i]] = 'string'
        elif df['data_type'][i].lower() in ('int', 'bigint', 'tinyint', 'smallint', 'mediumint', 'integer'):
            columnType[df['column_name'][i]] = 'int'
        elif df['data_type'][i].lower() in ('float', 'double'):
            columnType[df['column_name'][i]] = 'float'
        elif df['data_type'][i].lower() in ('date', 'time', 'year','datetime','timestamp'):
            columnType[df['column_name'][i]] = 'date'
        else:
            columnType[df['column_name'][i]] = 'string'
    print(columnType)
