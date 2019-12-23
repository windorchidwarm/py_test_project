#!/usr/bin/env python
# -- coding: utf-8 --#

import numpy as np

class NumTest():
    def ndarray(self):
        al = np.array([[1, 3, 5, 7], [2, 4, 6, 8]])
        print(al.shape)
        print(al.dtype)
        print(al)
        a0 = np.zeros(6)
        print(a0)
        print(np.arange(8))

        dd = np.arange(12).reshape(2, 2, 3)
        print(dd)
        print(dd.transpose(0, 2, 1))
        # print(dd.swapaxes(1, 0, 2))

if __name__ == '__main__':
    nt = NumTest()
    nt.ndarray()