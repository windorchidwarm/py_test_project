#!/usr/bin/env python
# -- coding: utf-8 --#
# @Time : 2020/4/21 13:26 
# @Author : Aries 
# @Site :  
# @File : priority_queue.py 
# @Software: PyCharm


from queue import PriorityQueue
import random


if __name__ == '__main__':
    '''
    优先队列测试
    '''

    q = PriorityQueue()
    q.put((3, 0, 'data'))
    q.put((6, 1, 'mike'))
    q.put((2, 2, 'hong'))
    q.put((3, 3, '四川'))
    q.put((14, 4, '外面'))

    n = 4

    while not q.empty():
        i, j, data = q.get()

        print(i, j, data)

        r = random.randint(2, 20)
        if r % 2 == 0:
            i = random.randint(2, 20)
            q.put((i, n, '测试' + str(n)))
            n += 1