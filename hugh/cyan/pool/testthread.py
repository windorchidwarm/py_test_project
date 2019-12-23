#!/usr/bin/env python
# -- coding: utf-8 --#

import threading
import time

globNum = 0
lock = threading.RLock()

def action(arg):
    time.sleep(1)
    mm = 0

    lock.acquire()
    global globNum
    globNum = globNum + 1
    mm = globNum
    lock.release()

    print('this is thread {0} {1} $$'.format(str(i), str(mm)))

class MyThread(threading.Thread):
    def __init__(self, args):
        super(MyThread, self).__init__()
        self.args = args

    def run(self):
        time.sleep(1)
        mm = 0

        lock.acquire()
        global globNum
        globNum = globNum + 1
        mm = globNum
        lock.release()

        print('this is my thread {0} {1} **'.format(str(self.args), str(mm)))

if __name__ == '__main__':
    for i in range(4):
        t = threading.Thread(target=action, args=(i,))
        t.start()
        print(t.getName())

    print('this is main end')
    print('######################')

    for i in range(9):
        g = MyThread(i)
        g.start()
        print(g.getName())