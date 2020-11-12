#!/usr/bin/env python
# -- coding: utf-8 --#

import pandas as pd
import sqlalchemy
import json

def mappingDfTypes(df):
    dtypedict = {}
    for i, j in zip(df.columns, df.dtypes):
        if "object" in str(j):
            maxLen = max(df[i].str.len())
            varType = sqlalchemy.NVARCHAR(length=32)
            if maxLen <= 32:
                varType = sqlalchemy.NVARCHAR(length=32)
            elif maxLen <= 64:
                varType = sqlalchemy.NVARCHAR(length=64)
            elif maxLen <= 255:
                varType = sqlalchemy.NVARCHAR(length=255)
            elif maxLen <= 3000:
                varType = sqlalchemy.NVARCHAR(length=3000)
            else:
                varType = sqlalchemy.TEXT()

            dtypedict.update({i: varType})
        if "float" in str(j):
            dtypedict.update({i: sqlalchemy.Float()})
        if "int" in str(j):
            varType = sqlalchemy.Integer()
            maxLen = max(df[i].apply(str).apply(len))
            if maxLen > 11:
                varType = sqlalchemy.BIGINT()
            dtypedict.update({i: varType})
    return dtypedict

if __name__ == '__main__':
    engienCmd = 'mysql+pymysql://{username}:{password}@{url}'.format(username='quant',
                                                                     password='bbd123',
                                                                     url='10.28.109.14:3306/sf_test')
    engine = sqlalchemy.create_engine(engienCmd, connect_args={'charset': 'utf8'})

    sqlstr = '''select * from alias_library'''
    df = pd.read_sql_query(sqlstr, engine)


    tableName = 'dfsfsfsdf_fdsfdsf'
    dtypedict = mappingDfTypes(df)
    df = df.set_index('bbd_unique_id')
    print(df)
    # df.to_sql(tableName, engine, if_exists="replace", dtype=dtypedict)
    dd = {}
    print(type(df.columns))
    dd['dd'] = list(df.columns)
    print(json.dumps(dd))


#     sqlStr = '''select * from ({sql}) a limit 1000  '''.format(sql='select * from test_data')
#     df = pd.read_sql_query(sqlStr, engine)
#     print(df)
#     print(df.dtypes)
#     print(isinstance(df['id'], (float,)))
#     df.to_csv(r'C:\Users\Administrator\Desktop\test\tmp\aaggc.csv')
#
#     sqlStr = '''select * from ({sql}) b limit 1000'''.format(sql='''select a.* from test_data a inner join test_data b
# on a.date_data = b.date_data
# and a.date_data_1 = b.date_data_1
# and a.float_data = b.float_data
# and a.id = b.id
# and a.int_data = b.int_data
# and a.string_data = b.string_data
# and a.`timestamp` = b.`timestamp`''')
#     df = pd.read_sql_query(sqlStr, engine)
#     print(df)

    # sqlTest = 'select * from test_data'
    # leftDf = pd.read_sql_query(sqlTest, engine)
    # leftDf.to_csv(r'C:\Users\Administrator\Desktop\test\tmp\leftDf.csv', index=False)
    # leftDf = pd.read_csv(r'C:\Users\Administrator\Desktop\test\tmp\leftDf.csv')
    # print(leftDf)
    # rightDf = pd.read_sql_query(sqlTest, engine)
    # rightDf.to_csv(r'C:\Users\Administrator\Desktop\test\tmp\rightDf.csv', index=False)
    # rightDf = pd.read_csv(r'C:\Users\Administrator\Desktop\test\tmp\rightDf.csv')
    # print(rightDf)
    # print(leftDf.iloc[4].values)
    # print(rightDf.iloc[4].values)
    # print(rightDf['string_data'][4] == rightDf['string_data'][4])
    # print(leftDf['string_data'][4] == leftDf['string_data'][4])
    # rIndex = ['id', 'int_data', 'float_data', 'string_data', 'date_data', 'date_data_1', 'timestamp']
    # lIndex = ['id', 'int_data', 'float_data', 'string_data', 'date_data', 'date_data_1', 'timestamp']
    #
    # allDf = leftDf.join(rightDf.set_index(rIndex), on=lIndex, how='inner', lsuffix='_l', rsuffix='_r')
    # print(allDf)

    # def removeRN(var):
    #     if var != None:
    #         var = var.replace("\r", "")
    #         var = var.replace("\n", "")
    #     return var
    #
    # sqlTest = 'select * from qyxg_rongzi'
    # upDf = pd.read_sql_query(sqlTest, engine)
    # for column in upDf.columns:
    #     if upDf[column].dtype == 'object':
    #         print(column)
    #         upDf[column].apply(removeRN)
    #
    # upDf.to_csv(r'C:\Users\Administrator\Desktop\test\tmp\upDf.csv',sep='\u0001', header=True, index=False)
    # upDf = pd.read_csv(r'C:\Users\Administrator\Desktop\test\tmp\upDf.csv',sep='\u0001')
    # print(upDf)

    # testDf = pd.read_csv(r'C:\Users\Administrator\Desktop\test\tmp\test_data.csv')
    # print(testDf)
    # if testDf['id'].isnull().any():
    #     print("--------")
    #     testDf['id'] = testDf['id'].astype('float')
    # else:
    #     testDf['id'] = testDf['id'].astype('int')
    # testDf['id'] = testDf['id'].astype('float')
    # print(testDf)