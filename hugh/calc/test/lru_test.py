#!/usr/bin/env python
# -- coding: utf-8 --#
# @Time : 2019/9/18 10:31 
# @Author : Aries 
# @Site :  
# @File : lru_test.py 
# @Software: PyCharm

class LRUCache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.keys = []

    def visit_key(self, key):
        if key in self.keys:
            self.keys.remove(key)
        self.keys.append(key)

    def elim_key(self):
        key = self.keys[0]
        self.keys = self.keys[1:]
        del self.cache[key]

    def get(self, key):
        if not key in self.keys:
            return -1
        self.visit_key(key)
        return self.cache[key]

    def put(self, key, value):
        if not key in self.keys:
            if len(self.keys) == self.capacity:
                self.elim_key()
        self.cache[key] = value
        self.visit_key(key)


def main():
    s = [["put","put","get","put","get","put","get","get","get"],[[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]]
    obj = LRUCache(2)
    l=[]
    for i,c in enumerate(s[0]):
        if c == "get":
            l.append(obj.get(s[1][i][0]))
        else:
            obj.put(s[1][i][0], s[1][i][1])
    print(l)

if __name__ == "__main__":
    print(bin(20))
    main()
