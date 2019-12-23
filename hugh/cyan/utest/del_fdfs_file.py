#!/usr/bin/env python
# -- coding: utf-8 --#
# @Time : 2019/8/13 16:05 
# @Author : Aries 
# @Site :  
# @File : del_fdfs_file.py 
# @Software: PyCharm
# 删除fdfs上未使用的文件


from fdfs_client.client import *
import os
import sqlalchemy
from sqlalchemy.orm import sessionmaker
import json


def del_file(del_file_name):
    FDFSDATA = {'host_tuple': ['10.28.200.184'], 'port': 22122, 'timeout': 60,
                'name': 'Tracker Pool'}
    client = Fdfs_client(FDFSDATA)
    for file_name in del_file_name:
        print(file_name)
        client.delete_file(file_name.encode())

def file_name(file_dir):
    file_list = []
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            file_list.append(os.path.join(root, file))
    for file_name in file_list:
        print(file_name)
    return file_list


def read_file_name():
    with open(r'C:\Users\BBD\Desktop\test\184\file_name.txt', 'r') as f:
        lines = [line.strip() for line in f.readlines()]
        list_file_name = []
        file_name_pre = 'group1/M00'
        for line in lines:
            line = line.replace('/home/fastdfs/fastdfs_storage/data', '')
            line = file_name_pre + line
            list_file_name.append(line)
        return list_file_name


def get_session():
    engienCmd = 'mysql+pymysql://{username}:{password}@{url}'.format(username='quant',
                                                                     password='bbd123',
                                                                     url='10.28.109.14:3306/bbd_tetris')
    engine = sqlalchemy.create_engine(engienCmd, connect_args={'charset': 'utf8'})
    session_factory = sessionmaker(bind=engine)
    session = session_factory()
    return session


# list转字典 根据列名
def to_dict(data, columns):
    return dict(zip(columns, data))


def node_file_name_list():
    sql = '''select id, type, location_x, location_y, is_end, end_index, property, latest_output from gxyh_node'''
    session = get_session()

    result_proxy = session.execute(sqlalchemy.text(sql))
    result_all = result_proxy.fetchall()
    my_column = ["id", "type", "location_x", "location_y", "is_end", "end_index", "property", "latest_output"]

    file_name_list = []
    for result in result_all:
        data = to_dict(result, my_column)

        if data['latest_output'] is not None and data['latest_output'] != '':
            latest_output = json.loads(data['latest_output'])
            for key in latest_output:
                if 'allDataPath' in latest_output[key]:
                    # jupyter中的数据读取为str，其它为dict
                    m_data = latest_output[key]
                    if isinstance(latest_output[key], str):
                        m_data = json.loads(m_data)
                    display_path = m_data['displayDataPath'].replace('\"', '')
                    all_path = m_data['allDataPath'].replace('\"', '')
                    downlaod_path = m_data['downloadDataPath'].replace('\"', '')
                    file_name_list.append(display_path)
                    file_name_list.append(all_path)
                    file_name_list.append(downlaod_path)
                else:
                    jupyter_dic = json.loads(latest_output[key])
                    display_path = jupyter_dic['targetDisplayDir'].replace('\"', '')
                    all_path = jupyter_dic['targetAllDir'].replace('\"', '')
                    downlaod_path = jupyter_dic['targetDownloadDir'].replace('\"', '')
                    file_name_list.append(display_path)
                    file_name_list.append(all_path)
                    file_name_list.append(downlaod_path)

        if data['property'] is not None and data['property'] != '' :
            property = json.loads(data['property'])
            if 'config' in property and 'hdfsPath' in property['config']:
                file_name_list.append(property['config']['hdfsPath'])
    return file_name_list

if __name__ == '__main__':
    # file_name(r'/home/fastdfs/fastdfs_storage/data')
    # del_file()
    fdfs_file_name =  read_file_name()
    local_file_name = node_file_name_list()
    del_file_name = [val for val in fdfs_file_name if val not in local_file_name]
    del_file(del_file_name)
