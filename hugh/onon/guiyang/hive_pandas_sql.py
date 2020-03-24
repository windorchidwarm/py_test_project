#!/usr/bin/env python
# -- coding: utf-8 --#
# @Time : 2020/3/24 10:46 
# @Author : Aries 
# @Site :  
# @File : hive_pandas_sql.py 
# @Software: PyCharm

from sqlalchemy import create_engine
import pandas as pd



if __name__ == '__main__':
    print('xxxxxxxxx')
    url = "jdbc:hive://10.20.10.11:10000/"
    url = url.replace("jdbc:hive2://", "hive://")
    url = url.replace("jdbc:hive://", "hive://")
    e = create_engine(url)
    # `tpcds_bin_partitioned_orc_2`.`web_site`
    sql = "select * from `bbd`.`edge_customer_return_catalog` limit 1"
    r = e.execute(sql).fetchall()
    print(r)
    df = pd.DataFrame(map(dict, r))
    print(df)
    # 这种方式获取不到数据
    # df = pd.read_sql(sql, con=e)
    df = pd.read_sql_query(sql, con= e)
    print(df)
