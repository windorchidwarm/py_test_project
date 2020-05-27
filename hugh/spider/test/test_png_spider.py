#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : test_png_spider.py
# Author: BBD
# Date  : 2020/5/27

from urllib import request
from lxml import etree

if __name__ == '__main__':
    '''
    爬虫获取
    '''
    r = request.urlopen('http://www.baidu.com').read()
    print(r)
    html = etree.HTML(r.decode())
    print(html)
    print(html.xpath('//div'))