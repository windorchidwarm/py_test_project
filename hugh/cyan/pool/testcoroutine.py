#!/usr/bin/env python
# -- coding: utf-8 --#

'''
协程 又作微线程
协程最大的优势就是协程极高的执行效率。因为子程序切换不是线程切换，而是由程序自身控制，
因此，没有线程切换的开销，和多线程比，线程数量越多，协程的性能优势就越明显。

第二大优势就是不需要多线程的锁机制，因为只有一个线程，也不存在同时写变量冲突，在协程中控制共享资源不加锁，
只需要判断状态就好了，所以执行效率比多线程高很多。
'''

import time

def comsumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        time.sleep(1)
        r = '200 Ok'

def producer(c):
    next(c)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()

def testYeild(a):
    b = yield a
    print('------>', a, b)
    c = yield b + a
    print('---->', a, b, c)

if __name__ == '__main__':
    # c = comsumer()
    # producer(c)
    # ty = testYeild(5)
    # next(ty)
    # ty.send(6)
    # ty.send(7)
    # ty.close()

    str = '35d13'
    i = 0
    try:
        i = int(str)
    except ValueError:
        i = 0

    print(i)


