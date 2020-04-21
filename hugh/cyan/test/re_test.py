#!/usr/bin/env python
# -- coding: utf-8 --#
# @Time : 2020/4/21 11:11 
# @Author : Aries 
# @Site :  
# @File : re_test.py 
# @Software: PyCharm

import re


'''
正则测试
'''

if __name__ == '__main__':
    '''
    正则测试
    '''

    # 去除非中文开头
    s = 'zhans1e3张三黄123zhangsan李四色的'
    exp_ch = re.compile('[\u4e00-\u9fa5]')

    while True and s:
        if not exp_ch.match(s[0]):
            s = s[1:]
        else:
            break
    print(s)

    # 去除特殊字符
    # 去除特殊字符
    s = '中国~;!?kdls！?zhog红啊都￥流^&口水'
    exp = re.compile('[*；！?@#￥%……^&，。_ ~;!?,.$]')
    s = exp.sub('', s)
    print(s)

    s = '宏 huan 宏'
    s = s.replace(' ', '')
    print(s)