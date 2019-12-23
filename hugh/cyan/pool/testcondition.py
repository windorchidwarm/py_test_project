#!/usr/bin/env python
# -- coding: utf-8 --#

import threading
import time
import random

products = 0
condition = threading.Condition()

class produce(threading.Thread):

    def __init__(self):
        super(produce, self).__init__()

    def run(self):
        global  products
        while True:
            if condition.acquire():
                if products < 10:
                    products += 1
                    print('produce this is thread {0}, produces {1}'.format(str(threading.current_thread().getName()), str(products)))
                    condition.notify()
                    condition.release()
                else:
                    print('######produce this is thread {0}, produces {1}'.format(str(threading.current_thread().getName()), str(products)))
                    condition.wait()
                time.sleep(random.randint(1,3))

class consumer(threading.Thread):

    def __init__(self):
        super(consumer, self).__init__()

    def run(self):
        global  products
        while True:
            if condition.acquire():
                if products > 0:
                    products -= 1
                    print('consumer this is thread {0}, consumer {1}'.format(str(threading.current_thread().getName()), str(products)))
                    condition.notify()
                    condition.release()
                else:
                    print('&&&&&&&consumer this is thread {0}, consumer {1}'.format(str(threading.current_thread().getName()), str(products)))
                    condition.wait()
                time.sleep(random.randint(1,3))

if __name__ == '__main__':
    for p in range(2):
        p = produce()
        p.start()

    for c in range(3):
        c = consumer()
        c.start()