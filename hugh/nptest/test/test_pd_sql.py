#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : test_pd_sql.py
# Author: hugh
# Date  : 2020/5/21



import pandas as pd
from pandasql import sqldf, load_meat, load_births


if __name__ == '__main__':
    '''
    pandas sql
    '''
    data = {'Chinese': [66, 95, 93, 90, 80], 'English': [65, 85, 92, 85, 90], 'Math': [30, 98, 96, 77, 90]}
    df = pd.DataFrame(data, index=['ZhangFei', 'GuanYu', 'ZhaoYun', 'HuangZhong', 'DianWei'],
                    columns=['English', 'Math', 'Chinese'])

    pysqldf = lambda sql: sqldf(sql, globals())

    sql = 'select * from df where English  = 85'

    print(pysqldf(sql))

    data = {'Chinese': [66, 95, 93, 90, 80, 80], 'English': [65, 85, 92, 88, 90, 90],
            'Math': [None, 98, 96, 77, 90, 90]}
    df_data = pd.DataFrame(data, index=['张飞', '关羽', '赵云', '黄忠', '典韦', '典韦'],
                      columns=['English', 'Math', 'Chinese'])

    df_data = df_data.drop_duplicates()

    def add_total(df):
        df['all'] = df['English'] + df['Math'] + df['Chinese']
        return df

    df_data = df_data.apply(add_total, axis=1)
    # df_data['all'] = df_data.sum(axis=1)
    print(df_data)