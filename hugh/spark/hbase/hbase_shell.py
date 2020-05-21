#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : hbase_shell.py
# Author: BBD
# Date  : 2020/5/11


hbase_shell_commond = '''
        flush '{data_table}'
        disable '{data_table}'
        drop '{data_table}'
        create '{data_table}',{{ NAME => '{fm}', COMPRESSION => 'snappy' }}, {{NUMREGIONS => {reg_num}, SPLITALGO => 'HexStringSplit'}}
        exit
        '''

if __name__ == '__main__':

    str_test = hbase_shell_commond.format(data_table = 'dd', fm = 'f1', reg_num=1024)
    print(str_test)