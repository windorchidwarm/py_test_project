#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : sns_test.py
# Author: hugh
# Date  : 2020/5/13

# %matplotlib inline
import numpy as np
import pandas as pd
from scipy import stats, integrate
import matplotlib.pyplot as plt #导入

import seaborn as sns
sns.set(color_codes=True)#导入seaborn包设定颜色

np.random.seed(sum(map(ord, "distributions")))

x = np.random.normal(size=100)
p = sns.distplot(x, kde=True, rug=True)    #kde=False关闭核密度分布,rug表示在
plt.legend()
plt.show(p)

