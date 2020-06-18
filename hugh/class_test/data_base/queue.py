#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : queue.py
# Author: hugh
# Date  : 2020/6/18

class Queue:
    '''
    简单队列实现
    '''

    def __init__(self):
        self._items = []

    def is_empty(self):
        return self._items == []

    def enqueue(self, item):
        self._items.insert(0, item)

    def dequeue(self):
        return self._items.pop()

    def size(self):
        return len(self._items)

    def __str__(self):
        return str(self._items)


if __name__ == '__main__':
    '''
    '''
    q = Queue()
    print(q)
    q.enqueue(3)
    q.enqueue('dog')
    q.enqueue(True)
    print(q)
    q.dequeue()
    print(q)