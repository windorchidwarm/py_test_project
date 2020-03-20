#!/usr/bin/env python
# -- coding: utf-8 --#
# @Time : 2020/3/17 14:28 
# @Author : Aries 
# @Site :  
# @File : value_chansform.py 
# @Software: PyCharm

import numpy as np
import pandas as pd

if __name__ == '__main__':
    print('xxx')
    df = pd.read_csv(r'C:\Users\BBD\Desktop\test\tmp\Cshl0V1SGLeAb6opAABKW103UTU063.csv')
    print(df)

    # test_svm_svc()
    # updf = df.select(['编号', '商场ID', '商户ID', '单位面积营业额', '单位面积租金'], axis=1)
    # labels = ['编号', '商场ID', '商户ID', '单位面积营业额', '单位面积租金']
    updf = df[['编号', '商场ID', '商户ID', '单位面积营业额', '客流转换率变化情况']]
    label = '编号'
    updf = updf.append(updf, ignore_index=True, sort=False)
    updf = updf.append(updf, ignore_index=True, sort=False)
    print(updf)
    field_name = '编号'
    updf[field_name] = np.log2((1+updf[field_name]))
    print(updf)
