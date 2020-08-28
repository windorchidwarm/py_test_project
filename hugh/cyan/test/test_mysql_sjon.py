#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : test_mysql_sjon.py
# Author: hugh
# Date  : 2020/8/28

import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy
import json

from sqlalchemy.ext.declarative import DeclarativeMeta
from datetime import datetime

Base = declarative_base()

class TMrecProcess(Base):
    '''
    创建表和字段的映射
    '''
    __tablename__ = 't_mrec_process'
    id = sqlalchemy.Column(sqlalchemy.INTEGER, primary_key=True)
    project_id = sqlalchemy.Column(sqlalchemy.INTEGER)
    process_name = sqlalchemy.Column(sqlalchemy.String(255))
    remarks = sqlalchemy.Column(sqlalchemy.String(255))
    status = sqlalchemy.Column(sqlalchemy.INTEGER)
    create_by = sqlalchemy.Column(sqlalchemy.INTEGER)
    create_date = sqlalchemy.Column(sqlalchemy.TIMESTAMP)
    update_by = sqlalchemy.Column(sqlalchemy.INTEGER)
    update_date = sqlalchemy.Column(sqlalchemy.TIMESTAMP)

def get_mysql_session_default():
    engienCmd = 'mysql+pymysql://{username}:{password}@{url}/{db}'\
        .format(username='bbd', password='123456', url='10.28.109.102', db='db_sse_visualmod')
    engine = sqlalchemy.create_engine(engienCmd, connect_args={'charset': 'utf8'})
    session_factory = sessionmaker(bind=engine)
    session = session_factory()
    return session


def new_alchemy_encoder():
    _visited_objs = []

    class AlchemyEncoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj.__class__, DeclarativeMeta):
                # don't re-visit self
                if obj in _visited_objs:
                    return None
                _visited_objs.append(obj)

                # an SQLAlchemy class
                fields = {}
                for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
                    data = obj.__getattribute__(field)
                    try:
                        if isinstance(data, datetime):
                            data = data.strftime('%Y-%m-%d %H:%M:%S')
                        json.dumps(data)  # this will fail on non-encodable values, like other classes
                        fields[field] = data
                    except TypeError:
                        fields[field] = None
                return fields

            return json.JSONEncoder.default(self, obj)
    return AlchemyEncoder

if __name__ == '__main__':
    session = get_mysql_session_default()
    deployData = session.query(TMrecProcess).all()
    msgs = {}
    for msg in deployData:
        msgs[msg.id] = msg
    publishConfig = json.dumps(msgs, cls=new_alchemy_encoder(), check_circular=False)
    print(publishConfig)