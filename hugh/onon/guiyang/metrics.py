#!/usr/bin/env python
# -- coding: utf-8 --#
# @Time : 2020/3/24 14:08 
# @Author : Aries 
# @Site :  
# @File : metrics.py 
# @Software: PyCharm

import pandas as pd
from sklearn import metrics
import math
import numpy as np
import json

def test_metris(y_valid, y_predict, metricsList):
    result = {}
    print(y_valid)
    print(y_predict)
    for em in metricsList:
        if em == 'confusion_matrix':
            data = metrics.confusion_matrix(y_valid, y_predict)
            result[em] = data.tolist()
        elif em == 'f1_score':
            result[em] = metrics.f1_score(y_valid, y_predict)
        elif em == 'accuracy':
            result[em] = metrics.accuracy_score(y_valid, y_predict)
        elif em == 'recall':
            result[em] = metrics.recall_score(y_valid, y_predict)
        elif em == 'mse':
            result[em] = metrics.mean_squared_error(y_valid, y_predict)
        elif em == 'rmse':
            result[em] = math.sqrt(metrics.mean_squared_error(y_valid, y_predict))
        elif em == 'roc_auc_score':
            result[em] = metrics.roc_auc_score(y_valid, y_predict)
        else:
            raise Exception("非法的评估方式")
    print(result)
    dataDistJson = json.dumps({"0": result})
    print(dataDistJson)

if __name__ == '__main__':
    print('xxx')
    df = pd.read_csv(r'C:\Users\BBD\Desktop\test\tmp\Cshl0V1SGLeAb6opAABKW103UTU063.csv')
    print(df)
    y_valid = df['是否掉铺'].values
    y_predict = df['是否掉铺'].values
    # y_valid = y_predict
    print(type(y_valid))
    test_metris(y_valid, y_predict, ['confusion_matrix', 'f1_score', 'accuracy', 'recall', 'mse', 'rmse', 'roc_auc_score'])