#encoding:utf-8

from enum import Enum, unique

'''
执行枚举状态
用于测试枚举写作
'''
@unique
class Tenum(Enum):
    SUCCESS = 0
    FAIL = -1
    RUNNING = 1
    WAITING = 2