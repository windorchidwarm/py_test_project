#!/usr/bin/env python
# -- coding: utf-8 --#

import pandas as pd

class PandasTest:

    def seriesTest(self):
        obj = pd.Series([1, 2, 4, 23, 15, 8])
        print(obj)
        print(obj.values)
        print(obj.index)
        print(obj[3])

    def seriesTestIn(self):
        obj = pd.Series([1, 4, 54, 25], index=['a', 'b', 'c', 'd'])
        obj = obj.reindex(['a', 'b', 'c', 'd', 'g', 'h'], fill_value=0)
        print(obj['c'])
        print(obj['g'])
        dic = {"my":6, "own":1, "home":7}
        print(pd.Series(dic))

    def dataFrameTest(self):
        data = {'name':['calvin', 'kobe', 'michale', 'duarant', 'james'],
                'age':[29, 40, 45, 32, 19], 'height':[1.70, 1.60, 1.73, 1.46, 2.05]}
        data2 = [['a', 1], ['b', 2], ['c', 3]]
        data3 = {'one': pd.Series([1, 2, 3], index=['a', 'b', 'c']),
                 'two': pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}
        dd = pd.DataFrame(data3)
        print(dd)
        df = pd.DataFrame(data2, columns=['name', 'age'])
        print(df)
        print(dd['one'])

        # print(dd['one'])
        print(dd.loc['b'])
        print(dd[0:2])
        dg = pd.DataFrame(data)
        print(dg)
        del dd['one']
        print(dd)

    def readExcel(self, fileName):
        data = pd.read_excel(fileName)
        print(data)
        print(data.describe())

    def copySeries(self):
        obj = pd.Series(['red', 'yellow', 'blue'], index=[0, 2, 4])
        print(obj)
        obj = obj.reindex(range(6), method="ffill")
        print(obj)

if __name__ == '__main__':
    pt = PandasTest()
    # pt.seriesTest()
    # pt.seriesTestIn()
    # pt.dataFrameTest()
    pt.copySeries()