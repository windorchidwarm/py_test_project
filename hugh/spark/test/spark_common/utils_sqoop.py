#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import subprocess


class SqoopUtils:

    @staticmethod
    def sqoop_export(host, port, db_name, user, password, table_name, hdfs_path, map_num):
        export_command = r'''
            sqoop import --append 
            --connect jdbc:mysql://{host}:{port}/{db_name} 
            --username {user} 
            --password {password} 
            --table {table_name} 
            --as-textfile 
            --target-dir {hdfs_path} 
            --fields-terminated-by '\001' 
            --input-null-string '\\N' 
            --input-null-non-string '\\N' 
            -m {map_num} 
            --hive-drop-import-delims
            '''.format(host=host,
                       port=port,
                       db_name=db_name,
                       user=user,
                       password=password,
                       table_name=table_name,
                       hdfs_path=hdfs_path,
                       map_num=map_num)
        p = subprocess.Popen(export_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        outline = p.communicate()
        for l in outline:
            print(l)
        if p.returncode != 0:
            raise Exception("***** from {}:{} export table {} fail *****".format(host, port, table_name))
