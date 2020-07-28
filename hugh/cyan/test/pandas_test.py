#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : pandas_test.py
# Author: hugh
# Date  : 2020/7/28

import pandas as pd

if __name__ == '__main__':
    '''
    '''
    df = pd.read_csv(r'C:\Users\BBD\Desktop\test\tmp\2.csv')
    print(df)
    print('2' in '2班')
    df['id'] = df['id'].apply(lambda x: str(x))
    df = df[df.apply(lambda x: str(x['id']) in x['class'], axis=1)]
    print(df)