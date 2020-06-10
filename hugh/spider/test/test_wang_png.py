#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : test_wang_png.py
# Author: hugh
# Date  : 2020/5/27

import requests
import json


def download(src, id):
    dir = './' + str(id) + '.jpg'
    try:
        pic = requests.get(src, timeout=10)
        fp = open(dir, 'wb')
        fp.write(pic.content)
        fp.close()
    except requests.exceptions.ConnectionError:
        print('图片无法下载')


if __name__ == '__main__':
    '''
    下载
    '''
    query = '王祖贤'
    ''' 下载图片 '''

    ''' for 循环 请求全部的 url '''
    for i in range(0, 22471, 20):
        url = 'https://www.douban.com/j/search_photo?q=' + query + '&limit=20&start=' + str(i)
        print(url)
        # 估计是代理问题 跑出来为空 后续解决
        html = requests.get(url).text  # 得到返回结果
        print(html)
        response = json.loads(html, encoding='utf-8') # 将 JSON 格式转换成 Python 对象
        for image in response['images']:
            print(image['src']) # 查看当前下载的图片网址 download(image['src'], image['id']) # 下载一张图片