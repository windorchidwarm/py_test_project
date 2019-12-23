#!/usr/bin/env python
# -- coding: utf-8 --#

import sqlalchemy
import pandas as pd
import numpy as np

if __name__ == '__main__':
    engienCmd = 'mysql+pymysql://{username}:{password}@{url}'.format(username='quant',
                                                                password='bbd123',
                                                                url='10.28.109.14:3306/bbd_tetris')
    engine = sqlalchemy.create_engine(engienCmd, connect_args={'charset': 'utf8'})

    # sample_0
    sql = '''
        {sql}
    '''.format(sql='select * from mytable limit 100')
    upDf = pd.read_sql_query(sql, engine)

    rowkeyMeta = [{"fieldName":"index"},{"fieldName":"job_blue_collar"}]


    rowkeyFileds = [rk.get("fieldName") for rk in rowkeyMeta]
    print(rowkeyFileds)

    upDf = upDf.set_index(rowkeyFileds)
    print(upDf)
    upDf.to_sql('mm', engine, if_exists='replace')

    # print(upDf)

    # upDf1 = upDf.sample(frac=1.0, replace=False)
    #
    # num = int(len(upDf) * 0.3)
    #
    # up1 = upDf1.head(num)
    # up2 = upDf1.tail(len(upDf) - num)
    #
    # print("*****************")
    # print(up1)
    # print("*****************")
    # print(up2)
    #
    # data = [up1, up2]
    #
    #
    #
    # print(upDf.describe())
    #
    # for i in range(len(data)):
    #     data[i].to_sql('tt' + str(i), engine, if_exists = 'replace')
    #
    # dd = upDf.corr()
    # print(dd)
    # print("&&&&&&&&&&&&")
    # print(str(dd))
    # print("&&&&&&&&&&&&")
    # isnulls = upDf.isnull().any()
    # print(isnulls)

    # up1.to_sql('t1', engine, if_exists = 'replace')
    # up2.to_sql('t2', engine, if_exists = 'replace')


    # mmDf = pd.DataFrame()
    # for field in ['index', 'job_blue_collar']:
    #     mmDf[field] = upDf[field]
    #
    # print(mmDf)

    # ttDf = pd.read_sql_query('select * from gxyh_process limit 100', engine)
    # print(upDf.join(ttDf.set_index(['id']), on =['index'], how='right', lsuffix='_l', rsuffix='_r'))
    # print(pd.merge)
    # print(upDf)
    # upDf['index'] = upDf['index'].fillna(upDf['index'].mean())
    # print("*****************")
    # print(upDf)
    # upDf['job_blue_collar'] = upDf['job_blue_collar'].fillna(5)
    # print("*****************")
    # print(upDf)
    # upDf = upDf.dropna(subset=['job_housemaid'])
    # print("*****************")
    # print(upDf)
    # upDf = upDf.drop(columns=['y'])
    # print("*****************")
    # print(upDf)
    # print(upDf['job_housemaid'])
    # upDf.to_sql('mytt', engine, if_exists='replace')
    # print(upDf)
    # print("**************************************")
    # ssDf = pd.read_sql_query('select * from mytt', engine)
    # print(ssDf)
    # print("**************************************")
    # ppDf = upDf.append(ssDf, ignore_index=True, sort=True)
    # print(ppDf)
    # print("**************************************")
    # print(ppDf['level_0'])
    # for i in range(3):
    #     ppDf = ppDf.append(ssDf)
    #     print("**************************************")
    #     print(ppDf)
