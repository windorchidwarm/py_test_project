#!/usr/bin/env python
# -- coding: utf-8 --#

from multiprocessing import Pool, Array, Process,Manager
import threading
import time

def Foo(i):
    time.sleep(2)
    print('$$$ {0} {1}'.format(threading.current_thread(), i))
    return i + 100

def FooM(i):
    time.sleep(1)
    print('-----------> thread {0} num {1}'.format(threading.current_thread().getName(), str(i)))

def Bar(i):
    print(i)

def FooA(a):
    for i in range(len(a)):
        a[i] = -a[i]

def FooAM(d, l):
    d[1] = '1'
    d['2'] = 2
    d[0.25] = None
    l.reverse()

if __name__ == '__main__':
    # t_start = time.time()
    #
    # pool = Pool(3)
    # for i in range(10):
    #     pool.apply_async(func=Foo, args=(i,), callback=Bar)
    #
    # pool.close()
    # pool.join()
    # pool.terminate()
    # t_end = time.time()
    # print('this time long is {0}'.format(str(t_end-t_start)))

    # t_start = time.time()
    # poolM = Pool(3)
    # #同步线程顺序执行 效率较低
    # for i in range(10):
    #     poolM.apply(func=FooM, args=(i,))
    # poolM.close()
    # poolM.join()
    # t_end = time.time()
    # print('-------------this time long is {0}'.format(str(t_end - t_start)))

    # t_start = time.time()
    # pool = Pool(4)
    # res_list = []
    # for i in range(20):
    #     res = pool.apply_async(func=Foo, args=(i,))
    #     res_list.append(res)
    # pool.close()
    # pool.join()
    #
    # for res in res_list:
    #     print(res.get())
    #
    # t_end = time.time()
    # print('this time long is {0}'.format(str(t_end-t_start)))

    t_start = time.time()
    pool = Pool(4)
    a = Array('i', range(10))
    p = Process(target=FooA, args=(a,))
    p.start()
    p.join()
    print(a[:])
    t_end = time.time()
    print('this time long is {0}'.format(str(t_end - t_start)))

    with Manager() as manager:
        d = manager.dict()
        l = manager.list(range(10))
        pld = Process(target=FooAM, args=(d, l))
        pld.start()
        pld.join()
        print(d)
        print(l)


