#!/usr/bin/env python
# -- coding: utf-8 --#
# @Time : 2020/4/8 13:45 
# @Author : Aries 
# @Site :  
# @File : random_splite.py 
# @Software: PyCharm



import pandas as pd

from sklearn import model_selection


if __name__ == '__main__':
    '''
    切分测试
    '''
    df = pd.read_csv(r'C:\Users\BBD\Desktop\test\tmp\Cshl0V1SGLeAb6opAABKW103UTU063.csv')
    print(df)

    train_df, test_df = model_selection.train_test_split(df, stratify=None, random_state=9, train_size=0.3)
    print(train_df)
    print(test_df)