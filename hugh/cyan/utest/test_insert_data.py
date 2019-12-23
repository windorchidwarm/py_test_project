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

    # 这里获取部门的id
    sql_tenant_id = '''select tenant_id from {table_name}'''.format(table_name='xxxx')
    my_column = ['tenant_id']
    session = get_session()

    result_proxy = session.execute(sqlalchemy.text(sql_tenant_id))
    result_all = result_proxy.fetchall()

    # 数据的初始化地址，自己记得修改 还有记得去修改映射的表名和字段名
    id = 0
    acount = 0
    # 循环部门的id
    for i in range(len(result_all)):
        tenant_id = result_all[i][0]
        # 循环部门的条数
        for num in range(data_nums):
            id = id + 1
            acount = acount + 1
            member_table_data = member_table(id=id, tenant_id=tenant_id, acount='test' + str(acount))
            session.add(member_table_data)
            session.commit()


