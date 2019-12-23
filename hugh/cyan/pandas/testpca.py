#!/usr/bin/env python
# -- coding: utf-8 --#

'''
人脸识别demo
'''
import numpy as np
import scipy.linalg as linA
from PIL import Image
import os
import glob
import random
from sklearn.decomposition import PCA
import pandas as pd
import sqlalchemy

def sim_distance(train, test):
    '''
    计算欧氏距离相似度
    :param train: 二维训练集
    :param test: 一维测试集
    :return: 该测试集到每一个训练集的欧氏距离
    '''
    return [np.linalg.norm(i - test) for i in train]

# picture_path = 'C:\\Users\\Administrator\\Desktop\\test\\picture\\'
# array_list = []
# for i in range(6):
#     array_list.append([random.randint(0,30),random.randint(0,128),random.randint(0,75),random.randint(0,85),random.randint(0,34),random.randint(0,3670),random.randint(0,3),random.randint(0,365),random.randint(0,530)])
#
# print(array_list)
# pca = PCA(n_components=3)
# pca_model = pca.fit(array_list)
# print(pca.explained_variance_ratio_)
# print("&&&&&&&&&&&&&&&&&&&&")
# print(pca.explained_variance_)
# pca_features = pca_model.transform(array_list)
# print("&&&&&&&&&&&&&&&&&&&&")
# print(pca_features)

engienCmd = 'mysql+pymysql://{username}:{password}@{url}'.format(username='quant',
                                                                password='bbd123',
                                                                url='10.28.109.14:3306/bbd_tetris')
engine = sqlalchemy.create_engine(engienCmd, connect_args={'charset': 'utf8'})

# sample_0
sql = '''
        {sql}
    '''.format(sql='select * from t1 limit 100')
upDf = pd.read_sql_query(sql, engine)

print(upDf.columns.values.tolist())
print(len(upDf))
pca = PCA(n_components=3)
pca_model = pca.fit(upDf)
print(pca.explained_variance_ratio_)
print("&&&&&&&&&&&&&&&&&&&&")
print(pca.explained_variance_)
pca_features = pca_model.transform(upDf)
print("&&&&&&&&&&&&&&&&&&&&")
print(pca_features)
columns = ['level_0','index','job_blue_collar','job_housemaid','job_management','job_retired','job_self_employed','job_services','job_technician','job_unemployed','job_unknown','marital_divorced','marital_married','marital_single','marital_unknown','education_basic_4y','education_basic_6y','education_basic_9y','education_high_school','education_illiterate','education_professional_course','education_university_degree','education_unknown','default_no','default_unknown','default_yes','housing_no','housing_unknown','housing_yes','loan_no','loan_unknown','loan_yes','contact_cellular','contact_telephone','month_apr','month_aug','month_dec','month_jul','month_jun','month_mar','month_may', 'month_nov', 'month_oct', 'month_sep', 'day_of_week_fri', 'day_of_week_mon', 'day_of_week_thu', 'day_of_week_tue', 'day_of_week_wed', 'poutcome_failure', 'poutcome_nonexistent', 'poutcome_success', 'duration', 'pdays', 'previous', 'emp_var_rate', 'cons_price_idx', 'cons_conf_idx', 'euribor3m', 'nr_employed', 'y']
columns = ['level_0','index','job_blue_collar']
print(len(columns))
# out = pca_features.rdd.map(lambda x: tuple(x["pca_features"].toArray().tolist())).toDF(columns)
print(pd.DataFrame(pca_features, columns=columns))
out = pd.DataFrame(pca_features.T)
# out = pca_features.rdd.map(lambda x: tuple(x["pca_features"].toArray().tolist())).toDF(columns)
print(out)

# for name in glob.glob(picture_path + '*.jpg'):
# # for name in [picture_path + '1.jpg']:
#     #读取每张图片并生成灰度(0-255)的一维序列 1*120000
#     img = Image.open(name)
#     # img_binary = img.convert('1') #二值化
#     img_grey = img.convert('L') #灰度化
#     # ss = np.array(img_grey).reshape(1, 120000)
#     # print(len(ss))
#     array_list.append(np.array(img_grey).reshape(1, 120000))


# print(array_list)
# mat = np.vstack(array_list) #将上述多个一维序列合并成矩阵 3*120000
# print(mat)
# P = np.dot(mat, mat.transpose()) #计算P
# print(P)
# v, d = np.linalg.eig(P) #计算P的特征值和特征向量
# print(v)
# print(d)
# d = np.dot(mat.transpose(), d) #计算Sigma的特征向量 12000 * 3
# print(d)
# train = np.dot(d.transpose(), mat.transpose()) #计算训练集的主成分值 3*3
# print(train)
#开始测试
# test_pic = np.array(Image.open('C:\\Users\\Administrator\\Desktop\\test\\4.jpg').convert('L')).reshape(1, 120000)
# result = sim_distance(train.transpose(), np.dot(test_pic, d))
# print(result)
# test_pic = np.array(Image.open('C:\\Users\\Administrator\\Desktop\\test\\5.jpg').convert('L')).reshape((1,120000))
# result = sim_distance(train.transpose(),np.dot(test_pic,d))
# print(result)