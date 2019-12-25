#!/usr/bin/env python
# -- coding: utf-8 --#
# @Time : 2019/12/25 15:42 
# @Author : Aries 
# @Site :  
# @File : thread_test.py 
# @Software: PyCharm


import threading

class my_thread_a(threading.Thread):
    def run(self):
        global g_write, metex, ins

        while ins > 0:
            if metex.acquire(1):
                if g_write[-1] == 'D':
                    g_write.append('A')
                metex.release()

class my_thread_b(threading.Thread):
    def run(self):
        global g_write, metex, ins

        while ins > 0:
            if metex.acquire(1):
                if g_write[-1] == 'A':
                    g_write.append('B')
                metex.release()

class my_thread_c(threading.Thread):
    def run(self):
        global g_write, metex, ins

        while ins > 0:
            if metex.acquire(1):
                if g_write[-1] == 'B':
                    g_write.append('C')
                metex.release()

class my_thread_d(threading.Thread):
    def run(self):
        global g_write, metex, ins

        while ins > 0:
            if metex.acquire(1):
                if g_write[-1] == 'C':
                    g_write.append('D')

                    ins -= 1

                    if ins <= 0:
                        metex.release()
                        print(''.join(g_write))
                        break
                metex.release()


if __name__ == '__main__':
    ins = int(input().strip())
    g_write = ['A']
    metex = threading.Lock()

    task = []
    task.append(my_thread_a())
    task.append(my_thread_b())
    task.append(my_thread_c())
    task.append(my_thread_d())
    for each in task:
        each.setDaemon(True)
        each.start()
    for each in task:
        each.join()

