#!/usr/bin/env python
# -- coding: utf-8 --#

'''
用于测试一些引用
'''

from fdfs_client.client import *
import os
from io import BytesIO
import pandas as pd
import operator
from hugh.cyan.test.config import config


def testFDSClientUpload():
    '''
    测试
    :return:
    '''
    # path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fdfs_client.cfg')
    # conf = config.getConfSection("fdfs")
    # print(conf)
    # client = Fdfs_client(conf)
    # client = Fdfs_client({'host_tuple': ['10.28.200.226'], 'port': 22122, 'timeout': 5, 'name': 'Tracker Pool'})
    client = Fdfs_client({'host_tuple': ['10.28.200.184'], 'port': 22122, 'timeout': 5, 'name': 'Tracker Pool'})
    # lpath = client.upload_by_filename(r'C:\Users\Administrator\Desktop\test\tmp\sample_0.csv')
    # print(lpath)
    buff = client.download_to_buffer(b'group1/M00/00/00/ChzIuFzk-XaALDKRAHt1Hf0UIKs809.csv')
    f = open(r'C:\Users\Administrator\Desktop\test\tmp\aaxcsds.csv', 'wb')
    f.write(buff['Content'])
    f.flush()
    f.close()

    # lpath = client.upload_by_filename(r'C:\Users\Administrator\Desktop\test\tmp\sample_0.csv')
    # print(lpath)
    # print(lpath['Remote file_id'])
    # time.sleep(5)  # 等待5s，否则下载时会报错文件不存在
    # file_id = lpath['Remote file_id']  # 新版本文件存放Remote file_id格式变化

    # ret_delete = client.delete_file(b'group1/M00/77/D3/ChzI4lzGxWKAQmg1AHt1Hf_e2Ls463.csv')
    # print(ret_delete)

    # download

    # file_id = b'group1/M00/77/CB/ChzI4lzGrLmANGx8AHt1Hf_e2Ls8707586'
    # buff = client.download_to_buffer(file_id)
    # # print(buff)
    # # print(buff[0:100])
    #
    # localPath = r'C:\\Users\\Administrator\\Desktop\\work\\test\\dd.csv'
    #
    # if os.path.isfile(localPath):
    #     os.remove(localPath)
    #
    # f = open(localPath, 'xb')
    # f.write(buff['Content'])
    # df = pd.read_csv(localPath)
    # df.to_csv(r'C:\\Users\\Administrator\\Desktop\\work\\test\\cc.csv')
    # content = buff['Content']
    # print(type(content))

    # f.write(buff['Content'])
    # df = pd.DataFrame(buff['Content'])
    # print(df)
    # df.to_csv()
    # print(buff)
    # f = open(r'C:\\Users\\Administrator\\Desktop\\work\\test\\dd.csv', 'w')
    # f.write(str(buff))
    # f.close()
    # ret_download = client.download_to_file(r'C:\\Users\\Administrator\\Desktop\\work\\test\\mm.csv', file_id)
    # print(ret_download)

    # delete
    # ret_delete = client.delete_file(file_id)
    # print(ret_delete)


def lineSep():
    str = os.linesep
    return str

if __name__ == '__main__':
    '''
    测试一些内容
    '''
    testFDSClientUpload()

    # a = [1, 3, 5, 1]
    # b = [5, 2, 9, 5]
    # dict = dict(zip(a, b))
    # print(dict)
    # print(dict.pop(1))
    # print(dict)

    # print(lineSep())
    # a = input("dddd")
    # print(a)

    # a = 1
    # print(id(a))
    # b = 2
    # print(id(b))
    # c = 'dd'
    # print(id(c))
    # d = 'dd'
    # print(id(d))
    # print(type(d))
    # print(repr(d))
    # print(str(d))
    # print(complex(a, b))
    # print(operator.eq(a, b))
    #
    # if isinstance(a, (int, float)):
    #     print(type(a))

    # print(2//4)
    # print(2/4)
    # print(35 & 86)
    # print(39 | 24)

    # print(ord('a'))
    # print(ord(''))
    # print(hex(849349))
    # print(oct(849349))
    # print(chr(57704))
    # print(0.1)

    # print(32 & 1)
    # print(31 & 1)
    #
    # for i,t in enumerate('fdfsaf'):
    #     print(i, ' --> ', t)
    #
    # a = [1, 3, 5, 1]
    # b = [5, 2, 9, 5]
    #
    # print(list(zip(a,b)))
    # a1, b1 = zip(* zip(a,b))
    # print(list(a1))
    # print(list(b1))

    # x = [4]
    # y = x
    # y[0] = 3
    # del x
    # print(y)