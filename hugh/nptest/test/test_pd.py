#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : test_pd.py
# Author: hugh
# Date  : 2020/5/21

import pandas as pd

if __name__ == '__main__':
    '''
    测试pandas
    '''
    x1 = pd.Series([1,2,3,4])
    x2 = pd.Series(data=[1,2,3,4], index=['a', 'b', 'c', 'd'])
    print(x1, x2)
    # 字典方式也可创建Series

    import pandas as pd
    from pandas import Series, DataFrame

    data = {'Chinese': [66, 95, 93, 90, 80], 'English': [65, 85, 92, 88, 90], 'Math': [30, 98, 96, 77, 90]}
    df1 = DataFrame(data)
    df2 = DataFrame(data, index=['ZhangFei', 'GuanYu', 'ZhaoYun', 'HuangZhong', 'DianWei'],
                    columns=['English', 'Math', 'Chinese'])
    print(df1)
    print(df2)

    df2.drop(index=['ZhangFei'])

    # 去除重复行
    df2 = df2.drop_duplicates()
    df2['English'] = df2['English'].astype('str')
    df2['English'] = df2['English'].str.strip('5')
    print(df2)


    # 跨行操作
    #其中 axis=1 代表按照列为轴进行操作，axis=0 代表按照行为轴进行操作，
    # args 是传递的两个参数，即 n=2, m=3，在 plus 函数中使用到了 n 和 m，从而生成新的 df。
    def plus(df, n, m):
        df['new1'] = (df[u'语文'] + df[u'英语']) * m
        df['new2'] = (df[u'语文'] + df[u'英语']) * n
        return df


    df1 = df1.apply(plus, axis=1, args=(2, 3,))

    data = pd.read_csv(r'C:\Users\BBD\Desktop\test\tmp\12345.csv')
    print(data)