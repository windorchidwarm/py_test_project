#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : test_https.py
# Author: hugh
# Date  : 2020/9/12


import ssl
from requests.sessions import HTTPAdapter
from urllib3.poolmanager import PoolManager
import requests

from requests.packages import urllib3

urllib3.disable_warnings()

class MyAdapter(HTTPAdapter):
    def init_poolmanager(self, connections, maxsize, block):
        self.poolmanager = PoolManager(num_pools=connections,
            maxsize=maxsize,
            ssl_version=3)

if __name__ == '__main__':
    '''
    '''
    ssl._create_default_https_context = ssl._create_unverified_context
    ss = requests.Session()
    ss.mount('https://', MyAdapter())
    ss.verify = False
    data = ss.get('https://www.baidu.com')
    print(data)