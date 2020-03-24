#!/usr/bin/env python
# -- coding: utf-8 --#
# @Time : 2020/3/16 11:01 
# @Author : Aries 
# @Site :  
# @File : time_serise_ar.py 
# @Software: PyCharm

# coding: utf-8
from __future__ import print_function
import numpy as np
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.contrib.timeseries.python.timeseries import  NumpyReader
import pandas as pd
from hugh.onon.guiyang.local_uitils import *


def to_output(predict, predict_name):
    df = pd.DataFrame(predict)
    df.columns = [predict_name]
    return df

def main(_):
    x = np.array(range(1000))
    noise = np.random.uniform(-0.2, 0.2, 1000)
    y = np.sin(np.pi * x / 100) + x / 200. + noise
    print(x, y)
    # plt.plot(x, y)
    # plt.savefig('timeseries_y.jpg')

    data = {
        tf.contrib.timeseries.TrainEvalFeatures.TIMES: x,
        tf.contrib.timeseries.TrainEvalFeatures.VALUES: y,
    }

    df = pd.read_csv(r'C:\Users\BBD\Desktop\test\tmp\Cshl0V1SGLeAb6opAABKW103UTU063.csv')
    data = {
        tf.contrib.timeseries.TrainEvalFeatures.TIMES: df['商场ID'].values,
        tf.contrib.timeseries.TrainEvalFeatures.VALUES: df['单位面积营业额'].values,
    }

    reader = NumpyReader(data)

    train_input_fn = tf.contrib.timeseries.RandomWindowInputFn(
        reader, batch_size=16, window_size=40)

    ar = tf.contrib.timeseries.ARRegressor(
        periodicities=200, input_window_size=30, output_window_size=10,
        num_features=1,
        loss=tf.contrib.timeseries.ARModel.NORMAL_LIKELIHOOD_LOSS)

    ar.train(input_fn=train_input_fn, steps=6000)

    evaluation_input_fn = tf.contrib.timeseries.WholeDatasetInputFn(reader)
    # keys of evaluation: ['covariance', 'loss', 'mean', 'observed', 'start_tuple', 'times', 'global_step']
    evaluation = ar.evaluate(input_fn=evaluation_input_fn, steps=1)

    pre_data = ar.predict(
        input_fn=tf.contrib.timeseries.predict_continuation_input_fn(
            evaluation, steps=250))
    print('xxxxxxxxxxxxxxxxxx')
    print(pre_data)
    (predictions,) = tuple(pre_data)
    print('xxxxxxxxxxxxxxxxxxxxxxxxx')
    print(predictions)
    print(type(predictions))
    pre_df = None
    for key in predictions:
        data = predictions[key].reshape(-1)
        print(data)
        data = np.nan_to_num(data)
        print(data)
        df = to_output(data, key)
        pre_df = pd.concat([pre_df, df], axis=1) if pre_df is not None else df
        print(df)
        print(key + '---< ' +str(predictions[key]))
        print(key + '&&&---> ' + str(predictions[key].reshape(-1)))

    print(pre_df)
    pre_df.to_csv(r'C:\Users\BBD\Desktop\test\tmp\12345.csv')
    data_dis = dataDistributionLocal(pre_df)
    print('3333333333333333')
    print(data_dis)

    #
    #
    # plt.figure(figsize=(15, 5))
    # plt.plot(data['times'].reshape(-1), data['values'].reshape(-1), label='origin')
    # plt.plot(evaluation['times'].reshape(-1), evaluation['mean'].reshape(-1), label='evaluation')
    # plt.plot(predictions['times'].reshape(-1), predictions['mean'].reshape(-1), label='prediction')
    # plt.xlabel('time_step')
    # plt.ylabel('values')
    # plt.legend(loc=4)
    # plt.savefig('predict_result.jpg')


if __name__ == '__main__':
    tf.logging.set_verbosity(tf.logging.INFO)
    tf.app.run()