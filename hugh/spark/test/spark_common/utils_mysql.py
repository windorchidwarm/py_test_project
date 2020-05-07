#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess


class MysqlUtils:
    def __init__(self, IP, PORT, DB_NAME, USER, PASSWORD):
        self.ip = IP
        self.port = PORT
        self.db_name = DB_NAME
        self.user = USER
        self.password = PASSWORD

        print("========================== ")
        print("连接数据库信息：" + IP + "：" + PORT + "," + USER + "," + PASSWORD + "," + DB_NAME)
        print("========================== ")

    def execute_sql(self, sqlStr):
        '''
        执行数据库查询操作
        :param self: 数据库连接类实例
        :param query: 需要执行的操作sql语句 String类型
        :return: 若成功则返回执行结果 list类型
        '''
        pass

    def get_table_meta(self, tableName=''):
        '''
        执行表查询元数据操作
        :param self: 数据库连接类实例
        :param tableName: 表名
        :return: 返回表信息
        '''
        sql = 'desc ' + tableName
        retDic = {}
        tableDesc = self.execute_sql(sql)
        for fieldDescTuple in tableDesc:
            retDic[fieldDescTuple[0]] = fieldDescTuple[1]
        return retDic

    def __replicate_table_structure(self, sourcTab, destTab, excludeColumn=''):
        '''
        复制已有表结构建新表（无数据）
        :param self: 数据库连接类实例
        :param sourcTab: 原表表名
        :param destTab: 新表表名
        :param excludeColumn: （optinal）不需被复制的列
        :return: 返回建表语句
        '''
        tabMetaDic = self.get_table_meta(sourcTab)
        excludeSet = set(excludeColumn.split(','))
        retSql = "CREATE TABLE " + destTab + " as SELECT   "
        select = ""
        for (k, v) in tabMetaDic.items():
            if k not in excludeSet:
                select = select + "," + k
        retSql = retSql + select[1:] + " from " + sourcTab
        return retSql

    def replicate_table(self, sourcTab, destTab="", excludeColumn=''):
        '''
        复制已有表到新表
        :param sourcTab: 原表表名
        :param destTab: 新表表名
        :param excludeColumn: （optinal）不需被复制的列
        :return:
        '''
        pass

    def dump_to_sql(self, table, sql_file):
        '''
        sql文件从mysql导出到本地
        :param tables: 导出表表名
        :param dir_name: 目标文件夹名
        :return: None
        '''
        dump_query = (
                "mysqldump "
                "-h {ip} "
                "-u {user} "
                "-p{passwd} "
                "-P {port}  "
                "--databases {database} "
                "-c -t --tables {table} > {sql_file}"
        ).format(
            ip=self.ip,
            port=self.port,
            user=self.user,
            passwd=self.password,
            database=self.db_name,
            table=table,
            sql_file=sql_file
        )
        if subprocess.call(dump_query, shell=True) != 0:
            print("数据导出错误： {table}".format(table=table))

    def sqoop_export(self, table, data_path, dt=None):
        '''
        用sqoop命令行的方式连接数据库，把数据从集群hdfs上批量导出到数据库
        :param self: 数据库连接配置
        :param table: 需要导入的数据库表名
        :param data_path: 数据存储在hdfs上的路径(需要使用绝对路径)
        :param dt: (optional) hdfs数据可能有分区信息，若没有则不填
        :return: None
        '''
        if dt:
            data_path = data_path + "/dt=" + dt
        export_commond = (
            "sqoop export "
            "--connect jdbc:mysql://{ip}:{port}/{db_name}?characterEncoding=UTF-8 "
            "--username {user} "
            "--num-mappers {mapper} "
            "--password '{password}' "
            "--table {table_name} "
            "--export-dir {absolute_path} "
            "--input-fields-terminated-by '\\t'"
        ).format(
            ip=self.ip,
            port=self.port,
            db_name=self.db_name,
            user=self.user,
            mapper=self.mapper,
            password=self.password,
            table_name=table,
            absolute_path=data_path
        )

        self.__get_shell_record(
            subprocess.call(export_commond, shell=True),
            "导入错误：{table} {data_path}".format(table=table, data_path=data_path)
        )

    def jdbc_read(self, spark, table):
        '''
        需要引mysql-connector.jar 包
        :param table: 数据库表名
        :return: spark dataframe 的mysql数据
        '''
        jdbc_query = (
            "jdbc:mysql://{ip}:{port}/{db_name}"
            "?user={user}"
            "&password={password}"
            "&characterEncoding=utf8"
        ).format(
            ip=self.ip,
            port=self.port,
            db_name=self.db_name,
            user=self.user,
            password=self.password
        )
        driver = "com.mysql.jdbc.Driver"
        df = spark.read.format("jdbc").options(
            url=jdbc_query,
            dbtable=table,
            driver=driver
        ).load()
        return df

    def jdbc_write(self, df, table, write_mode="overwrite"):
        '''
        :param df: spark df格式的数据
        :param table: 写入表名
        :param write_mode: 写入模式（默认为覆盖）
        :return: None
        '''
        jdbc_query = (
            "jdbc:mysql://{ip}:{port}/{db_name}"
            "?user={user}"
            "&password={password}"
            "&characterEncoding=utf8"
        ).format(
            ip=self.ip,
            port=self.port,
            db_name=self.db_name,
            user=self.user,
            password=self.password
        )
        driver = "com.mysql.jdbc.Driver"
        df.write.mode(write_mode).format("jdbc").options(
            url=jdbc_query,
            dbtable=table,
            driver=driver
        ).save()


if __name__ == '__main__':
    pass
