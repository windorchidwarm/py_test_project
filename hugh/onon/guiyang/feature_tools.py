#!/usr/bin/env python
# -- coding: utf-8 --#
# @Time : 2020/3/6 13:41 
# @Author : Aries 
# @Site :  
# @File : feature_tools.py 
# @Software: PyCharm


import featuretools as ft
import pandas as pd


if __name__ == '__main__':
    '''
    特征组合 测试
    '''

    df = pd.read_csv(r'C:\Users\BBD\Desktop\test\tmp\Cshl0V1SGLeAb6opAABKW103UTU063.csv')
    print(df)
    updf = df[['编号', '商场ID', '商户ID', '单位面积营业额', '客流转换率变化情况']]
    # print(df.isnull)
    r_lsit = ['商场ID']

    es = ft.EntitySet(id = 'sales')
    es.entity_from_dataframe(entity_id='bigmart', dataframe=df, index='商户ID')
    print(es['bigmart'])
    es.normalize_entity(base_entity_id='bigmart', new_entity_id='sasa', index='编号', additional_variables=r_lsit)
    # print(es)
    feature_matrix_customers, features_dfs = ft.dfs(entityset=es, target_entity='bigmart', max_depth=2, n_jobs=3, verbose=1)
    print('***************')

    print(feature_matrix_customers)
    print('***************')
    print(feature_matrix_customers.columns)
    print('***************')
    print(features_dfs)
    feature_matrix_customers.to_csv(r'C:\Users\BBD\Desktop\test\tmp\xxxxx.csv')

