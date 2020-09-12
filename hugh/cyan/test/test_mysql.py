#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : test_mysql.py
# Author: hugh
# Date  : 2020/9/11

import sqlalchemy
from sqlalchemy.orm import sessionmaker
BASE_USERNAME = 'bbd'
BASE_PASSWORD = '123456'
BASE_URL = '10.28.109.102:3306'
BASE_DB = 'db_sse_visualmod'

from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy

from datetime import datetime

Base = declarative_base()

# sqlalchemy的表映射
class TMrecNode(Base):
    '''
    创建表和字段的映射
    '''
    __tablename__ = 't_mrec_node'
    id = sqlalchemy.Column(sqlalchemy.INTEGER, primary_key=True)
    process_id = sqlalchemy.Column(sqlalchemy.INTEGER)
    name = sqlalchemy.Column(sqlalchemy.String(255))
    type = sqlalchemy.Column(sqlalchemy.INTEGER)
    location_x = sqlalchemy.Column(sqlalchemy.FLOAT)
    location_y = sqlalchemy.Column(sqlalchemy.FLOAT)
    is_end = sqlalchemy.Column(sqlalchemy.INTEGER)
    end_index = sqlalchemy.Column(sqlalchemy.String(255))
    property = sqlalchemy.Column(sqlalchemy.TEXT)
    latest_output = sqlalchemy.Column(sqlalchemy.TEXT)
    status = sqlalchemy.Column(sqlalchemy.INTEGER)
    create_by = sqlalchemy.Column(sqlalchemy.INTEGER)
    create_date = sqlalchemy.Column(sqlalchemy.TIMESTAMP)
    update_by = sqlalchemy.Column(sqlalchemy.INTEGER)
    update_date = sqlalchemy.Column(sqlalchemy.TIMESTAMP)


# sqlalchemy的表映射
class TMrecProcessExecuteHistory(Base):
    '''
    创建表和字段的映射
    '''
    __tablename__ = 't_mrec_process_execute_history'
    id = sqlalchemy.Column(sqlalchemy.INTEGER, primary_key=True)
    process_id = sqlalchemy.Column(sqlalchemy.INTEGER)
    process_type = sqlalchemy.Column(sqlalchemy.INTEGER)
    execute_version = sqlalchemy.Column(sqlalchemy.String(16))
    status = sqlalchemy.Column(sqlalchemy.INTEGER)
    dag = sqlalchemy.Column(sqlalchemy.TEXT)
    create_by = sqlalchemy.Column(sqlalchemy.INTEGER)
    create_date = sqlalchemy.Column(sqlalchemy.TIMESTAMP)
    update_by = sqlalchemy.Column(sqlalchemy.INTEGER)
    update_date = sqlalchemy.Column(sqlalchemy.TIMESTAMP)

# 获取mysql的session
def get_mysql_session_default():
    engine_cmd = 'mysql+pymysql://{username}:{password}@{url}/{db}' \
        .format(username=BASE_USERNAME, password=BASE_PASSWORD, url=BASE_URL, db=BASE_DB)
    engine = sqlalchemy.create_engine(engine_cmd, connect_args={'charset': 'utf8'})
    session_factory = sessionmaker(bind=engine)
    session = session_factory()
    current_node = session.query(TMrecNode) \
        .filter(TMrecNode.id == 9).one()
    print(current_node.create_by)
    n_date = datetime.now()
    his = TMrecProcessExecuteHistory(process_id=1, process_type=4, execute_version='12221',
                                     status=0, dag='22', create_by=1, update_by=1, create_date=n_date,
                                     update_date=n_date)
    session.add(his)
    session.flush()
    session.commit()
    print(his.id)
    his = TMrecProcessExecuteHistory(process_id=1, process_type=4, execute_version='12221',
                                     status=0, dag=his, create_by=1, update_by=1, create_date=n_date,
                                     update_date=n_date)
    session.add(his)
    session.flush()
    session.commit()
    return session

if __name__ == '__main__':
    '''
    '''
    get_mysql_session_default()