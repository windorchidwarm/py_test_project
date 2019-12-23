#!/usr/bin/env python
# -- coding: utf-8 --#

import pandas as pd
import sqlalchemy

if __name__ == '__main__':
    engienCmd = 'mysql+pymysql://{username}:{password}@{url}'.format(username='quant',
                                                                     password='bbd123',
                                                                     url='10.28.109.14:3306/sf_test')
    engine = sqlalchemy.create_engine(engienCmd, connect_args={'charset': 'utf8'})
    sql = '''select * from test_data'''
    leftDf = pd.read_sql_query(sql, engine)
    rightDf = pd.read_sql_query(sql, engine)
    # print(rightDf.dtypes)
    allDf = leftDf.join(rightDf.set_index('string_data'), on='id', how='left', lsuffix='_l', rsuffix='_r')
    print(allDf)