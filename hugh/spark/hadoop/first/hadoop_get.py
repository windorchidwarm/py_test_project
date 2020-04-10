#!/usr/bin/env python
# -- coding: utf-8 --#

import os
import sys

if __name__ == '__main__':
    hdfsstr = 'hadoop dfs -get  /user/bbders/data_mining/trained_data/7352/metadata/part-00000 /home/bbders/tetris_schedule/logs/'
    os.system(hdfsstr)