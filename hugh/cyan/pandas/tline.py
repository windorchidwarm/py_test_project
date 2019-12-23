#!/usr/bin/env python
# -- coding: utf-8 --#

import sqlalchemy
import pandas as pd

if __name__ == '__main__':
    engienCmd = 'mysql+pymysql://{username}:{password}@{url}'.format(username='quant',
                                                                password='bbd123',
                                                                url='10.28.109.14:3306/sf_test')
    engine = sqlalchemy.create_engine(engienCmd, connect_args={'charset': 'utf8'})

    # sample_0
    sql = '''
        {sql}
    '''.format(sql='SELECT id, website,REPLACE(company_introduction, "\\r\\n", "@r@n") as "company_introduction" FROM qyxg_rongzi')

    df = pd.read_sql_query(sql, engine)
    print(len(df))
    print(df)
    df.join()
    # print(df[15:18])
    # print(df[15:16]['company_introduction'])
    # df = df.replace('\n', '@n')
    # df = df.replace('\\', '@r')
    # print(df[15:16]['company_introduction'])

    # for row in df.iterrows():
    #     print(row)

    df.to_csv('C://Users//Administrator//Desktop//test//tmp//rongzi.csv', index = False, header = True)