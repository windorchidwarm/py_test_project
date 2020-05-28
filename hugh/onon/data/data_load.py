#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import date, timedelta, datetime
import time
import os, sys
import tempfile
from subprocess import Popen, PIPE


def excSubprocessCommand(command):
    out_temp = tempfile.SpooledTemporaryFile()
    file_no = out_temp.fileno()
    try:
        print(command)
        p = Popen(command, stdout=file_no, stderr=file_no, shell=True)
        p.communicate()
        out_temp.seek(0)
        for line in out_temp.readlines():
            print(line)
    finally:
        if out_temp:
            out_temp.close()


# hbase 创建表的语句
def create_table():
    command = 'hbase shell'
    process = Popen(command, stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True)
    create_table_shell = "create '%s' ,{NAME => '%s',COMPRESSION => 'SNAPPY'}\n" % (table_name, family_name)
    print(create_table_shell)
    process.stdin.write(create_table_shell)
    process.stdin.flush()
    process.stdin.write("exit\n")
    process.stdin.flush()
    process.stdin.close()
    print('创建HBASE表成功')


# hadoop 远程复制
def copy_hdfs():
    os.system("hadoop distcp " + source_hdfs_path + " " + target_hdfs_path)
    # os.system('hadoop fs -rm -r ' + source_hdfs_path)
    print('加载hdfs成功')

# 得到最终结果的指标输出顺序:
def make_hfile():
    delimiter = '|'  # 根据原csv文件格式决定
    columns = 'f1:name,f1:id,HBASE_ROW_KEY,f1:other'
    shell = """hbase org.apache.hadoop.hbase.mapreduce.ImportTsv 
        -Dmapreduce.map.output.compress=true 
        -Dmapreduce.map.output.compress.codec=org.apache.hadoop.io.compress.SnappyCodec 
        -Dhbase.mapreduce.bulkload.max.hfiles.perRegion.perFamily=1024 
        -Dimporttsv.separator="{delimiter}" 
        -Dimporttsv.bulk.output={gfileAbsolutePath} 
        -Dimporttsv.columns={columns} {tableName} {destinationDataAbsolutePath}
        """.replace("\n", " ").format(delimiter=delimiter,
                                      gfileAbsolutePath=hfile_tmp_path,
                                      columns=columns,
                                      tableName=table_name,
                                      destinationDataAbsolutePath=target_hdfs_path)
    excSubprocessCommand(shell)
    os.system('hadoop fs -rm -r ' + target_hdfs_path)
    print("生成hfile文件成功")


def load_hfile():
    shell = 'hbase org.apache.hadoop.hbase.mapreduce.LoadIncrementalHFiles %s %s' % (hfile_tmp_path, table_name)
    excSubprocessCommand(shell)
    os.system('hadoop fs -rm -r ' + hfile_tmp_path)
    print('导入hfile到HBASE成功')


def update_meta():
    # 元数据表
    meta_table = 'api_meta'
    row_key = 'actual_operation_address_v1'
    command = 'hbase shell'
    process = Popen(command, stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True)
    put = "put '{metaTable}','{rowKey}','f1:table','{tableName}'"\
        .format(metaTable=meta_table, rowKey=row_key, tableName=table_name)
    process.stdin.write('%s\n' % put)
    process.stdin.flush()
    print('更新元数据成功')
    # disable表
    last_table = 'hongjing:actual_operating_address_' + get_date(data_dt)
    process.stdin.write('disable %s\n' % last_table)
    process.stdin.flush()
    process.stdin.write("exit\n")
    process.stdin.flush()
    process.stdin.close()
    print('禁用表成功')


def get_date(version, days=7):
    dt_date = time.strptime(version, '%Y%m%d')
    delta = timedelta(days=days)
    dt_date_time = datetime.date(dt_date.tm_year, dt_date.tm_mon, dt_date.tm_mday)
    pre_date = dt_date_time - delta
    p_date_str = pre_date.strftime('%Y%m%d')
    return p_date_str


# 关闭无用的表
# def disable_table():
#     # 判断当前是否为当月的最后一个星期六
#     # 如果是，则保留最后一个
#     list_date = max_date()
#     last_date = max(list_date)
#     if now_date == last_date:
#         list_date.remove(last_date)
#         # 关闭表
#         print('disable')
#         command = 'hbase shell'
#         process = Popen(command, stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True)
#         for disable_date in list_date:
#             disable_table_name = 'qyxg_products_' + disable_date
#             print(disable_table_name)
#             process.stdin.write('disable %s\n' % disable_table_name)
#             process.stdin.flush()
#         process.stdin.write("exit\n")
#         process.stdin.flush()
#         process.stdin.close()
#         print('禁用表成功')


# 保留策略： 每月保留最后一个，保留一年
# def max_date():
#     m = datetime.now().month
#     y = datetime.now().year
#     n_days = (date(y, m + 1, 1) - date(y, m, 1)).days
#     day_one = date(y, m, 1)
#     last_day = date(y, m, n_days)
#     delta = last_day - day_one
#     data_list = []
#     for i in range(delta.days + 1):
#         p = (day_one + timedelta(days=i)).strftime('%Y%m%d')
#         pp = datetime.strptime(str(p), '%Y%m%d')
#         one = pp.isoweekday()
#         if one == 6:
#             d2 = pp.strftime('%Y%m%d')
#             data_list.append(d2)
#     return data_list


if __name__ == '__main__':
    # 1.在HBASE中创建表
    data_dt = sys.argv[1] if len(sys.argv) > 1 else datetime.datetime.now().strftime('%Y%m%d')
    table_name = 'table_name' + data_dt
    family_name = 'f1'
    create_table()
    # 2.拷贝至目标集群的hdfs上
    merged_result_path_base = '/user/all/'
    merged_result_path = os.path.join(merged_result_path_base, os.path.join(data_dt, 'data_all'))
    source_hdfs_path = "hdfs://source" + merged_result_path  # 源目标hdfs地址
    target_hdfs_path = "hdfs://target" + merged_result_path  # 目标hdfs地址
    copy_hdfs()
    # 3.生成HFile文件
    hfile_tmp_path = 'hdfs://target' + "/user/data/data_all"
    make_hfile()
    # 4.把生成的hfile文件导入HBASE中
    load_hfile()
    # 5.更新HBASE元数据
    update_meta()
