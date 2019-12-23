#!/usr/bin/env python
# -- coding: utf-8 --#
# @Time : 2019/11/18 15:26 
# @Author : Aries 
# @Site :  
# @File : del_184_admin.py 
# @Software: PyCharm


import pandas as pd
import seaborn as sns
import numpy as np
import sqlalchemy
import json
from fdfs_client.client import *

if __name__ == '__main__':
    engienCmd = 'mysql+pymysql://{username}:{password}@{url}'.format(username='quant',
                                                                     password='bbd123',
                                                                     url='10.28.109.14:3306/bbd_tetris')
    engine = sqlalchemy.create_engine(engienCmd, connect_args={'charset': 'utf8'})

    sql = '''select id, latest_output
      from gxyh_node
      where create_by = "2088741431098938"'''
    sql = sqlalchemy.text(sql)
    print(sql)

    FDFSDATA = {'host_tuple': ['10.28.200.184'], 'port': 22122, 'timeout': 60,
                'name': 'Tracker Pool'}
    client = Fdfs_client(FDFSDATA)

    allDf =pd.read_sql_query(sql, engine)
    # print(allDf)
    for index, row in allDf.iterrows():
        # print(row)
        # print(row['id'], '------------', row['latest_output'])
        # print(row['id'])
        if row['latest_output'] is not None and row['latest_output'] != '':
            data = json.loads(row['latest_output'])
            for key in data:
                statisc = data[key]
                # print(statisc)
                if 'group1' in statisc['displayDataPath']:
                    print(statisc['displayDataPath'].replace('\"', ''))

                    print(statisc['allDataPath'].replace('\"', ''))
                    print(statisc['downloadDataPath'].replace('\"', ''))
                    try:
                        client.delete_file(statisc['displayDataPath'].replace('\"', '').encode())
                        client.delete_file(statisc['allDataPath'].replace('\"', '').encode())
                        client.delete_file(statisc['downloadDataPath'].replace('\"', '').encode())
                    except Exception as e:
                        print(e)

                    # client.delete_file(statisc['displayDataPath'].encode())
                    # client.delete_file(statisc['allDataPath'].encode())
                    # client.delete_file(statisc['downloadDataPath'].encode())