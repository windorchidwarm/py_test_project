#encoding:utf-8

import queue
import os

from . import get_context, TimeoutError

RUN = 0
CLOSE = 1
TERMINATE = 2

class Pool(object):
    '''池的书写 部分模仿 里面的内容比较多 仅用于理解 不可实际使用'''
    def __init__(self, processes=None, initializer=None, initargs=(),
                 maxtasksperchild=None, context=None):
        self._ctx = context or get_context()
        self._setup_queues()
        self._tastqueue = queue.Queue()
        self._cache = {}
        self._state = RUN
        self._maxtasksperchild = maxtasksperchild
        self._initializer = initializer
        self._initargs = initargs

        if processes is None:
            processes = os.cpu_count() or 1
        if processes < 1:
            raise ValueError("xxxxx")

        if initializer is not None and not callable(initializer):
            raise TypeError("initializer must be a callable")

        self._process = processes
        self._pool = []
        # self._repopulate_pool()

    def _setup_queues(self):
        self._inqueue = self._ctx.SimpleQueue()
        self._outqueue = self._ctx.SimpleQueue()
        self._quick_put = self._inqueue._writer.send
        self._quick_get = self._outqueue._reader.recv