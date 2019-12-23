#!/usr/bin/env python
# -- coding: utf-8 --#
# @Time : 2019/9/10 11:21 
# @Author : Aries 
# @Site :  
# @File : processpool.py 
# @Software: PyCharm

from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor

global g_index

import os,time,random
def task(n):
    global g_index
    print("g_index start:", g_index)
    print('%s is runing' %os.getpid())
    time.sleep(random.randint(1,3))
    g_index -= 1
    print("g_index end:", g_index)
    return n**2

if __name__ == '__main__':

    executor=ProcessPoolExecutor(max_workers=3)

    futures=[]
    global g_index
    g_index = 0
    codes = []
    for i in range(11):
        codes.append(i)
    while True:
        if(g_index < 3):
            g_index += 1
            print("g_index:", g_index)
            future=executor.submit(task,i)
            futures.append(future)
            print("g_index any:", g_index)
    executor.shutdown(True)
    print('+++>')
    for future in futures:
        print(future.result())