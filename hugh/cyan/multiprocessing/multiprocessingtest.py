#!/usr/bin/env python
# -- coding: utf-8 --#
# @Time : 2019/9/10 10:47 
# @Author : Aries 
# @Site :  
# @File : multiprocessingtest.py 
# @Software: PyCharm

from multiprocessing import Pool
import os, time, random

def long_time_task(name): #执行函数
    print('run task %s (%s)...'% (name,os.getpid()))
    start = time.time()
    time.sleep(random.random()*30)#random()生成0-1之间的随即实数
    end = time.time()
    print('task %s run %0.2f seconds.'% (name,end-start))

if __name__ =='__main__':
    print('parents process %s.'% os.getpid())
    p = Pool(4)
    for i in range(8):
        p.apply_async(long_time_task, args = (i,))#apply_async()方法下面说明
        print('waiting for all subprocesses done...')
    p.close()#关闭进程池,不在接收新的任务
    p.join()
    print('all subprocesses done')