#!/usr/bin/env python
# -- coding: utf-8 --#
# @Time : 2019/10/14 11:12 
# @Author : Aries 
# @Site :  
# @File : yunnan.py 
# @Software: PyCharm

import pandas as pd
import sqlalchemy
import datetime
import re


if __name__ == '__main__':
    engienCmd = 'mysql+pymysql://{username}:{password}@{url}'.format(username='bbd',
                                                                     password='123456',
                                                                     url='10.28.109.102:3306/db_policy_government_service')
    engine = sqlalchemy.create_engine(engienCmd, connect_args={'charset': 'utf8'})
    sql = 'select * from policy_company_declare'
    df = pd.read_sql_query(sql, engine)
    df = df.drop(['registration_addr_city', 'registration_addr_county', 'registration_addr_area'], axis=1)
    print(df)
    # addrs = df['registration_addr'].str.split('/',expand=True).stack().reset_index(level=1, drop=True).rename("track")
    # print(addrs)
    # print(df["registration_addr"].str.split('/',expand=True).stack().reset_index(level=1, drop=True).rename("test"))
    df1 = df.join(df["registration_addr"].str.split('/',expand=True))
    print('------------------------')
    print(df1)
    df1.rename(columns={0 :'registration_addr_city', 1: 'registration_addr_county', 2: 'registration_addr_area'}, inplace=True)
    print(df1)

    for column in df1.columns:
        print(column)

    df1.to_sql('policy_company_declare', engienCmd, if_exists='replace', index=False)
    # gp = addrs.groupby(by = [0, 1], as_index=False)
    # print(gp)
    # data = gp.size()
    # print(data)
    # print(type(data))