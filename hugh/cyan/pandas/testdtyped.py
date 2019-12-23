#!/usr/bin/env python
# -- coding: utf-8 --#

import pandas as pd

def changeToNum(x):
    try:
        float(x)
    except ValueError:
        x = None
    return x

if __name__ == '__main__':
    print('------------------------------')
    df = pd.read_csv(r'C:\Users\Administrator\Desktop\test\tmp\sample_0.csv')
    df = df.head(30)
    df['index'].astype('object')
    df['job_blue-collar'].astype('object')
    df['job_housemaid'].astype('object')
    df['euribor3m'].astype('object')
    df['index'][3] = 'a'
    df['job_blue-collar'][0] = '2018-03-21'
    df['job_housemaid'][0] = '2018-03-21 19:23:33'
    df['euribor3m'][0] = '2018/03/21 19:23:33'
    print(df)
    df['euribor3m'] = df['euribor3m'].apply(changeToNum)
    print(df['euribor3m'])
    df['euribor3m'].astype('float')
    # df.to_csv(r'C:\Users\Administrator\Desktop\test\tmp\abc.csv', index=False)

