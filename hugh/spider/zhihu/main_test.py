#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : main_test.py
# Author: chen
# Date  : 2020-04-06

from hugh.spider.utils import html_utils

from bs4 import BeautifulSoup
# beautifulsoup4 lxml html5lib


root_path = r'C:\Users\yhchen\Desktop\test\mike'

if __name__ == '__main__':
    print('xxxxxxxxx')
    # root_url = 'http://www.baidu.com'
    root_url = 'http://www.ziyexing.com/files-5/zzbj_index.htm'
    html = html_utils.get_html(root_url)
    print(html)

    soup = BeautifulSoup(html, 'lxml')
    # print(soup)
    # print(soup.title)
    # print(soup.a)
    # print(soup.center.table.children)

    # for data in soup.center.table.children:
    #     print('xxxxxxx')
    #     if 'href="zhouyi' in str(data):
    #         m_data = data.table.table.center.tr.td.td.div.center.table
    #         # print('end----------------')
    #         for d_data in m_data.children:
    #             if 'href="' in str(d_data):
    #                 for h_data in d_data.children:
    #                     if 'href="' in str(h_data):
    #                         for g_data in h_data.children:
    #                             if 'href="' in str(g_data):
    #                                 for k_data in g_data.children:
    #                                     if 'href="' in str(k_data):
    #                                         print(k_data)
    #                                     print('555555555555555555555555')
    #                         # print(h_data)
    #                     print('&&&&&&&&&&&&&&&&&&&&')
    #             print('end----------------')
    # print(soup.a.attrs['href'])

    data = soup.find_all(name='a', target='_blank')
    for n in data:
        print(n['href'])
    # u_html = soup.prettify()