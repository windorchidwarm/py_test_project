# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 13:52:40 2018

@author: wangfuzheng
"""

import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegressionCV
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import roc_auc_score
import matplotlib.pyplot as plt
import seaborn as sns
import os

os.chdir('F:\\data\\redalert')

class RedAlert(object):
    def __init__(self,outlier_size):
        self.data = None
        self.feature_list = None
        self.sample_size = None
        self.outlier_size = outlier_size
        self.data_balance = None
        self.data_scaled = None
        self.mean = None
        self.var = None
        self.scaler = None
        self.coef = None
        self.lr_proba = None
        self.gbdt_proba = None
        self.gbdt = None
        self.roc_auc = None
        self.lr_roc_auc = None
    #异常值处理    
    def outlier_proprecessing(self,data):
        data.fillna(method='bfill',inplace=True)
        #生成特征列表
        feature_list = []
        for i in data.columns:
            if i[:7]=='feature':
                feature_list.append(i)
        self.feature_list = feature_list
        #data的统计描述
        data_describe = data[self.feature_list].describe(
                                         percentiles=[self.outlier_size])
        #将异常值填充为空值
        for j in self.feature_list:
            #当99.5分位为1时说明大部分均为0或者1，则不存在异常值
            if data_describe.loc['99.5%',j]==1:
                pass
            elif data_describe.loc['99.5%',j]==0:
                pass
            elif data_describe.loc['99.5%',j]!=0 &(
                    float(data_describe.loc['max',j])/float(data_describe.loc['99.5%',j])<10):
                pass
            else:               
                data[j] = data[j].map(
                        lambda x: 
                        x if x< data_describe.loc['99.5%',j]
                        else None)
        self.data = data.dropna(axis=0)
    #样本不平衡处理    
    def imbalance(self,data):
        self.sample_size = 30*len(data[data['label']==1])
        white = self.data[self.data['label']==0]
        black = self.data[self.data['label']==1]
        white_sample = white.sample(n=self.sample_size)
        self.data_balance = pd.concat([white_sample,black])
    #逻辑回归数据标准化处理
    def standardscaler(self):
        scaler = StandardScaler()
        self.data_scaled = scaler.fit_transform(self.data[self.feature_list])
        self.mean = scaler.mean_
        self.var = scaler.var_
        self.scaler = scaler
    #搭建逻辑回归模型    
    def logistic(self):
        data_balance_scaled = self.scaler.fit_transform(
                                         self.data_balance[self.feature_list])
        lr = LogisticRegressionCV(Cs=10,cv=5)
        lr.fit(data_balance_scaled,self.data_balance['label'])
        self.coef = lr.coef_
        self.lr_proba = lr.predict_proba(self.data_scaled)
    #搭建GBDT模型
    def GBDT(self):
        gbdt = GradientBoostingClassifier(n_estimators=600,learning_rate=0.01, 
                                          min_samples_split=1200,
                                          min_samples_leaf=50,
                                          max_depth=5, subsample=0.8,
                                          random_state=10,loss= 'exponential')
        gbdt.fit(self.data_balance[self.feature_list],self.data_balance['label'])
        self.gbdt_proba = gbdt.predict_proba(self.data[self.feature_list])
        self.gbdt = gbdt
    #对总体数据预测的AUC值
    def roc_auc(self):
        self.gbdt_roc_auc = roc_auc_score(self.data['label'],self.gbdt_proba[:,1])
        self.lr_roc_auc = roc_auc_score(self.data['label'],self.lr_proba[:,1])
    #黑白样本识别图   
    def plot(self,data):
        plt.figure(figsize=[8,4])
        plt.title(u'总体评分')
        sns.distplot(data.iloc[:,0]**0.2*100,bins=range(0,100,1),norm_hist=True)
        plt.show()
        
        plt.figure(figsize=[8,4])
        plt.title(u'总体黑白样本评分')
        sns.distplot(data[data['label']==1].iloc[:,0]**0.2*100,
                     bins=np.linspace(0,100,100),color = '#FF0000',label = 'black')
        sns.distplot(data[data['label']==0].iloc[:,0]**0.2*100,
                     bins=np.linspace(0,100,100),color = '#00FF00',label = 'white')
        plt.legend()
        plt.show()
        
        B201708 = plt.hist(data[data['label']==1].iloc[:,0]**0.2*100,normed=True,bins=range(0,100,1))
        W201708 = plt.hist(data[data['label']==0].iloc[:,0]**0.2*100,normed=True,bins=range(0,100,1))
        
        Black08 = B201708[0]
        Black08_accum = np.add.accumulate(Black08)
        White08 = W201708[0]
        White08_accum = np.add.accumulate(White08)
        ks = max(White08_accum - Black08_accum)
        axv = list(White08_accum - Black08_accum).index(ks)
        plt.figure(figsize=[8,4])
        plt.title(u'累计图')
        plt.plot(Black08_accum,'-',color = '#FF0000',label = 'Black')
        plt.plot(White08_accum,'-',color = '#00FF00',label = 'White')
        plt.axvline(axv)
        plt.show()
        return ks,axv
if __name__ == '__main__':
    data = pd.read_csv('.\\data_redalert_5.csv')
    redalert = RedAlert(0.995)
    redalert.outlier_proprecessing(data)
    redalert.imbalance(data)
    redalert.standardscaler()
    redalert.logistic()
    redalert.GBDT()
    gbdt_proba = pd.DataFrame(redalert.gbdt_proba)
    gbdt_proba['label'] = redalert.data['label']
    redalert.plot(gbdt_proba)
    
        