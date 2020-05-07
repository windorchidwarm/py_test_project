#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime

"""
company_county表相关通用函数
"""

def all_table_distinct_sql(dt):
    """
    去重后的地区表
    :param dt:
    :return:
    """

    return '''
    select * from (
        select 
          *,
          row_number() over (partition by code order by (case when tag==0 then 2 else tag end)) as rank 
        from fta_dw.company_county 
        where dt = '{}'
    ) a where rank=1
    '''.format(dt)