#!/usr/bin/env python
# -- coding: utf-8 --#

from urllib import request
import bs4
from bs4 import BeautifulSoup

def getHtml(url):
    html = request.urlopen(url)
    print(html.getcode())
    html = html.read().decode()
    return html

def content(html):
    #内容分割标签
    str = '<article class="article-content">'
    content = html.partition(str)[2]
    str1 = '<div class="article-social">'
    content = content.partition(str1)[0]
    return content

def title(content, beg = 0):
    #思路是利用str.index()和序列的切片
    try:
        title_list = []
        while True:
            num1 = content.index('】', beg)
            num2 = content.index('</p>', num1)
            title_list.append(content[num1+3:num2])
            beg = num2
    except ValueError:
        return title_list

def get_img(content, beg=0):
    img_list = []
    try:
        while True:
            src1 = content.index('http', beg)
            src2 = content.index('" /></p>', src1)
            img_list.append(content[src1:src2])
            beg = src2
    except ValueError:
        pass
    try:
        while True:
            src1 = content.index('http', beg)
            src2 = content.index('[/img]', src1)
            img_list.append(content[src1:src2])
            beg = src2
    except ValueError:
        pass
    return img_list

def data_out(data):
    with open(r'', 'a+') as fo:
        fo.write('\n')
        fo.write('\n'.join(data))

def data_out(title, img):
    with open(r'', 'a+') as fo:
        fo.write('\n')
        size = 0
        for size in range(0, len(title)):
            fo.write(title[size] + "$" + img[size] + '\n')

if __name__ == '__main__':
    html = getHtml("http://bohaishibei.com/post/10475/")
    content = content(html)
    print(content)
    title = title(content)
    img = get_img(content)
    print(title)
    print(img)