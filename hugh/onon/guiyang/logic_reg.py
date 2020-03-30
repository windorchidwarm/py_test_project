#!/usr/bin/env python
# -- coding: utf-8 --#
# @Time : 2020/3/30 14:35 
# @Author : Aries 
# @Site :  
# @File : logic_reg.py 
# @Software: PyCharm

import pandas as pd
from sklearn.linear_model import LogisticRegression


def getDataFrameResTable(res, i):
    resHtml = res.tables[i].as_html()
    temp = pd.read_html(resHtml)[0]
    return temp.to_json(orient='index')

def test_logic(X, y):
    '''

    :param X:
    :param y:
    :return:
    '''
    lr = LogisticRegression(penalty='l2', C=10)
    # 训练
    lr.fit(X, y)

    preResult = lr.predict_proba(X)
    predicResult = lr.predict(X)
    print(preResult)
    print('xxxxxxxxx')
    print(predicResult)
    X["prediction"] = preResult[:, -1]
    X['pre_data'] = predicResult
    print(X)




if __name__ == '__main__':
    print('xxx')
    df = pd.read_csv(r'C:\Users\BBD\Desktop\test\tmp\Cshl0V1SGLeAb6opAABKW103UTU063.csv')
    print(df)
    y = df['编号']
    X = df[['商场ID', '商户ID', '单位面积营业额', '客流转换率变化情况']]
    test_logic(X, y)