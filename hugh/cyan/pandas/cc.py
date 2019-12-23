#!/usr/bin/env python
# -- coding: utf-8 --#

import pandas as pd
import seaborn as sns
import numpy as np
import sqlalchemy
from sqlalchemy.orm import sessionmaker


# f = open("C://Users//Administrator//Desktop//test//tmp//xydfds.csv", "wb+")
# f.close()

# ss = b'group1/M00/85/C8/ChzI4lzRRCKAWj1ZAHt1Hf_e2Ls114.csv'
# print(ss)
# print(ss.decode("UTF-8"))

# url = "jdbc:mysql://10.28.109.14:3306/bbd_tetris"
# url = url.replace("jdbc:mysql://", "")
# print(url)
# url = "\"dd\""
# print(url.replace("\"", ''))

# filed = [{'fieldName': 'job_admin', 'valueType': 'int', 'key': 'job_admin'}]
# print(filed[0]['fieldName'])

# table = [{"fieldName":"Row_No_","valueType":"int"},{"fieldName":"Passenger_Class_First","valueType":"int"},{"fieldName":"Passenger_Class_Second","valueType":"int"},{"fieldName":"Passenger_Class_Third","valueType":"int"},{"fieldName":"Sex_Female","valueType":"int"},{"fieldName":"Sex_Male","valueType":"int"},{"fieldName":"Port_of_Embarkation_?","valueType":"int"},{"fieldName":"Port_of_Embarkation_Cherbourg","valueType":"int"},{"fieldName":"Port_of_Embarkation_Queenstown","valueType":"int"},{"fieldName":"Port_of_Embarkation_Southampton","valueType":"int"}]
# columns = []
# for i in range(len(table)):
#     columns.append(table[i]['fieldName'])
# print(columns)
#
# def getPandasDataType(type):
#     type = type.upper()
#     if type == "BIGINT":
#         return 'int','dealNum'
#     if type in ("INT", "TINYINT", "SMALLINT", "MEDIUMINT", "INTEGER", "BIGINT"):
#         return 'int','dealNum'
#     elif type == "FLOAT":
#         return 'float','dealNum'
#     elif type == "DOUBLE":
#         return 'float','dealNum'
#     elif type == "DECIMAL":
#         return 'float','dealNum'
#     elif type in ("TIMESTAMP", "DATETIME", "TIME"):
#         return 'date','dealDate'
#     elif type == "DATE":
#         return 'date','dealDate'
#     elif type == "LIST":
#         return 'str','notDeal'
#
#     return 'str','dealString'
#
# outDataTypes = []
# for i in range(len(table)):
#     dict = {}
#     dict['filedName'] = table[i]['fieldName']
#     type,deal = getPandasDataType(table[i]['valueType'])
#     dict['dataType'] = type
#     outDataTypes.append(dict)
# print(outDataTypes)
# ss = "inI"
# print(ss.lower())
#
# import pandas as pd
#
# df = pd.read_excel(r'C:\Users\Administrator\Desktop\test\tmp\news_credit_info.xls')
# # df = pd.read_csv(r'C:\Users\Administrator\Desktop\test\tmp\news_credit_info.xls')
# print(df)
# print(df['bbd_uptime'])
# df['bbd_uptime'] = df['bbd_uptime'] * 1000
# print(pd.to_datetime(df['bbd_uptime']))
# print(df['ctime'])

if __name__ == '__main__':
    engienCmd = 'mysql+pymysql://{username}:{password}@{url}'.format(username='quant',
                                                                     password='bbd123',
                                                                     url='10.28.109.14:3306/bbd_tetris')
    engine = sqlalchemy.create_engine(engienCmd, connect_args={'charset': 'utf8'})

    sql = '''select MAX(date_format(create_date, "%H:%i:%s")) latest_op_time, operator_name
      from gxyh_operate_log
      where operator_name
      group by operator_name
      order by latest_op_time desc'''

    sql = '''select id, operator_id, operator_name, target_type
          from gxyh_operate_log
          where operator_name'''
    # Session = sessionmaker(bind=engine)
    # sess = Session()
    #
    # allDf = sess.execute(sql).fetchall()
    # allDf = pd.DataFrame(allDf)
    # print(allDf)
    # reg = 'date_format'
    sql = sqlalchemy.text(sql)
    print(sql)
    allDf =pd.read_sql_query(sql, engine)
    print(allDf)
    x = allDf.loc[:, allDf.columns != 'operator_name']

    print(x)

