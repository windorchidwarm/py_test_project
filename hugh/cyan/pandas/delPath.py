#!/usr/bin/env python
# -- coding: utf-8 --#

import os

def delDir(path):
    if os.path.exists(path):
        try:
            for root, dirs, files in os.walk(path, topdown=False):
                if files != None and len(files) > 0:
                    for i in range(len(files)):
                        os.remove(os.path.join(root, files[i]))
                if dirs != None and len(dirs) > 0:
                    for i in  range(len(dirs)):
                        os.rmdir(os.path.join(root, dirs[i]))
            os.rmdir(path)
        except Exception as e:
            print(e)

if __name__ == '__main__':
    path = r'C:\Users\Administrator\Desktop\test\tmp212'
    delDir(path)