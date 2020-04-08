#!/usr/bin/env python
# -- coding: utf-8 --#
# @Time : 2020/4/8 13:45 
# @Author : Aries 
# @Site :  
# @File : random_splite.py 
# @Software: PyCharm



import pandas as pd

from sklearn import model_selection

def train_test_split(df, stratify):
    '''

    :param df:
    :return:
    '''
    stratify_df = df[stratify] if stratify is not None and stratify != '' else None

    train_df, test_df = model_selection.train_test_split(df, stratify=stratify_df, random_state=9, train_size=0.3)
    return train_df, test_df


def k_folder(df, stratify):
    '''
    k折交叉切分。
    :param df:
    :param stratify:
    :return:
    '''
    y = df[stratify]
    X = df.loc[:, df.columns != stratify]
    folder = model_selection.KFold(n_splits=4, random_state=0, shuffle=False)
    sfolder = model_selection.StratifiedKFold(n_splits=4, random_state=0, shuffle=False)
    for train, test in folder.split(X, y):
        print(train)
        print(test)
        print('---------')


if __name__ == '__main__':
    '''
    切分测试
    '''
    df = pd.read_csv(r'C:\Users\BBD\Desktop\test\tmp\test_data_classification.csv')
    print(df)
    stratify = 'Disbursed'
    k_folder(df, stratify)
    train_df, test_df = train_test_split(df, stratify)
    # print(train_df)
    # print(test_df)