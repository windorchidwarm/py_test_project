#!/usr/bin/env python
# -- coding: utf-8 --#
# @Time : 2019/8/12 17:17 
# @Author : Aries 
# @Site :  
# @File : static_data.py 
# @Software: PyCharm
# 用于静态数据集文件下载和上传转换

import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import pandas as pd
import json
from fdfs_client.client import *


# 下载并重新上传文件
def downlaod_upload_path(path):
    FDFSDATA = {'host_tuple': ['10.200.101.205', '10.200.101.209'], 'port': 22122, 'timeout': 60,
                'name': 'Tracker Pool'}
    client = Fdfs_client(FDFSDATA)
    buff = client.download_to_buffer(path.encode())
    local_path = r'C:\Users\BBD\Desktop\test\tmp'
    local_path = os.path.join(local_path, path.split('/')[4])
    print(local_path)
    if os.path.isfile(local_path):
        os.remove(local_path)
    f = open(local_path, 'xb')
    f.write(buff['Content'])
    f.flush()
    time.sleep(2)

    upload_data = client.upload_by_filename(local_path)
    return upload_data['Remote file_id'].decode()


# 获取数据库连接的session
def get_session():
    engienCmd = 'mysql+pymysql://{username}:{password}@{url}'.format(username='tetris',
                                                                     password='tetris123',
                                                                     url='10.200.101.196:3306/bbd_tetris_edu')
    engine = sqlalchemy.create_engine(engienCmd, connect_args={'charset': 'utf8'})
    session_factory = sessionmaker(bind=engine)
    session = session_factory()
    return session


# list转字典 根据列名
def to_dict(data, columns):
    return dict(zip(columns, data))


Base = declarative_base()


# sqlalchemy的表映射
class tetris_process_resource(Base):
    '''
    创建表和字段的映射
    '''
    __tablename__ = 'tetris_process_resource'
    id = sqlalchemy.Column(sqlalchemy.INTEGER, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String(100))
    type = sqlalchemy.Column(sqlalchemy.String(4))
    properties = sqlalchemy.Column(sqlalchemy.TEXT)
    latest_output = sqlalchemy.Column(sqlalchemy.TEXT)
    comments = sqlalchemy.Column(sqlalchemy.String(2000))


if __name__ == '__main__':
    print("start ... ")
    fileList = {16852:'13', 16853:'14', 16854:'15', 16855:'16'}


    sql = '''select * from gxyh_node where id = {node_id} '''

    my_column = ["id", "name", "type", "location_x", "location_y", "is_end", "end_index","property", "latest_output",
                 "create_by", "create_date", "update_by", "update_date", "is_local"]

    for node_id in fileList.keys():
        print(node_id)
        sql_now = sql.format(node_id = node_id)
        print(sql_now)
        session = get_session()

        result_proxy = session.execute(sqlalchemy.text(sql_now))
        result_all = result_proxy.fetchall()
        data = to_dict(result_all[0], my_column)
        latest_output = json.loads(data['latest_output'])
        print(latest_output)
        display_path = latest_output['0']['displayDataPath']
        all_path = latest_output['0']['allDataPath']
        downlaod_path = latest_output['0']['downloadDataPath']

        display_path = downlaod_upload_path(display_path.replace('\"', ''))
        all_path = downlaod_upload_path(all_path.replace('\"', ''))
        downlaod_path = downlaod_upload_path(downlaod_path.replace('\"', ''))

        latest_output['0']['displayDataPath'] = '"' +  display_path + '"'
        latest_output['0']['allDataPath'] = '"' +  all_path + '"'
        latest_output['0']['downloadDataPath'] = '"' +  downlaod_path + '"'

        # 更新静态数据集的数据库数据
        print(json.dumps(latest_output))
        result_proxy = session.query(tetris_process_resource) \
            .filter(tetris_process_resource.type == fileList.get(node_id)).one()
        result_proxy.latest_output = json.dumps(latest_output)
        session.commit()

