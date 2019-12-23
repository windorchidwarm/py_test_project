
#!/usr/bin/env python
# -- coding: utf-8 --#


import pandas as pd
import numpy as np
import datetime
import time

# allDf = pd.read_csv(r'C:\Users\Administrator\Desktop\test\tmp\titanic_1_1.csv')
# tDf = pd.read_csv(r'C:\Users\Administrator\Desktop\test\tmp\titanic_1_2.csv')
# allDf = allDf.append(tDf, ignore_index=True, sort=False)
# print(allDf)
# print(allDf.columns)
# allDf.to_csv(r'C:\Users\Administrator\Desktop\test\tmp\mm.csv', sep='\u0001', header=True, index=False)

#
# leftDf = pd.read_csv(r'C:\Users\Administrator\Desktop\test\tmp\titanic_1_1.csv')
# rightDf = pd.read_csv(r'C:\Users\Administrator\Desktop\test\tmp\titanic_2_1.csv')
# allDf = leftDf.join(rightDf.set_index(['Row No.']), on =['Row No.'], how='left', lsuffix='_l', rsuffix='_r')
# allDf.to_csv(r'C:\Users\Administrator\Desktop\test\tmp\mm.csv', header=True, index=False)

# gdf = pd.merge(leftDf, rightDf, how='left', on=None, left_on=['Row No.'], right_on=['Row No.'],
#       left_index=False, right_index=False, sort=False,
#       suffixes=('_l', '_r'), copy=True, indicator=True)
# gdf.to_csv(r'C:\Users\Administrator\Desktop\test\tmp\gg.csv', header=True, index=False)

# leftDf = pd.read_csv(r'C:\Users\Administrator\Desktop\test\tmp\titanic_1_1.csv')
# pp = leftDf['Row No.']
# pp = pp[pp > 500]
# print(pp.count())
# print(leftDf)

# maxv = time.strptime('2019-06-11 20:59:05', '%Y-%m-%d %H:%M:%S')
# minv = time.strptime('2019-06-11 11:28:04', '%Y-%m-%d %H:%M:%S')
# print(maxv)
# print(minv)
# maxv = datetime.datetime(*maxv[:6])
# minv = datetime.datetime(*minv[:6])
# print(maxv)
# print(minv)
# dateSpan = (maxv - minv) if maxv and minv else datetime.timedelta(0)
# print(dateSpan)
# print(dateSpan.seconds)
# print(minv + datetime.timedelta(seconds=dateSpan.seconds/10))

# upDf = pd.read_csv(r'C:\Users\Administrator\Desktop\test\tmp\titanic_1_1.csv')
# print(upDf.columns)
# dm = pd.get_dummies(upDf['Passenger Class_Second'], prefix='Passenger Class_Second', drop_first=False)
# print(dm.columns)
# upDf = pd.concat([upDf, dm], axis=1)
# print(upDf.columns)
# for fieldName in upDf.columns:
#     print(fieldName, '--->',str(upDf[fieldName].dtype).lower())

df = pd.read_csv(r'C:\Users\Administrator\Desktop\test\tmp\test_data.csv')

pp = df['float_data'].dropna()
percentile = np.percentile(pp, [0, 25, 50, 75, 100])
iqr = percentile[3] - percentile[1]
upLimit = percentile[3] + iqr * 1.5
downLimit = percentile[1] - iqr * 1.5
pp = pp[pp <= upLimit]
pp = pp[pp >= downLimit]
print(int(8 - pp.count()))
print(pp.count())
uf = df[df['float_data'] >= downLimit]
uf = uf[uf['float_data'] <= upLimit]
print(uf)

df['date_data'] = pd.to_datetime(df['date_data'])
datep = df['date_data'].dropna()
maxv = datep.max()
minv = datep.min()
print(type(datep), maxv, '---',minv, ':', type(maxv), datep.dtype)
dateSpan = (maxv - minv) if maxv and minv else datetime.timedelta(0)
print(dateSpan)
print(dateSpan.total_seconds())
print(maxv.strftime('%Y-%m-%d %H:%M:%S'))