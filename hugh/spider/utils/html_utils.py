#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : html_utils.py
# Author: chen
# Date  : 2020-04-06

import urllib.request

def get_html(url):
    '''
    获取html网页
    :param url:
    :return:
    '''
    html = urllib.request.urlopen(url).read()
    return html

def save_html(file_name, file_content):
    '''
    保存网页
    :param file_name:
    :param file_content:
    :return:
    '''
    with open(file_name, 'wb') as f:
        f.write(file_content)