#!/usr/bin/env python
# -- coding: utf-8 --#

import statsmodels.api as sm
from statsmodels.regression.linear_model import OLS
import statsmodels.formula.api as smf
import numpy as np
import pandas as pd
import sqlalchemy
import json

if __name__ == '__main__':
    # engienCmd = 'mysql+pymysql://{username}:{password}@{url}'.format(username='quant',
    #                                                                 password='bbd123',
    #                                                                 url='10.28.109.14:3306/sf_test')
    # engine = sqlalchemy.create_engine(engienCmd, connect_args={'charset': 'utf8'})
    # sql = '''select * from '''

    df = pd.read_csv(r'C:\Users\Administrator\Desktop\test\tmp\线性回归训练集.csv')
    y = df['label']
    X = df[['a', 'b']]
    X = sm.add_constant(X)
    model = sm.OLS(y,X)
    est = model.fit()
    # est.write().overwrite().save(r'C:\Users\Administrator\Desktop\test\tmp\tt.csv')
    result_summary = est.summary()
    print("######################")
    print(result_summary)
    print("######################")
    print(est.params)
    print(est.fittedvalues)

    lDf = pd.DataFrame(est.fittedvalues)
    lDf.columns = ['label']
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    print(lDf)

    def getDataFrameTable(res, i):
        resHtml = res.tables[i].as_html()
        temp = pd.read_html(resHtml)[0]
        return temp.to_json(orient='index')

    # result0_html = result_summary.tables[0].as_html()
    # table0 = pd.read_html(result0_html)
    # table0['index'][:16] = table0['index'][:16].map(lambda x: x.strip(':'))
    # dict_table1 = table0.set_index(['index']).T.to_dict('list')
    # table0 = pd.DataFrame(dict_table1, columns=dict_table1.keys())
    table0 = getDataFrameTable(result_summary, 0)
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    print(table0)
    # result1_html = result_summary.tables[1].as_html()
    # table1 = pd.read_html(result1_html)
    table1 = getDataFrameTable(result_summary, 1)
    print("######################")
    print(table1)
    # result2_html = result_summary.tables[2].as_html()
    # table2 = pd.read_html(result2_html)
    table2 = getDataFrameTable(result_summary, 2)
    print("######################")
    print(table2)
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    est.save(r'C:\Users\Administrator\Desktop\test\tmp\tt.pickle')
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    # print(sm.stats.linear_rainbow(result_summary))

    print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&')
    # estNow = sm.load(r'C:\Users\Administrator\Desktop\test\tmp\tt.pickle')
    # smf.ols()
    preDf = pd.read_csv(r'C:\Users\Administrator\Desktop\test\tmp\线性回归测试集.csv')
    XX = preDf[['a', 'b']]
    nwt = sm.load(r'C:\Users\Administrator\Desktop\test\tmp\tt.pickle')
    print(dir(nwt))
    # nowTreain = OLS.predict(nwt, XX)
    XX = preDf.drop('no', axis=1).values
    print(XX)
    nowTreain = nwt.predict(XX)
    print(nowTreain)
    print(json.dumps({"0":table0,"1":table1,"2":table2}))
    label = 'label'
    def toOutput(predict):
        df = pd.DataFrame(predict)
        df.columns = [label]
        return df

    rDf = toOutput(nowTreain)
    preDf = preDf.drop(label, axis=1)
    print(pd.concat([preDf,rDf],axis=1))

    print(toOutput(nowTreain))
