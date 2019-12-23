#!/usr/bin/env python
# -- coding: utf-8 --#

from fdfs_client.client import *

FDFSDATA = {'host_tuple': ['10.200.101.205','10.200.101.209'], 'port': 22122, 'timeout': 60, 'name': 'Tracker Pool'}
client = Fdfs_client(FDFSDATA)
outHdfs =  b'group1/M00/00/00/Cshl0Vz_UmmAGehCArZwOzMgNHo277.csv'
buff = client.download_to_buffer(outHdfs)
localPath = '/home/bbd/tetris/schedule/logs/tt.csv'
if os.path.isfile(localPath):
    os.remove(localPath)

f = open(localPath, 'xb')
f.write(buff['Content'])
f.flush()