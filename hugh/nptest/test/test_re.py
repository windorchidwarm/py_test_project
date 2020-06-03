#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : test_re.py
# Author: BBD
# Date  : 2020/6/3


import re


isLetterDigitOrChinesePlot = '^[a-z0-9A-Z_\u4e00-\u9fa5\.]+$'


if __name__ == '__main__':
    '''
    '''
    re_test = re.compile(isLetterDigitOrChinesePlot)
    print(re_test.match('this_de.'))