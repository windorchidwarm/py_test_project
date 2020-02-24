#!/usr/bin/env python
# -- coding: utf-8 --#
# @Time : 2020/2/24 13:33 
# @Author : Aries 
# @Site :  
# @File : test_sample.py 
# @Software: PyCharm


import pandas as pd
from imblearn.under_sampling import RandomUnderSampler


'''
采样测试
'''


def under_smaple(df):
    '''
    下采样
    :param df:
    :return:
    '''
    label = '商场ID'
    y = df[label]
    x = df.loc[:, df.columns != label]

    from imblearn.over_sampling import RandomOverSampler

    ros = RandomOverSampler(random_state=2020)
    X_resampled, y_resampled = ros.fit_sample(x, y)
    print(X_resampled)
    print(y_resampled)


if __name__ == '__main__':
    print('xxx')
    df = pd.read_csv(r'C:\Users\BBD\Desktop\test\tmp\Cshl0V1SGLeAb6opAABKW103UTU063.csv')
    print(df)

    print(under_smaple(df))
