#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : printer.py
# Author: hugh
# Date  : 2020/6/18

import random
from hugh.class_test.data_base.queue import Queue

class Printer:

    def __init__(self, ppm):
        self._page_rate = ppm
        self._current_task = None
        self._time_remaining = 0

    def tick(self):
        if self._current_task is not None:
            self._time_remaining = self._time_remaining - 1
            if self._time_remaining <= 0:
                self._current_task = None

    def busy(self):
        if self._current_task is not None:
            return True
        else:
            return False

    def start_next(self, new_task):
        self._current_task = new_task
        self._time_remaining = new_task.get_pages() * 60 / self._page_rate

class Task:

    def __init__(self, time):
        self._timestamp = time
        self._pages = random.randrange(1, 21)

    def get_stamp(self):
        return self._timestamp

    def get_pages(self):
        return self._pages

    def wait_time(self, current_time):
        return current_time - self._timestamp

def new_print_task():
    num = random.randrange(1, 181)
    if num == 180:
        return True


def sinulation(num_seconds, pages_per_minute):
    lab_printer = Printer(pages_per_minute)
    print_queue = Queue()
    waiting_times = []
    for current_second in range(num_seconds):
        if new_print_task():
            task = Task(current_second)
            print_queue.enqueue(task)
        if not lab_printer.busy() and not print_queue.is_empty():
            next_task = print_queue.dequeue()
            waiting_times.append(next_task.wait_time(current_second))
            lab_printer.start_next(next_task)
        lab_printer.tick()
    average_wait = sum(waiting_times) / len(waiting_times)
    print(average_wait)

if __name__ == '__main__':
    '''
    '''
    sinulation(3600, 5)