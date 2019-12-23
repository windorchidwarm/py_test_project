#!/usr/bin/env python
# -- coding: utf-8 --#

import pandas as pd
import sqlalchemy
import datetime
import re

#jdbc:mysql://10.28.109.14:3306/bbd_tetris?useUnicode=true&characterEncoding=utf-8&useSSL=false&allowMultiQueries=true

# engienCmd = 'mysql+pymysql://{username}:{password}@{url}'.format(username='quant',
#         password='bbd123', url='10.28.109.14:3306/bbd_tetris')
# engine = sqlalchemy.create_engine(engienCmd, connect_args={'charset':'utf8'})
#
# # sample_0
# sql = '''
# {sql}
# '''.format(sql='select * from gxyh_node')

# df = pd.read_sql_query(sql, engine)
# print(df)
# print("***********************^^")
# # print(df.count())
#
# print(df.info())
# print("***********************^^")
# print(df.get_dtype_counts())
# print(df.mean())
# print(df.max())
# print(df.min())
# print(df.keys())


# for key in df.keys():
#     print(key, end='')
#     print("--->", end='')
#     print(df[key].dtype)
#     print(str(df[key].dtype).lower() in ['int32', 'int64'])
#     print(str(df[key].dtype).lower() in ['float32', 'float64'])
#     print(str(df[key].dtype).lower() in ['object'])
#     print(str(df[key].dtype).lower() in ['datetime64', 'datetime32', 'datetime64[ns]', 'datetime32[ns]'])

def getDealFun(df):
    dict = {}
    for fieldName in df.keys():
        if str(df[fieldName].dtype).lower() in ['object']:
            dataTypeCount['str'] = dataTypeCount['str'] + 1
            dict[fieldName] = dealStr
        elif str(df[fieldName].dtype).lower() in ['int32', 'int64']:
            dataTypeCount['int'] = dataTypeCount['int'] + 1
            dict[fieldName] = dealNum
        elif str(df[fieldName].dtype).lower() in ['float32', 'float64']:
            dataTypeCount['float'] = dataTypeCount['float'] + 1
            dict[fieldName] = dealNum
        elif str(df[fieldName].dtype).lower() in ['datetime64', 'datetime32', 'datetime64[ns]', 'datetime32[ns]']:
            dataTypeCount['date'] = dataTypeCount['date'] + 1
            dict[fieldName] = dealDate
        else:
            dict[fieldName] = notDeal
    return dict

def dealStr(fieldName, showLen = 20):
    '''
    处理字符串类型
    :param fieldName:
    :param showLen:
    :return:
    '''
    retDict = {}

    count = len(df)
    # sp = df[fieldName][df[fieldName] != '']
    # sp = sp[sp != '']
    strCount = df[fieldName][df[fieldName] != ''].value_counts(ascending=True, dropna=True)

    retDict['max'] = strCount.max()
    retDict['min'] = strCount.min()
    #唯一值
    retDict['uniqueCount'] = len(df[fieldName].unique())
    #缺失值
    retDict['defectCount'] = count - sum(strCount)
    # 分布图
    distData = []
    strCountSort = sorted(strCount.items(), key=lambda item: item[1], reverse=True)
    top10Count = 0
    for i in range(min(9, len(strCountSort))):
        top10Count = top10Count + strCountSort[i][1]
        key = strCountSort[i][0]
        distData.append({key[0:showLen]+u"......" if key and len(key) > showLen else key: strCountSort[i][1]})
    if len(strCountSort) > 10:
        distData.append({'other': (count - top10Count)})
    retDict['distData'] = distData
    retDict['fieldName'] = fieldName
    retDict['dataType'] = "string"
    # print("##########################")
    # print(fieldName)
    # pc = df[fieldName].count()
    # count = len(df)
    # print(count)
    # print(len(df[fieldName]))
    # print(pc)
    # # print(df[fieldName].value_counts())
    # # strCount = df.groupby(fieldName).size();
    # strCount = df[fieldName].value_counts()
    # print(strCount)
    # print("@@@@@@@@@@@@@@@@@@@@@@@@@@")
    # print(strCount.max())
    # print(strCount.min())
    # print(len(df[fieldName].unique()))
    # print(count - sum(strCount))
    # # 分布图
    # distData = []
    # # strCountDict = {}
    # # for key, value in strCount.items():
    # #     strCountDict[key] = value
    # # print(sorted(strCountDict.items(), key =lambda item:item[1]))
    #
    # # print(strCount.index[0])
    # # print(sorted(strCount.items(), key=lambda item: item[1], reverse=True))
    # strCountSort = sorted(strCount.items(), key=lambda item: item[1], reverse=True)
    # top10Count = 0
    # print(strCountSort)
    # k = 0
    # for i in range(min(9, len(strCountSort))):
    #     while strCountSort[i + k][0] == '':
    #         k = k + 1
    #     top10Count = top10Count + strCountSort[i + k][1]
    #     key = strCountSort[i + k][0]
    #     distData.append({key[0:showLen]+u"......" if key and len(key) > showLen else key: strCountSort[i + k][1]})
    # if len(strCountSort) > 10 or k > 0:
    #     distData.append({'other': (count - top10Count)})

    # if len(strCount) > 10:
    #     strCount = sorted(strCount)
    #     other = 0
    #     for i in range(9):
    #        other += strCount[i]
    # print(distData)
    # print("##########################")


    return retDict

def dealNum(fieldName):
    '''
    数值类型的处理
    :param fieldName:
    :return:
    '''
    retDict = {}
    pp = df[fieldName]
    maxv = pp.max()
    minv = pp.min()
    retDict['max'] = maxv
    retDict['min'] = minv
    retDict['mean'] = pp.mean()
    #标准差
    retDict['stddev'] = pp.std()
    #缺失值
    totalCount = pp.count()
    retDict['defectCount'] = len(pp) - totalCount
    # 数据分布
    numDistArr = []
    if maxv != minv:
        interv = float(maxv - minv) / 10.0
        levels = []
        for i in range(0, 10):
            v = float(minv) + interv * (i + 1)
            levels.append(float('%.4f' % v))
        preCount = len(pp[pp >= minv])
        afCount = len(pp[pp >= levels[0]])
        numDistArr.append({"{0}-{1}".format(minv, levels[0]): preCount - afCount})
        preCount = afCount
        for i in range(1, len(levels) - 1):
            afCount = len(pp[pp >= levels[i]])
            numDistArr.append({"{0}-{1}".format(levels[i - 1], levels[i]): preCount - afCount})
            preCount = afCount
        numDistArr.append({"{0}-{1}".format(levels[8], str(maxv)): preCount})
    elif totalCount > 0:
        numDistArr.append({str(maxv): totalCount})
    retDict['distData'] = numDistArr
    retDict['fieldName'] = fieldName
    retDict['dataType'] = "number"
    # print(retDict)
    # print("##########################")
    return retDict

def dealDate(fieldName):
    '''
    时间类型处理
    :param fieldName:
    :return:
    '''
    retDict = {}
    datep = df[fieldName]
    # datep.registerTempTable("date_t")
    # 总数
    dateTotalCount =datep.count()
    maxv = datep.max()
    minv = datep.min()
    retDict['max'] = str(maxv)
    retDict['min'] = str(minv)
    # 久期
    dateSpan = (maxv - minv) if maxv and minv else datetime.timedelta(0)
    retDict['dateSpan'] = str(dateSpan)
    #缺失值
    retDict['defectCount'] = len(datep) - dateTotalCount
    # 数据分布
    dateDistArr = []
    if dateSpan.days > 0:
        interv = float(dateSpan.days) / 10.0
        levels = []
        dateDistArr = []
        for i in range(0, 10):
            v = (minv if minv else datetime.datetime(1970, 1, 1)) + datetime.timedelta(days=interv * (i + 1))
            levels.append(v)
        preCount = len(datep[datep >= minv])
        afCount = len(datep[datep >= levels[0]])
        dateDistArr.append({"{0}-{1}".format(minv, levels[0]): (preCount - afCount)})
        preCount = afCount
        for i in range(1, len(levels) - 1):
            afCount = len(datep[datep >= levels[i]])
            dateDistArr.append({"{0}-{1}".format(levels[i - 1], levels[i]): preCount - afCount})
            preCount = afCount
            dateDistArr.append({"{0}-{1}".format(levels[8], maxv): preCount})
    elif dateTotalCount > 0:
        dateDistArr.append({str(maxv): dateTotalCount})
    retDict['distData'] = dateDistArr
    retDict['fieldName'] = fieldName
    retDict['dataType'] = "date"
    return retDict

def notDeal(fieldName):
    '''
    不处理的计算类型
    :param fieldName:
    :return:
    '''
    retDict = {}
    return retDict

def replaceRN(var):
    if var is not None:
        var = str(var).replace('\r', '@r').replace('\n', '@n')
        return var
    return var

if __name__ == '__main__':
    engienCmd = 'mysql+pymysql://{username}:{password}@{url}'.format(username='quant',
                                                                password='bbd123',
                                                                url='10.28.109.14:3306/sf_test')
    engine = sqlalchemy.create_engine(engienCmd, connect_args={'charset': 'utf8'})

    tt = 'select * from test'
    de = 1000

    sql = 'select * from ({sql}) b limit {limitNum}'.format(sql=tt, limitNum=de)
    print(sql)

    alldf = pd.read_sql_query(sql, engine)
    print(alldf.dtypes)
    print("###########################")
    for column in alldf.columns:
        print(column, '---->', alldf[column].dtype)

    print('r.kk'.split("."))

    exp = re.compile('[\n|\r]')
    for column in alldf.columns:
        print(column, '---->', alldf[column].dtype)
        if alldf[column].dtype == 'object':
            alldf[column] = alldf[column].apply(lambda x: exp.sub('\u0002', str(x)) if x != None else x)

    # exp = re.compile('[\n|\r]')
    # for column in df.columns:
    #     if df[column].dtype == 'object':
    #         df[column] = df[column].apply(lambda x: exp.sub('\u0002', str(x)) if x != None else x)
    # print(df)
    alldf.to_csv(r'C:\Users\Administrator\Desktop\test\tmp\aa.csv', header=True, index=False)

    # print(df)
    # for fieldName in df.keys():
    #     if str(df[fieldName].dtype).lower() in ['int32', 'int64']:
    #         print(df[fieldName].dtype, '--->int')
    #     elif str(df[fieldName].dtype).lower() in ['float32', 'float64']:
    #         print(df[fieldName].dtype, '--->float')
    #     elif str(df[fieldName].dtype).lower() in ['date', 'datetime', 'datetime64', 'datetime32', 'datetime64[ns]',
    #                                               'datetime32[ns]']:
    #         print(df[fieldName].dtype, '--->date')
    #     elif str(df[fieldName].dtype).lower() in ['object']:
    #         print(df[fieldName].dtype, '--->str')
    #     else:
    #         print("----")


    # sql = 'select * from titanic_1_1'
    # sql2 = 'select * from titanic_2_3'
    # leftDf = pd.read_sql_query(sql, engine)
    # rightDf = pd.read_sql_query(sql2, engine)
    # allDf = leftDf.join(rightDf.set_index(['Row No.1']), on=['Row No.'], how='right', lsuffix='_l', rsuffix='_r')
    # allDf.to_csv(r'C:\Users\Administrator\Desktop\test\tmp\mm.csv', header=True, index=False)


    # gdf = pd.merge(leftDf, rightDf, how='left', on=None, left_on=['Row No.'], right_on=['Row No.'],

    # sql = '''
    #         {sql}
    #     '''.format(sql='select * from gxyh_execute_status')
    #
    # df = pd.read_sql_query(sql, engine)

    # strCount = df['statistic_data'][df['statistic_data'] != ''].value_counts(ascending=True, dropna=True)
    # print("######################")
    # print(strCount)
    # print("######################")
    # strCountSort = sorted(strCount.items(), key=lambda item: item[1], reverse=True)
    # print(strCountSort[0][0])
    # df['statistic_data'] = df['statistic_data'].fillna(strCountSort[1][0])
    # print(df)
    #
    # res = df.corr()
    #
    # df['xx'] = None
    # print(df)
    # print(res)
    # print(len(res))
    # # print(len(res[0]))
    # res = res.values
    # resSize = len(res)
    # for i in range(resSize):
    #     for j in range(resSize):
    #         res[i][j] = round(float(res[i][j]), 5)
    # print(res.tolist())





    # sample_0
    # sql = '''
    #     {sql}
    # '''.format(sql='select * from gxyh_process')
    # df = pd.read_sql_query(sql, engine)
    # dataTypeCount = {"int": 0, "float": 0, "str": 0, "date": 0}
    # dict = getDealFun(df)
    # totalCount = df.count()
    # retDict = {}
    # for fieldName, dealFun in dict.items():
    #     retDict[fieldName] = dealFun(fieldName)
    #
    # retDict['totalCount'] = totalCount
    # retDict.update(dataTypeCount)
    # print(retDict)



# print(df.isnull())
# print(df.describe())
# print(df.describe()['duration'])
# print(df.to_csv(path_or_buf="D:/log/t1.csv"))
#
# print(df.head(100).to_csv(path_or_buf="D:/log/t2.csv", header=True))
# print(min(1000, df.count()))
# print(df.head(100).head(min(1000, df.count())).to_csv(path_or_buf="D:/log/t3.csv", header=True))

# df.to_sql("mytable", engine, if_exists="replace", index=False, index_label='')
# print("_________________")
# df = pd.DataFrame({'id':[1,2,3,4],'num':[12,34,56,89]})
# df.to_sql('mydf', engine, index=False)
# print("success")