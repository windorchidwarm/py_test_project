#!/usr/bin/env python
# -- coding: utf-8 --#
# @Time : 2020/3/17 13:57 
# @Author : Aries 
# @Site :  
# @File : mean_shift.py 
# @Software: PyCharm


from sklearn.cluster import  MeanShift
import pandas as pd
import numpy as np


def test_mean_shift(df, label):
    '''

    :param df:
    :param label:
    :return:
    '''
    mean_shift =  MeanShift(bandwidth=10, seeds=[10])
    y = df[label]
    X = df.loc[:, df.columns != label]
    print(mean_shift)
    data = mean_shift.fit(X, y)
    print(data)
    print(mean_shift.cluster_centers_)
    out0 = pd.DataFrame(mean_shift.cluster_centers_, columns=np.array(X.columns[:]))
    print(out0)
    print(mean_shift.min_bin_freq)



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

    # svc_test(updf, label)
    test_mean_shift(updf, label)