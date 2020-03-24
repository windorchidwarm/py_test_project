#!/usr/bin/env python
# -- coding: utf-8 --#
# @Time : 2020/3/23 17:05 
# @Author : Aries 
# @Site :  
# @File : test_local.py 
# @Software: PyCharm

import pandas as pd
from hugh.onon.guiyang.local_uitils import *


pre = pd.read_csv(r'C:\Users\BBD\Desktop\test\tmp\12345.csv')
print(pre)
data = dataDistributionLocal(pre)
print(data)