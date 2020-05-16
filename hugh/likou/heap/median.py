#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : median.py
# Author: chen
# Date  : 2020-05-12


import heapq


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.count = 0
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num: int) -> None:
        self.count += 1
        # 因为 Python 中的堆默认是小顶堆，所以要传入一个 tuple，用于比较的元素需是相反数
        # 才能模拟出大顶堆的效果
        heapq.heappush(self.max_heap, (-num, num))
        _, max_heap_top = heapq.heappop(self.max_heap)
        heapq.heappush(self.min_heap, max_heap_top)
        if self.count % 2 == 1:
            min_heap_top = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, (-min_heap_top, min_heap_top))

    def findMedian(self) -> float:
        if self.count % 2 == 1:
            return self.max_heap[0][1]
        else:
            return (self.min_heap[0] + self.max_heap[0][1]) / 2


if __name__ == '__main__':
    ll = MedianFinder()
    ll.addNum(1)
    print(ll.max_heap, ll.min_heap, ll.findMedian())

    ll.addNum(6)
    print(ll.max_heap, ll.min_heap, ll.findMedian())

    ll.addNum(3)
    print(ll.max_heap, ll.min_heap, ll.findMedian())

    ll.addNum(2)
    print(ll.max_heap, ll.min_heap, ll.findMedian())

    ll.addNum(9)
    print(ll.max_heap, ll.min_heap, ll.findMedian())