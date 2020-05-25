#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : lru_test.py
# Author: BBD
# Date  : 2020/5/25

import collections

class LRUCache(collections.OrderedDict):

    def __init__(self, capacity: int):
        self.capacity = capacity


    def get(self, key: int) -> int:
        if key not in self:
            return -1
        self.move_to_end(key)
        return self[key]


    def put(self, key: int, value: int) -> None:
        if key in self:
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.capacity:
            self.popitem(last=False)