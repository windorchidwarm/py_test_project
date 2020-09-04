#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : test_pyhive.py
# Author: hugh
# Date  : 2020/8/28


from krbcontext.context import krbcontext
from pyhive import sqlalchemy_hive,hive

config = {
    "kerberos_principal": "hive@CSDNTEST.COM.LOCAL",
    "keytab_file": '/home/tools/wyk/keytab/hive.keytab',
    "kerberos_ccache_file": '/home/tools/wyk/keytab/hive_ccache_uid',
    "AUTH_MECHANISM": "GSSAPI"
}

with krbcontext(using_keytab=True,
                               principal=config['kerberos_principal'],
                               keytab_file=config['keytab_file'],
                               ccache_file=config['kerberos_ccache_file']):
    con = hive.connect(host='uatnd02.csdntest.com.local', port=10000, auth='KERBEROS',
                       kerberos_service_name="hive")  # host为hiveserver2所在节点，port默认10000，为hs2的端口
    cursor = con.cursor()
    cursor.execute('select * from dl_nccp.account limit 5')  # 不能有分号！
    # cursor.execute('desc dl_nccp.account') #不能有分号！
    datas = cursor.fetchall()
    print(datas)
    cursor.close()
    con.close()