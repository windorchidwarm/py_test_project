#!/usr/bin/env python
# -- coding: utf-8 --#
# @Time : 2019/8/29 16:15 
# @Author : Aries 
# @Site :  
# @File : test_insert_data.py 
# @Software: PyCharm


import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import pandas as pd
import json


# 获取数据库连接的session
def get_session():
    engienCmd = 'mysql+pymysql://{username}:{password}@{url}'.format(username='canghai',
                                                                     password='PfBC7RdJ',
                                                                     url='10.28.109.230:3307')
    engine = sqlalchemy.create_engine(engienCmd, connect_args={'charset': 'utf8'})
    session_factory = sessionmaker(bind=engine)
    session = session_factory()
    return session


def get_engine():
    engienCmd = 'mysql+pymysql://{username}:{password}@{url}'.format(username='canghai',
                                                                     password='PfBC7RdJ',
                                                                     url='10.28.109.230:3307')
    engine = sqlalchemy.create_engine(engienCmd, connect_args={'charset': 'utf8'})
    return engine

# list转字典 根据列名
def to_dict(data, columns):
    return dict(zip(columns, data))


Base = declarative_base()


# sqlalchemy的表映射
class member_table(Base):
    '''
    创建表和字段的映射
    '''
    __tablename__ = 'NewTable'
    id = sqlalchemy.Column(sqlalchemy.INTEGER, primary_key=True)
    tenant_id = sqlalchemy.Column(sqlalchemy.INTEGER)
    account = sqlalchemy.Column(sqlalchemy.String(255))
    password = sqlalchemy.Column(sqlalchemy.String(200))
    avatar = sqlalchemy.Column(sqlalchemy.String(255))
    realname = sqlalchemy.Column(sqlalchemy.String(100))
    email = sqlalchemy.Column(sqlalchemy.String(255))
    phone = sqlalchemy.Column(sqlalchemy.String(255))
    space = sqlalchemy.Column(sqlalchemy.INTEGER)
    created_at = sqlalchemy.Column(sqlalchemy.DATE)
    updated_at = sqlalchemy.Column(sqlalchemy.DATE)
    deleted_at = sqlalchemy.Column(sqlalchemy.DATE)
    used_space = sqlalchemy.Column(sqlalchemy.INTEGER)
    info = sqlalchemy.Column(sqlalchemy.Text)
    ic_card = sqlalchemy.Column(sqlalchemy.String(100))
    disabled = sqlalchemy.Column(sqlalchemy.INTEGER)


if __name__ == '__main__':
    # 这里定义你要插入的数据条数
    data_nums = 200

    df = pd.read_csv(r'C:\Users\BBD\Desktop\test\tmp\2.csv')
    engine = get_engine()
    sql = 'select * from `canghai_ai`.`gxyh_edge` a limit 10'
    dd = pd.read_sql_query(sql, engine)
    print(dd)

    df.to_sql(name='test', schema='canghai_ai', con=engine, if_exists="replace")



