#!/usr/bin/env python
# -- coding: utf-8 --#
# @Time : 2019/10/25 13:43 
# @Author : Aries 
# @Site :  
# @File : yunnan2.py 
# @Software: PyCharm

import pandas as pd
import pymysql
import math


if __name__ == '__main__':
    engienCmd = 'mysql+pymysql://{username}:{password}@{url}'.format(username='bbd',
                                                                     password='123456',
                                                                     url='10.28.109.102:3306/db_policy_government_service')
    df = pd.read_excel(r'C:\Users\BBD\Desktop\test\data\附件1-专项资金申报数据字段.xlsx')
    print(df)
    # db = pymysql.connect('10.28.109.102', 'bbd', '123456', 'db_policy_government_service')
    db = pymysql.connect('10.28.200.238', 'root', '123456', 'db_policy_government_service')
    cursor = db.cursor()

    query = '''insert ignore into policy_company_declare
    (`id`,`program_name`,`program_company_name`,`company_name`,`declare_score`,`investment_money`,`registration_addr`
    ,`registration_addr_city`,`registration_addr_county`,`registration_addr_area`)
    values (%s, %s, %s,%s,%s,%s,%s,%s,%s,%s)
    '''

    for index, row in df.iterrows():
        try:

            id = row['企业申报']
            program_name = row[1]
            program_company_name = row[2]
            company_name = row[3]
            declare_score = 0.0
            # declare_score = row[4]
            print(row[4])
            investment_money = row[4] if not math.isnan(row[4]) else 0.0
            print(investment_money)
            registration_addr = row[5]
            reg = str(registration_addr).split('/')
            lenReg = len(reg)
            if id == '序号':
                continue
            print(lenReg)
            registration_addr_city = reg[0] if lenReg >= 1 else None
            registration_addr_county = reg[1] if lenReg >= 2 else None
            registration_addr_area = reg[2] if lenReg >= 3 else None


            values = (id, program_name, program_company_name, company_name, declare_score, investment_money, registration_addr
                      ,registration_addr_city,registration_addr_county,registration_addr_area)
            cursor.execute(query, values)
            print(values)
        except:
            print("error at ", index)
            continue
    cursor.close()
    db.commit()
    db.close()