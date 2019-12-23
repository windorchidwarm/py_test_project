#!/usr/bin/env python
# -- coding: utf-8 --#

from fdfs_client.client import *

#10.28.200.226
# FDFSDATA = {'host_tuple': ['10.28.200.185'], 'port': 22122, 'timeout': 60, 'name': 'Tracker Pool'}
# outHdfs = 'group1/M00/06/EC/ChzI4lzbdQOAKo11AAACRHLx9u0758.csv'
# outHdfs = outHdfs.encode('utf-8')
# print(outHdfs)
# f2 = outHdfs.decode('utf-8').encode('utf-8')
# print(f2)  b'group1/M00/00/00/ChzIuFzwyQmARBSmAHt1Hf0UIKs627.csv'
#
FDFSDATA = {'host_tuple': ['10.200.101.205','10.200.101.209'], 'port': 22122, 'timeout': 60, 'name': 'Tracker Pool'}
client = Fdfs_client(FDFSDATA)
# r'' CLIENT_ADVISOR_STAGING_16_20190201_106628.csv qyxx_basic.xlsx test_data.csv
tt = client.upload_by_filename(r'C:\Users\Administrator\Desktop\test\tmp\经营信息_餐饮美食.csv')
print(tt)
# outHdfs = tt['Remote file_id']
# outHdfs = b'group1/M00/00/F2/Cshl0V0xM8qAFkN_AABLazT1ReI002.csv'
# buff = client.download_to_buffer(outHdfs)
# localPath = r'C:\Users\Administrator\Desktop\test\tmp\经营信息_生活精品.csv'
# # localPath = '/home/bbders/tetris_prod/tetris-schedule/logs/tt.csv'
# if os.path.isfile(localPath):
#     os.remove(localPath)
#
# f = open(localPath, 'xb')
# f.write(buff['Content'])
# f.flush()