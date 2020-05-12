#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import subprocess

class HbaseUtils:

    hbase_shell_commond = '''
        flush '{data_table}'
        disable '{data_table}'
        drop '{data_table}'
        create '{data_table}',{{ NAME => '{fm}', COMPRESSION => 'snappy' }}, {{NUMREGIONS => {reg_num}, SPLITALGO => 'HexStringSplit'}}
        exit
        '''
    hbase_meta_commond = '''
        put  '{meta_table}','{meta_rowkey}','f1:table','{data_table}'
        exit
        '''

    @staticmethod
    def excSubprocessCommand(command,commandTps=None):
        if commandTps:
            print (commandTps + command)
        p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        outline = p.communicate()
        for l in outline:
            print(l)
        return p.returncode == 0

    @staticmethod
    def hbaseShellExc(hbaseshellFile, command=None):

        hbaseshellPath = os.path.split(hbaseshellFile)[0]
        if not os.path.exists(hbaseshellPath):
            os.makedirs(hbaseshellPath)

        if command:
            if "exit" not in command:
                command = command+"\nexit"
            hbase_meta_shell = open(hbaseshellFile, 'w')
            hbase_meta_shell.write(command)
            hbase_meta_shell.close()

        ok = HbaseUtils.excSubprocessCommand('hbase shell  ' + hbaseshellFile)

        return ok


    @staticmethod
    def bulkload_hbase(
            dataPath,
            hfilePath,
            dataTable,
            metaTable,
            metaRokey,
            columns,
            reg_num,
            hbaseshellFile,
            delimiter='\t',
            updateMeta=False,
            fm='f1'
    ):
        '''

        :param dataPath: 输入的数据路径
        :param hfilePath: 指定生成hfie的路径
        :param dataTable: hbase 表名
        :param metaTable: meta表名
        :param metaRokey: 要更新的meta表Rowkey
        :param columns: 对应的hbase列 fm:column
        :param reg_num: hbase表初始化的region个数
        :param hbaseshellFile: 用于可生成hbaseshell文件的路径
        :param delimiter: 输入数据的数据分割符
        :param updateMeta: 是否更新 Metam表
        :param fm: 列簇
        :return:
        '''
        # 创建hbase表 命名规则 tablename_yyyymmm
        HbaseUtils.hbaseShellExc(
            hbaseshellFile,
            command=HbaseUtils.hbase_shell_commond.format(data_table=dataTable,fm=fm,reg_num=reg_num)
        )

        #生成hfile
        os.system("hadoop fs -rm -f -r "+  hfilePath)
        command_create_hfile = (
            'hbase org.apache.hadoop.hbase.mapreduce.ImportTsv ' 
            '-Dmapreduce.map.output.compress=true  ' 
            '-Dmapreduce.map.output.compress.codec=org.apache.hadoop.io.compress.SnappyCodec ' 
            '-Dhbase.mapreduce.bulkload.max.hfiles.perRegion.perFamily=1024   ' 
            '-Dimporttsv.separator="{delimiter}" ' 
            '-Dimporttsv.bulk.output={hfile} ' 
            '-Dimporttsv.columns={columns} ' 
            '{dataTable} {dataPath}'
        ).format(
            delimiter=delimiter,
            hfile=hfilePath,
            columns=columns,
            dataTable=dataTable,
            dataPath=dataPath
        )

        ok = HbaseUtils.excSubprocessCommand(command_create_hfile,"command_create_hfile ===> ")
        if ok!=True:
            raise Exception("生成HFile失败")

        # 导入hbase
        command_import = (
            'hbase org.apache.hadoop.hbase.mapreduce.LoadIncrementalHFiles '
            '{hfile} '
            '{dataTable}'
        ).format(hfile=hfilePath,dataTable=dataTable)
        ok = HbaseUtils.excSubprocessCommand(command_import, "command_load_hfile ===> ")
        if ok!=True:
            raise Exception("导入HBase失败")

        #更新meta表
        if updateMeta:
            ok = HbaseUtils.hbaseShellExc(
                hbaseshellFile+'_meta',
                HbaseUtils.hbase_meta_commond.format(meta_table=metaTable,data_table=dataTable,meta_rowkey=metaRokey)
            )
            if ok != True:
                raise Exception("更新hbase meta失败")

