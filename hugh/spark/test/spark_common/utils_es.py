#!/usr/bin/env python
# -*- coding: utf-8 -*-

from elasticsearch import Elasticsearch
import time


class EsUtils:

    @staticmethod
    def get_es(hosts, timeout=300000):
        """
        es连接
        :param hosts: 地址数值[{'host': 'host', 'port': int('post')}]
        :return:
        """
        es = Elasticsearch(hosts=hosts, timeout=timeout)
        return es

    @staticmethod
    def delete_es_data(es, index, type, query):
        """
        条件删除es数据（等待异步删除完成）
        :param es: es连接
        :param index: 索引
        :param type: 索引type
        :param query: 条件
        :return:
        """
        if not query:
            raise Exception("es删除条件必须明确")
        if es.indices.exists(index) and es.indices.exists_type(index, type):
            tid = es.delete_by_query(
                index=index,
                body=query,
                doc_type=type,
                params={"wait_for_completion": "false"})
            doing = True
            while doing:
                time.sleep(2)
                x = es.tasks.get(tid["task"])
                if x["completed"] == True:
                    break

