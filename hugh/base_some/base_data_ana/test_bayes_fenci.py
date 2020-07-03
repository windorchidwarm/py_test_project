#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : test_bayes_fenci.py
# Author: hugh
# Date  : 2020/6/29


import os,io
import jieba
import warnings
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics

base_path = os.path.dirname(os.path.realpath(__file__))\
    .replace(os.path.join('hugh', os.path.join('base_some', 'base_data_ana')), '')
print(base_path)

warnings.filterwarnings('ignore')

def cut_words(file_path):
    '''
    对文本进行分词
    :param file_path:
    :return: 用空格分词的字符串
    '''
    text_with_space = ''
    text = open(file_path, 'r', encoding='gb18030').read()
    textcut = jieba.cut(text)
    for word in textcut:
        text_with_space += word + ' '
    return text_with_space


def loadfile(file_dir, label):
    '''
    将路径下的所有文件加载
    :param file_dir:
    :param label:
    :return: 分词后的文档列表和标签
    '''
    file_list = os.listdir(file_dir)

    words_list = []
    labels_list = []
    for file in file_list:
        file_path = file_dir + '/' + file
        words_list.append(cut_words(file_path))
        labels_list.append(label)
    return words_list, labels_list

file_dir = os.path.join(os.path.join(base_path, 'files'), 'text_classification')

file_train_dir = os.path.join(file_dir, 'train')
# 训练数据
train_words_list1, train_labels1 = loadfile(os.path.join(file_train_dir, '女性'), '女性')
train_words_list2, train_labels2 = loadfile(os.path.join(file_train_dir, '体育'), '体育')
train_words_list3, train_labels3 = loadfile(os.path.join(file_train_dir, '文学'), '文学')
train_words_list4, train_labels4 = loadfile(os.path.join(file_train_dir, '校园'), '校园')

train_words_list = train_words_list1 + train_words_list2 + train_words_list3 + train_words_list4
train_labels = train_labels1 + train_labels2 + train_labels3 + train_labels4

file_test_dir = os.path.join(file_dir, 'test')
# 测试数据
test_words_list1, test_labels1 = loadfile(os.path.join(file_test_dir, '女性'), '女性')
test_words_list2, test_labels2 = loadfile(os.path.join(file_test_dir, '体育'), '体育')
test_words_list3, test_labels3 = loadfile(os.path.join(file_test_dir, '文学'), '文学')
test_words_list4, test_labels4 = loadfile(os.path.join(file_test_dir, '校园'), '校园')

test_words_list = test_words_list1 + test_words_list2 + test_words_list3 + test_words_list4
test_labels = test_labels1 + test_labels2 + test_labels3 + test_labels4

file_stop_dir = os.path.join(file_dir, 'stop')
# stop_words = open(os.path.join(file_stop_dir, 'stopword.txt'), 'r', encoding='utf-8').read()
stop_words = [line.strip() for line in open(os.path.join(file_stop_dir, 'stopword.txt'), 'r', encoding='utf-8').readlines()]

# 计算单词权重
tf = TfidfVectorizer(stop_words=stop_words, max_df=0.5)
print(tf)
train_features = tf.fit_transform(train_words_list)
test_features = tf.transform(test_words_list)

clf = MultinomialNB(alpha=0.001)
clf.fit(train_features, train_labels)
predicted_labels = clf.predict(test_features)
print(predicted_labels)
# 计算准确率
print('准确率为：', metrics.accuracy_score(test_labels, predicted_labels))