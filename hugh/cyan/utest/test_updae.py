#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : test_updae.py
# Author: hugh
# Date  : 2020/6/22

import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class tetris_node_partition(Base):
    '''
    创建表和字段的映射
    '''
    __tablename__ = 'gxyh_node_partition'
    id = sqlalchemy.Column(sqlalchemy.INTEGER)
    partition_id = sqlalchemy.Column(sqlalchemy.INTEGER)
    partition_type = sqlalchemy.Column(sqlalchemy.INTEGER)
    name = sqlalchemy.Column(sqlalchemy.String(255))
    type = sqlalchemy.Column(sqlalchemy.INTEGER)
    location_x = sqlalchemy.Column(sqlalchemy.FLOAT)
    location_y = sqlalchemy.Column(sqlalchemy.FLOAT)
    is_end = sqlalchemy.Column(sqlalchemy.INTEGER)
    end_index = sqlalchemy.Column(sqlalchemy.String(256))
    property = sqlalchemy.Column(sqlalchemy.TEXT)
    latest_output = sqlalchemy.Column(sqlalchemy.TEXT)
    create_by = sqlalchemy.Column(sqlalchemy.String(64))
    create_date = sqlalchemy.Column(sqlalchemy.TIMESTAMP)
    update_by = sqlalchemy.Column(sqlalchemy.String(64))
    update_date = sqlalchemy.Column(sqlalchemy.TIMESTAMP)
    is_local = sqlalchemy.Column(sqlalchemy.String(4))

    __mapper_args__ = {
        'primary_key': [id, partition_id, partition_type]
    }


def get_engine():
    engienCmd = 'mysql+pymysql://{username}:{password}@{url}'.format(username='canghai',
                                                                     password='PfBC7RdJ',
                                                                     url='10.28.109.230:3307')
    engine = sqlalchemy.create_engine(engienCmd, connect_args={'charset': 'utf8'})
    return engine


def get_session():
    engienCmd = 'mysql+pymysql://{username}:{password}@{url}'.format(username='canghai',
                                                                     password='PfBC7RdJ',
                                                                     url='10.28.109.230:3307/canghai_ai')
    engine = sqlalchemy.create_engine(engienCmd, connect_args={'charset': 'utf8'})
    session_factory = sessionmaker(bind=engine)
    session = session_factory()
    return session


if __name__ == '__main__':
    '''
    '''
    session = get_session()
    result_proxy = session.query(tetris_node_partition) \
        .filter(tetris_node_partition.id == 64,
                tetris_node_partition.partition_id == 24,
                tetris_node_partition.partition_type == 1) \
        .one()
    print(result_proxy)
    print(result_proxy.partition_id)
    result_proxy.name = '测试1'
    session.commit()
