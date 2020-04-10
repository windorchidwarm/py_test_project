#!/usr/bin/env python
# -- coding: utf-8 --#
# @Time : 2020/4/10 13:31 
# @Author : Aries 
# @Site :  
# @File : test_fastdfs.py 
# @Software: PyCharm

from fdfs_client.client import *



FDFSDATA = {'host_tuple': ['10.20.10.41'], 'port': 22122, 'timeout': 60, 'name': 'Tracker Pool'}
client = Fdfs_client(FDFSDATA)


def down_load_file(remote_path, local_path):
    buff = client.download_to_buffer(remote_path)
    if os.path.isfile(local_path):
        os.remove(local_path)
    f = open(local_path, 'xb')
    f.write(buff['Content'])
    f.flush()

def upload_file(local_path):
    remote_data = client.upload_by_filename(local_path)
    return remote_data['Remote file_id']


if __name__ == '__main__':
    local = r'C:\Users\BBD\Desktop\test\tmp\tt.csv'
    remote = b'group1/M00/03/3A/ChQUAV6QAsOAFLAyAAA3qyMf10Y193.csv'
    down_load_file(remote, local)
