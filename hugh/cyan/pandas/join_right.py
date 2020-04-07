#!/usr/bin/env python
# -- coding: utf-8 --#
# @Time : 2020/4/7 13:37 
# @Author : Aries 
# @Site :  
# @File : join_right.py 
# @Software: PyCharm


import pandas as pd

import numpy as np

if __name__ == '__main__':
    print('xxxxxxxxx')
    leftDf = pd.read_csv(r'C:\Users\BBD\Desktop\test\tmp\2.csv')
    rightDf = pd.read_csv(r'C:\Users\BBD\Desktop\test\tmp\31.csv')
    print(leftDf)
    print(rightDf)

    data = rightDf.set_index(['class', 'name'])
    print(data)
    l_data = leftDf.set_index(['class', 'name'])
    print(l_data)
    allDf = leftDf.join(rightDf.set_index(['class', 'name']), on=['class', 'name'], how='right', lsuffix='_l', rsuffix='_r')
    print('xxxxxxxxxxxxxx')
    print(allDf)

    allDf2 = pd.merge(leftDf, rightDf, how='right', left_on=['class', 'name'], right_on=['class', 'name'], suffixes=('_x', '_y'))
    print(allDf2)

    ss = r'Traceback (most recent call last):\n  File "/usr/local/lib/python3.7/site-packages/sqlalchemy/engine/base.py", line 1248, in _execute_context\n    cursor, statement, parameters, context\n  File "/usr/local/lib/python3.7/site-packages/sqlalchemy/engine/default.py", line 588, in do_execute\n    cursor.execute(statement, parameters)\n  File "/usr/local/lib/python3.7/site-packages/pymysql/cursors.py", line 170, in execute\n    result = self._query(query)\n  File "/usr/local/lib/python3.7/site-packages/pymysql/cursors.py", line 328, in _query\n    conn.query(q)\n  File "/usr/local/lib/python3.7/site-packages/pymysql/connections.py", line 517, in query\n    self._affected_rows = self._read_query_result(unbuffered=unbuffered)\n  File "/usr/local/lib/python3.7/site-packages/pymysql/connections.py", line 732, in _read_query_result\n    result.read()\n  File "/usr/local/lib/python3.7/site-packages/pymysql/connections.py", line 1075, in read\n    first_packet = self.connection._read_packet()\n  File "/usr/local/lib/python3.7/site-packages/pymysql/connections.py", line 684, in _read_packet\n    packet.check_error()\n  File "/usr/local/lib/python3.7/site-packages/pymysql/protocol.py", line 220, in check_error\n    err.raise_mysql_exception(self._data)\n  File "/usr/local/lib/python3.7/site-packages/pymysql/err.py", line 109, in raise_mysql_exception\n    raise errorclass(errno, errval)\npymysql.err.InternalError: (1059, "Identifier name \'异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异\' is too long")\n\nThe above exception was the direct cause of the following exception:\n\nTraceback (most recent call last):\n  File "/opt/workdir/component_local/data_file.py", line 82, in execute\n    publicNodeLocal(nodeId, excuteId, publishConfig, executeVersion, outTableMetaDict, [allDf])\n  File "/opt/workdir/spark_common/local_uitils.py", line 286, in publicNodeLocal\n    df.to_sql(tableName, get_mysql_engine(), if_exists="replace", dtype=dtypedict)\n  File "/usr/local/lib/python3.7/site-packages/pandas/core/generic.py", line 2663, in to_sql\n    method=method,\n  File "/usr/local/lib/python3.7/site-packages/pandas/io/sql.py", line 521, in to_sql\n    method=method,\n  File "/usr/local/lib/python3.7/site-packages/pandas/io/sql.py", line 1316, in to_sql\n    table.create()\n  File "/usr/local/lib/python3.7/site-packages/pandas/io/sql.py", line 655, in create\n    self._execute_create()\n  File "/usr/local/lib/python3.7/site-packages/pandas/io/sql.py", line 641, in _execute_create\n    self.table.create()\n  File "/usr/local/lib/python3.7/site-packages/sqlalchemy/sql/schema.py", line 871, in create\n    bind._run_visitor(ddl.SchemaGenerator, self, checkfirst=checkfirst)\n  File "/usr/local/lib/python3.7/site-packages/sqlalchemy/engine/base.py", line 2058, in _run_visitor\n    conn._run_visitor(visitorcallable, element, **kwargs)\n  File "/usr/local/lib/python3.7/site-packages/sqlalchemy/engine/base.py", line 1627, in _run_visitor\n    visitorcallable(self.dialect, self, **kwargs).traverse_single(element)\n  File "/usr/local/lib/python3.7/site-packages/sqlalchemy/sql/visitors.py", line 144, in traverse_single\n    return meth(obj, **kw)\n  File "/usr/local/lib/python3.7/site-packages/sqlalchemy/sql/ddl.py", line 826, in visit_table\n    include_foreign_key_constraints,  # noqa\n  File "/usr/local/lib/python3.7/site-packages/sqlalchemy/engine/base.py", line 984, in execute\n    return meth(self, multiparams, params)\n  File "/usr/local/lib/python3.7/site-packages/sqlalchemy/sql/ddl.py", line 72, in _execute_on_connection\n    return connection._execute_ddl(self, multiparams, params)\n  File "/usr/local/lib/python3.7/site-packages/sqlalchemy/engine/base.py", line 1046, in _execute_ddl\n    compiled,\n  File "/usr/local/lib/python3.7/site-packages/sqlalchemy/engine/base.py", line 1288, in _execute_context\n    e, statement, parameters, cursor, context\n  File "/usr/local/lib/python3.7/site-packages/sqlalchemy/engine/base.py", line 1482, in _handle_dbapi_exception\n    sqlalchemy_exception, with_traceback=exc_info[2], from_=e\n  File "/usr/local/lib/python3.7/site-packages/sqlalchemy/util/compat.py", line 178, in raise_\n    raise exception\n  File "/usr/local/lib/python3.7/site-packages/sqlalchemy/engine/base.py", line 1248, in _execute_context\n    cursor, statement, parameters, context\n  File "/usr/local/lib/python3.7/site-packages/sqlalchemy/engine/default.py", line 588, in do_execute\n    cursor.execute(statement, parameters)\n  File "/usr/local/lib/python3.7/site-packages/pymysql/cursors.py", line 170, in execute\n    result = self._query(query)\n  File "/usr/local/lib/python3.7/site-packages/pymysql/cursors.py", line 328, in _query\n    conn.query(q)\n  File "/usr/local/lib/python3.7/site-packages/pymysql/connections.py", line 517, in query\n    self._affected_rows = self._read_query_result(unbuffered=unbuffered)\n  File "/usr/local/lib/python3.7/site-packages/pymysql/connections.py", line 732, in _read_query_result\n    result.read()\n  File "/usr/local/lib/python3.7/site-packages/pymysql/connections.py", line 1075, in read\n    first_packet = self.connection._read_packet()\n  File "/usr/local/lib/python3.7/site-packages/pymysql/connections.py", line 684, in _read_packet\n    packet.check_error()\n  File "/usr/local/lib/python3.7/site-packages/pymysql/protocol.py", line 220, in check_error\n    err.raise_mysql_exception(self._data)\n  File "/usr/local/lib/python3.7/site-packages/pymysql/err.py", line 109, in raise_mysql_exception\n    raise errorclass(errno, errval)\nsqlalchemy.exc.InternalError: (pymysql.err.InternalError) (1059, "Identifier name \'异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异\' is too long")\n[SQL: \nCREATE TABLE local_nationalcredit_data_mining_2638_0_20200407 (\n\t`异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据异常数据` NATIONAL VARCHAR(3000), \n\ttest INTEGER\n)\n\n]\n(Background on this error at: http://sqlalche.me/e/2j85)\n'
    print(len(ss))
    v = np.array([np.Infinity,np.Infinity,np.Infinity])
    print(v)
    v.round(8, v)
    v = np.nan_to_num(v).tolist()
    print(v)
