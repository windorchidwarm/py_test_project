#!/usr/bin/env python
# -- coding: utf-8 --#

from multiprocessing import Process
import threading
import time

def foo(i):
    time.sleep(1)
    print('this is thread, num is {0}'.format(str(i)))
    time.sleep(1)
    print('-- this is thread --, num is {0}'.format(str(i)))

if __name__ == '__main__':
    p_list = []

    for i in range(10):
        p = Process(target=foo, args=(i,))
        p.daemon = True
        p_list.append(p)

    for p in p_list:
        p.start()

    for p in p_list:
        p.join()