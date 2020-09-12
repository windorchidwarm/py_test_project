#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : test_pyhive.py
# Author: hugh
# Date  : 2020/8/28


from krbcontext.context import krbcontext
# from krbcontext import krbcontext
from pyhive import sqlalchemy_hive,hive
from impala import dbapi
import requests, csv, time

from hdfs.ext.kerberos import KerberosClient

config = {
    "kerberos_principal": "hive@CSDNTEST.COM.LOCAL",
    "keytab_file": '/home/tools/wyk/keytab/hive.keytab',
    "kerberos_cache_file": '/home/tools/wyk/keytab/hive_ccache_uid',
    "AUTH_MECHANISM": "GSSAPI"
}

import requests
from requests.packages import urllib3

urllib3.disable_warnings()
session = requests.Session()

from requests.adapters import HTTPAdapter
import ssl
from requests.sessions import HTTPAdapter
from urllib3.poolmanager import PoolManager

class MyAdapter(HTTPAdapter):
    def init_poolmanager(self, connections, maxsize):
        self.poolmanager = PoolManager(num_pools=connections,
            maxsize=maxsize,
            ssl_version=ssl.PROTOCOL_SSLv3)


with krbcontext(using_keytab=True,
                               principal=config['kerberos_principal'],
                               keytab_file=config['keytab_file'],
                               ccache_file=config['kerberos_cache_file']):
    # hive.Connection()
    con = hive.connect(host='uatnd02.csdntest.com.local', port=10000, auth='KERBEROS',
                       kerberos_service_name="hive")  # host为hiveserver2所在节点，port默认10000，为hs2的端口
    cursor = con.cursor()
    cursor.execute('select * from dl_nccp.account limit 5')  # 不能有分号！
    # cursor.execute('desc dl_nccp.account') #不能有分号！
    datas = cursor.fetchall()
    print(datas)
    cursor.close()
    con.close()

    conn = dbapi.connect(host='uatnd02.csdntest.com.local', port=10000, auth_mechanism='GSSAPI',
                       kerberos_service_name="hive")
    cursor = conn.cursor()

    # hdfs kerberos
    client = KerberosClient('http://hdfs_ip:50070', hostname_override="hdfs域名")
    client._list_status()
    client.list()
    client.delete()
    client.upload()
    client.download()
    client.makedirs('test')