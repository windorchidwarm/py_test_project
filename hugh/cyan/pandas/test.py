#!/usr/bin/env python
# -- coding: utf-8 --#
# @Time : 2019/12/5 11:50 
# @Author : Aries 
# @Site :  
# @File : test.py 
# @Software: PyCharm


#!/usr/bin/env python
# -- coding: utf-8 --#

import pandas as pd
import seaborn as sns
import numpy as np
import sqlalchemy
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engienCmd = 'mysql+pymysql://{username}:{password}@{url}'.format(username='root',
                                                                     password='123456',
                                                                     url='10.28.103.19:12345/tetris_manage')
    engine = sqlalchemy.create_engine(engienCmd, connect_args={'charset': 'utf8'})

    # sql = '''select MAX(date_format(create_date, "%H:%i:%s")) latest_op_time, operator_name
    #   from gxyh_operate_log
    #   where operator_name
    #   group by operator_name
    #   order by latest_op_time desc'''
    # # Session = sessionmaker(bind=engine)
    # # sess = Session()
    # #
    # # allDf = sess.execute(sql).fetchall()
    # # allDf = pd.DataFrame(allDf)
    # # print(allDf)
    # # reg = 'date_format'
    # sql = sqlalchemy.text(sql)
    # print(sql)
    # allDf =pd.read_sql_query(sql, engine)
    # print(allDf)

    df = pd.read_csv(r'C:\Users\BBD\Desktop\test\tmp\iris.data')
    df = df.drop(columns="Iris-setosa")
    df.columns = ['a', 'b', 'c', 'd']
    df.to_sql('test_lo', engine, if_exists='replace', index=False)
    print(df)