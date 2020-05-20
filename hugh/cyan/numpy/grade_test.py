#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : grade_test.py
# Author: chen
# Date  : 2020-05-20

import numpy as np

if __name__ == '__main__':
    '''
    全班成绩统计
    numpy 字符串类型
    整数	i
    无符号整数	u
    单精度浮点数	f
    双精度浮点数	d
    布尔值	b
    复数	D
    字符串	S
    Unicode	U
    Void	V
    '''
    person_types = np.dtype({
        'names':['xingming', 'chinese', 'english', 'math'],
        'formats':['U32', 'i', 'i', 'i']
    })
    print('中文')
    person_data = np.array([('张飞', 66, 63, 30), ('关羽', 95, 85, 98),
                            ('赵云', 93, 92, 96), ('黄忠', 90, 88, 77),
                            ('典韦', 80, 90, 90)], dtype=person_types)

    print(person_data)

    print(np.mean(person_data[:]['chinese']))
    print(np.min(person_data[:]['chinese']))
    print(np.max(person_data[:]['chinese']))
    print(np.std(person_data[:]['chinese']))
    print(np.var(person_data[:]['chinese']))

    x1 = np.arange(1, 11, 2)
    x2 = np.linspace(1, 9, 5)
    print(np.add(x1, x2))
    print(np.subtract(x1, x2))
    print(np.multiply(x1, x2))
    print(np.divide(x1, x2))
    print(np.power(x1, x2))
    print(np.remainder(x1, x2))

    print(np.mod(x1, x2))

    a = np.array([[1,2,3], [4,5,6],[7,8,9]])
    print(np.amin(a))
    print(np.amin(a, 0))
    print(np.amin(a, 1))
    print(np.amax(a))
    print(np.amax(a, 0))
    print(np.amax(a, 1))
    # 最大和最小值偏差
    print(np.ptp(a))
    print(np.ptp(a, 0))
    print(np.ptp(a, 1))
    # 百分位数
    print(np.percentile(a, 50))
    print(np.percentile(a, 50, axis=0))
    print(np.percentile(a, 50, axis=1))

    print(np.median(a))
    print(np.median(a, axis=0))
    print(np.median(a, axis=1))

    print(np.mean(a))
    print(np.mean(a, axis=0))
    print(np.mean(a, axis=1))

    print(np.sort(a, axis=0))
    print(np.sort(a, axis=1))