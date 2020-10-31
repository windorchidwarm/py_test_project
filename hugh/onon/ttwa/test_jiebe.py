#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : test_jiebe.py
# Author: hugh
# Date  : 2020/10/30


import requests
from bs4 import BeautifulSoup
url = "https://www.sohu.com/a/399536519_384789"
responce = requests.get(url)
soup = BeautifulSoup(responce.text, 'lxml')    # lxml用来解析网页
print('返回的访问值')  # 如果返回值为200则表示访问成功
print(responce.status_code)

links_div = soup.find("article", class_="article")
print(links_div)     # 我们可以尝试输出下获取的文本，验证是否是我们想要的
text = links_div
text = links_div.get_text().strip()  # 对字符串进行切片操作
print(text)
# 把页面内容作为对象保存在字典中，再写入本地的记事本中
import os
os.getcwd()  # 获取当前工作路径
dic = {text}
print(dic)
with open("report.txt", 'a', encoding='UTF-8')as f:
    f.write(str(dic))
    print(f)
f.close()

# 清洗
import jieba
import re
r = '[，。\%、；1234567890n]'
file = open("report.txt","r",encoding='utf-8').read()
file = re.sub(r, '', file)      #剔除无关信息
con = jieba.lcut(file)     #分词
words = " ".join(con)    #分词后插入空格
#词云分析
from wordcloud import WordCloud
font_path = "/System/Library/fonts/PingFang.ttc"
font_path = r'F:\pyworkspace\test_project\files\汉仪大隶书繁.ttf'
font_path = r'F:\pyworkspace\test_project\files\msyhbd.ttc'
print('&&&&&&&&&&&&&&&&&&&&&')
print(font_path)
print(words)
wordcloud = WordCloud(font_path=font_path, background_color="black",
                      width=800, height=660).generate(words)
#我们注意到wordcloud对中文很不友好，必须要进行jieba分词，还应该再WordCloud中增加设置字体的参数
#否则生成的词云图片是方框型的
wordcloud.to_file('nobel_pprize.png')     #保存图片