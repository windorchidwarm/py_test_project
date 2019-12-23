#!/usr/bin/env python
# -- coding: utf-8 --#

import pandas as pd
import sqlalchemy
import datetime
import re


def getFieldJoinColumns(fieldAs):
    leftColumns = {}
    rightColumns = {}
    for newName in fieldAs.keys():
        oldNameMap = fieldAs[newName].split(".")
        if oldNameMap[0] == 'l':
            leftColumns[oldNameMap[1]] = newName
        else:
            rightColumns[oldNameMap[1]] = newName
    return leftColumns, rightColumns

if __name__ == '__main__':
    engienCmd = 'mysql+pymysql://{username}:{password}@{url}'.format(username='quant',
                                                                password='bbd123',
                                                                url='10.28.109.14:3306/sf_test')
    engine = sqlalchemy.create_engine(engienCmd, connect_args={'charset': 'utf8'})

    tt = 'select * from test'
    de = 1000

    sql = 'select * from ({sql}) b limit {limitNum}'.format(sql=tt, limitNum=de)
    print(sql)
    alldf = pd.read_sql_query(sql, engine)

    print(alldf.isnull().all())

    fieldAs = {"news_site_l": "l.news_site", "news_site_r": "r.news_site", "bbd_xgxx_id_r": "r.bbd_xgxx_id", "news_title_r": "r.news_title", "news_title_l": "l.news_title", "bbd_url_r": "r.bbd_url", "plate_l": "l.plate", "bbd_url_l": "l.bbd_url", "ctime_r": "r.ctime", "bbd_dotime_l": "l.bbd_dotime", "plate_r": "r.plate", "bbd_uptime": "l.bbd_uptime", "bbd_dotime_r": "r.bbd_dotime", "attachment_list_l": "l.attachment_list", "main_r": "r.main", "bbd_type_l": "l.bbd_type", "ctime_l": "l.ctime", "attachment_list_r": "r.attachment_list", "bbd_type_r": "r.bbd_type", "main_l": "l.main", "bbd_source_r": "r.bbd_source", "pubdate_r": "r.pubdate", "pubdate_l": "l.pubdate", "bbd_xgxx_id_l": "l.bbd_xgxx_id", "bbd_source_l": "l.bbd_source"}
    l,r = getFieldJoinColumns(fieldAs)
    print(fieldAs)
    print(l)
    print(r)

    # alldf = pd.read_sql_query(sql, engine)
    # print(alldf.dtypes)
    # alldf['te'] = pd.to_datetime(alldf['te'])
    # print(alldf.dtypes)
    # print(alldf)
    # columnType = {}