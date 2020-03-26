#!/usr/bin/env python
# -- coding: utf-8 --#
# @Time : 2020/3/12 14:59 
# @Author : Aries 
# @Site :  
# @File : empty.py 
# @Software: PyCharm



import json


if __name__ == '__main__':
    data_model_param = {}
    print(data_model_param)
    data_model_param['33'] = 33
    print(len(data_model_param))
    print(json.dumps({"0":"这是"}))
    print(json.dumps({"0": "来这里了"}))
    print(float('-inf'))

    data = {}
    data['xxx'] = 1
    data['yyyy'] = 2
    print(data)
    data.pop('xxx')
    print(data)
    if 'xy' in data.keys():
        del data['xy']
    print(data)
