#!/usr/bin/env python
# -- coding: utf-8 --#
import importlib
import os
import sys

COMPONENT_PATH_ROOT = os.path.dirname(os.path.realpath(__file__)).replace(os.path.join('hugh', os.path.join('cyan', 'test')),'')
print(COMPONENT_PATH_ROOT)
sys.path.append(COMPONENT_PATH_ROOT)
COMPONENT_PATH_NOW = os.path.dirname(os.path.realpath(__file__)).replace('test', 'math')
print(COMPONENT_PATH_NOW)
sys.path.append(COMPONENT_PATH_NOW)
# COMPONENT_PATH_NOW = os.path.join(os.path.dirname(os.path.realpath(__file__)),os.path.join("hugh", os.path.join("cyan", "math")))
# print(COMPONENT_PATH_NOW)
# sys.path.append(COMPONENT_PATH_NOW)
COMPONENT_PATH_NOW = os.path.join(COMPONENT_PATH_NOW, 'mtest.py')

def test():
    print('dddd')


    print(COMPONENT_PATH_NOW)
    m = importlib.import_module('hugh.cyan.math.mtest', COMPONENT_PATH_NOW)
    print(m)
    cls = getattr(m, 'dtest')
    cls().executeNodes('haodldk')

test()