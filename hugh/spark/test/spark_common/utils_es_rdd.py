#!/usr/bin/env python
# -*- coding: utf-8 -*-

from spark_common.utils_es import EsUtils

class EsRddUtils(EsUtils):


    @staticmethod
    def write_es(nodes, port, clusters_name, input_rdd, index, type=None, mapping_id=None, timeout=300000):
        es_write_conf = {"es.resource": index + ('/{}'.format(type) if type else ''),
                         "es.nodes": nodes,
                         'clusters_name': clusters_name,
                         "es.mapping.id": mapping_id,
                         'es.http.timeout': timeout,
                         'es.input.json': 'true',
                         "es.port": port}
        input_rdd.saveAsNewAPIHadoopFile(
            path='-',
            outputFormatClass="org.elasticsearch.hadoop.mr.EsOutputFormat",
            keyClass="org.apache.hadoop.io.NullWritable",
            valueClass="org.elasticsearch.hadoop.mr.LinkedMapWritable",
            conf=es_write_conf)

    @staticmethod
    def query_es(nodes, port, clusters_name, spark, index, query_str, type=None, include="", exclude="", timeout=300000):

        es_query_conf = {"es.resource": index + ('/{}'.format(type) if type else ''),
                         "es.nodes": nodes,
                         'clusters_name': clusters_name,
                         'es.http.timeout': timeout,
                         'es.input.json': 'true',
                         "es.port": port,
                         "es.query": query_str,
                         "es.read.field.include": include,
                         "es.read.field.exclude": exclude
                         }

        data_rdd = spark.sparkContext.newAPIHadoopRDD(
            inputFormatClass="org.elasticsearch.hadoop.mr.EsInputFormat",
            keyClass="org.apache.hadoop.io.NullWritable",
            valueClass="org.elasticsearch.hadoop.mr.LinkedMapWritable",
            conf=es_query_conf)
        return data_rdd
