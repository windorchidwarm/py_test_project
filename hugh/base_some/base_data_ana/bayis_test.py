#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : bayis_test.py
# Author: hugh
# Date  : 2020/6/29


from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import naive_bayes
import nltk
import jieba

def test_nltk(text):
    '''
    英文分词
    :param text:
    :return:
    '''
    word_list = nltk.word_tokenize(text) # 分词
    print(word_list)
    nltk.pos_tag(word_list) # 标注到此的词性
    print(word_list)


def test_jieba(text):
    word_list = jieba.cut(text) # 中文分词
    print(word_list)


def test_tfidf_vectorizer():
    '''
    停用词就是在分类中没有用的词，这些词一般词频 TF 高，但是 IDF 很低，起不到分类的作用。
    为了节省空间和计算时间，我们把这些词作为停用词 stop words，告诉机器这些词不需要帮我计算
    TfidfVectorizer
    stop_words list
    token_pattern 过滤规则 正则表达式
    fit_transform后
    vocabulary_ 词汇表 字典型
    idf_ 返回idf值
    stop_words_ 返回停用词表
    :return:
    '''
    tfidf_vec = TfidfVectorizer()
    print(tfidf_vec)
    documents = [
        'this is the bayes document',
        'this is the second document',
        'and the third one',
        'is this the document'
    ]
    tfidf_matrix = tfidf_vec.fit_transform(documents)
    print(tfidf_vec.get_feature_names())
    print(tfidf_vec.get_stop_words())
    print(tfidf_vec.get_params())
    print(tfidf_vec.vocabulary_)
    print(tfidf_matrix.toarray())

    # 当 alpha=1 时，使用的是 Laplace 平滑。Laplace 平滑就是采用加 1 的方式，
    # 来统计没有出现过的单词的概率。这样当训练样本很大的时候，加 1 得到的概率变化可以忽略不计，
    # 也同时避免了零概率的问题
    # 当 0<alpha<1 时，使用的是 Lidstone 平滑。对于 Lidstone 平滑来说，alpha 越小，
    # 迭代次数越多，精度越高。我们可以设置 alpha 为 0.001。
    # clf = naive_bayes.MultinomialNB(alpha=0.001).fit()
    # test_nltk('this is a good time')
    # test_jieba('中华人民共和国')


if __name__ == '__main__':
    '''
    贝叶斯相关内容学习
    先验概率 后验概率 条件概率
    似然函数
    
    p(A|B1)=0.999 p(A|B2)=0.001 p(B1)=0.0001 p(B2)=0.9999
    p(B1,A)=p(B1)*p(A|B1) = 0.00009999
    p(B2,A)=p(B2)*p(A|B2)=0.9999*0.001=0.0009999
    
    p(Bi|A)=p(Bi)*p(A|Bi)/(Σp(Bi)*p(A|Bi))
    
    朴素贝叶斯
    两种类型概率
    1.每个类别的概率p(Cj)
    2.每个属性的条件概率p(Ai|Cj)
    eg:假设7个棋子，其中3个白色，4个黑色。那么棋子的白色概率为3/7，黑色的概率为4/7.这是类别概率。
    如果把7个棋子放到两个盒子，其中A盒里面有2个白旗，2个黑棋；B盒里面一个白棋，2个黑棋。
    那么在盒子A中抓到白棋的概率是1/2，这是条件概率。
    
    贝叶斯原理 贝叶斯分类 朴素贝叶斯
    离散数据 计算概率
    连续数据 得到正态分布的密度函数
    累积分布和概率密度
    
    分别是高斯朴素贝叶斯（GaussianNB）、多项式朴素贝叶斯（MultinomialNB）和伯努利朴素贝叶斯（BernoulliNB）。
    高斯朴素贝叶斯：特征变量是连续变量，符合高斯分布，比如说人的身高，物体的长度。
    多项式朴素贝叶斯：特征变量是离散变量，符合多项分布，在文档分类中特征变量体现在一个单词出现的次数，或者是单词的 TF-IDF 值等。
    伯努利朴素贝叶斯：特征变量是布尔变量，符合 0/1 分布，在文档分类中特征是单词是否出现。
    
    F-IDF 实际上是两个词组 Term Frequency 和 Inverse Document Frequency 的总称，
    两者缩写为 TF 和 IDF，分别代表了词频和逆向文档频率。
    
    '''

    test_tfidf_vectorizer()