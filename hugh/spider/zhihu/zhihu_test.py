#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : zhihu_test.py
# Author: chen
# Date  : 2020-04-06



from hugh.spider.utils import html_utils

from bs4 import BeautifulSoup
# beautifulsoup4 lxml html5lib


root_path = r'C:\Users\yhchen\Desktop\test\mike'

if __name__ == '__main__':
    print('xxxxxxxxx')
    # root_url = 'http://www.baidu.com'
    # root_url = 'https://www.zhihu.com/question/19787945?sort=created&page=2'
    # root_url = 'https://www.zhihu.com/people/su-meng-xi'
    root_url = 'https://www.zhihu.com/people/su-meng-xi'
    html = html_utils.get_html(root_url)
    print(html)

    soup = BeautifulSoup(html, 'lxml')
    prettify_html = soup.prettify()
    # print(prettify_html)
    p_soup = BeautifulSoup(prettify_html, 'lxml')
    # print(p_soup)
    m_data = p_soup.find_all(name='div', attrs={'class': 'ProfileHeader-content'})
    for n in m_data:
        print(n)
    print('------------------------')
    data = p_soup.find_all(name='a', attrs={'class': 'UserLink-link', 'data-za-detail-view-element_name': 'User'})
    for i in data:
        print(i)
        print(i['href'])