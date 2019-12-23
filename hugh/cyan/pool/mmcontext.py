#!/usr/bin/env python
# -- coding: utf-8 --#

import contextlib

@contextlib.contextmanager
def myopen(filename, mod):
    f = open(filename, mod)
    try:
        yield f.readlines()
    except Exception as e:
        print(e)
    finally:
        f.close()


@contextlib.contextmanager
def filenameFormat():
    print('《', end='')
    yield
    print('》', end='')

if __name__ == '__main__':
    with myopen(r'C:\Users\Administrator\Desktop\test\tmp\tr.txt', 'r') as f:
        for line in f:
            print(line)

    with filenameFormat():
        print('梦的解析', end='')