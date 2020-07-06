#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : apriori_test.py
# Author: hugh
# Date  : 2020/7/3


import efficient_apriori
import fptools

import os

from lxml import etree
from selenium import webdriver
import time
import csv


base_path = os.path.dirname(os.path.realpath(__file__))\
    .replace(os.path.join('hugh', os.path.join('base_some', 'base_data_ana')), '')
print(base_path)
file_dir = os.path.join(base_path, 'apriori')



def download(request_url, director, flags, csv_write):
    '''

    :param request_url:
    :return:
    '''
    driver = webdriver.Chrome()
    driver.get(request_url)
    time.sleep(1)

    html = driver.find_element_by_xpath('//*').get_attribute('outerHTML')
    html = etree.HTML(html)
    # 设置电影名称，导演演员的 xpath
    movie_lists = html.xpath("/html/body/div[@id='wrapper']/div[@id='root']/div[1]//div[@class='item-root']/div[@class='detail']/div[@class='title']/a[@class='title-text']")
    name_lists = html.xpath("/html/body/div[@id='wrapper']/div[@id='root']/div[1]//div[@class='item-root']/div[@class='detail']/div[@class='meta abstract_2']")

    # 获取返回数据个数
    num = len(movie_lists)
    if num > 15: # 第一页16条数据
        # 默认第一条部署 所以需要去掉
        movie_lists = movie_lists[1:]
        name_lists = name_lists[1:]

    for (movie, name_list) in zip(movie_lists, name_lists):
        # 可能会 存在为空的情况下
        if name_list.text is None:
            continue
        # 显示演员名称
        print(name_list.text)
        names = name_list.text.split('/')
        # 判断导演是否为指定的director
        if names[0].strip() == director and movie.text not in flags:
            # 将第一个字段设置为电影名称
            names[0] = movie.text
            flags.append(movie.text)
            csv_write.writerow(names)
    print('OK')
    # 代表这页数据下载成功
    print(num)
    if num >= 14:
        #有可能一页会有14个电影
        # 继续下一页
        return True
    else:
        # 没有下一页
        return False



def test_apriori_main_data(director, file_name):
    '''

    :return:
    '''
    # director = '宁浩'
    # file_name = os.path.join(file_dir, director + '.csv')
    base_url = 'https://movie.douban.com/subject_search?search_text='+director+'&cat=1002&start='
    out = open(file_name, 'w', newline='', encoding='utf-8-sig')
    csv_wirte = csv.writer(out, dialect='excel')
    flags = []

    start = 0
    while start < 10000:
        request_url = base_url + str(start)
        flag = download(request_url, director, flags, csv_wirte)
        if flag:
            start = start + 15
        else:
            break
    out.close()
    print('finished')


def test_apriori_main():
    '''
    一般来说最小支持度常见的取值有0.5，0.1, 0.05。最小置信度常见的取值有1.0, 0.9, 0.8。
    可以通过尝试一些取值，然后观察关联结果的方式来调整最小值尺度和最小置信度的取值。
    :return:
    '''
    director = '宁浩'
    file_name = os.path.join(file_dir, director + '.csv')
    test_apriori_main_data(director, file_name)

    lists = csv.reader(open(file_name, 'r', encoding='utf-8-sig'))
    data = []
    for names in lists:
        name_new = []
        for name in names:
            # 去掉演员数据中的空格
            name_new.append(name.strip())
        data.append(name_new[1:])
    itemsets, rules = efficient_apriori.apriori(data, min_support=0.5, min_confidence=1)
    print(itemsets)
    print(rules)





def test_apriori():
    '''

    :return:
    '''
    data = [('牛奶','面包','尿布'), ('可乐','面包', '尿布', '啤酒'),
            ('牛奶','尿布', '啤酒', '鸡蛋'), ('面包', '牛奶', '尿布', '啤酒'),
            ('面包', '牛奶', '尿布', '可乐')]
    itemsets, rules = efficient_apriori.apriori(data, min_support=0.5, min_confidence=1)
    print(itemsets)
    print(rules)
    print(dir(fptools))

    fptools.FPTree()
    fptools.fpgrowth()

if __name__ == '__main__':
    '''
    关联规则挖掘 Apriori
    
    支持度 置信度 提升度
    支持度=出现次数/总次数 即p(A)
    置信度(A->B)=p(B|A)
    提升度(A->B)=置信度/支持度 即p(B|A)/P(B) >1 代表有提升 =1 关联不大 <1 有下降
    
    Apriori算是就是查找频繁项集(frequent itemset)的过程
    频繁项集就是支持度大于等于最小支持度 (Min Support) 阈值的项集
    递归流程：
    1.K=1，计算K项集的支持度
    2.筛选掉小于最小支持度的项集
    3.如果想项集为空，则对应K-1项集的结果为最终结果
    否则K=K+1，重复1-3
    
    Apriori缺点：
    1.可能产生大量候选集
    2.每次计算都需要重新扫描数据集，来计算每个项集的支持力度
    
    改进：FP-Grouth算法
    特点：1.创建一颗FP树来存储频繁子集。在创建前对不满足最小支持力度的项进行删除，减少了存储空间。
          2.整个生成过程只遍历数据集2次，大大减少了计算量。
    原理：1.创建项头表(item header table)
            创建项头表的作用是为 FP 构建及频繁项集挖掘提供索引。
            **这一步的流程是先扫描一遍数据集，对于满足最小支持度的单个项（K=1 项集）按照支持度从高到低进行排序，这个过程中删除了不满足最小支持度的项。
            项头表包括了项目、支持度，以及该项在 FP 树中的链表。初始的时候链表为空。
          2.构造FP树
            FP 树的根节点记为 NULL 节点。
            整个流程是需要再次扫描数据集，对于每一条数据，按照支持度从高到低的顺序进行创建节点
            （也就是第一步中项头表中的排序结果），节点如果存在就将计数 count+1，
            如果不存在就进行创建。同时在创建的过程中，需要更新项头表的链表。
            1）遍历第1条数据，得到
            尿布1 |牛奶1 |面包1
            2）遍历第2条数据，得到
            尿布2 |面包1 |啤酒1
                     |牛奶1 |面包1
            3）遍历第3条数据，得到
            尿布3 |面包1 |啤酒1
                     |牛奶2 |面包1
                              |啤酒1
            4）遍历第4条数据，得到
            尿布4 |面包1 |啤酒1
                     |牛奶3 |面包2 |啤酒1
                              |啤酒1
            5）遍历第5条数据，得到
            尿布5 |面包1 |啤酒1
                     |牛奶4 |面包3 |啤酒1
                              |啤酒1
          3.通过 FP 树挖掘频繁项集
            “条件模式基”：指的是以要挖掘的节点为叶子节点，自底向上求出 FP 子树，然后将 FP 子树的祖先节点设置为叶子节点之和。
            
    '''
    test_apriori()