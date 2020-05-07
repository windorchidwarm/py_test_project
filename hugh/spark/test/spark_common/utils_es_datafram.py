#!/usr/bin/env python
# -*- coding: utf-8 -*-

from spark_common.utils_es import EsUtils


class EsDfUtils(EsUtils):

    @staticmethod
    def write_es(df, nodes, port, clusters_name, index, type, mode="append", mapping_id="main_id", timeout=300000):
        df.write.format("org.elasticsearch.spark.sql") \
            .option("es.nodes", nodes) \
            .option("es.resource", index + ('/{}'.format(type) if type else '')) \
            .option("es.mapping.id", mapping_id) \
            .option("es.port", port) \
            .option("clusters_name", clusters_name) \
            .option('es.input.json', 'false') \
            .option('es.http.timeout', timeout) \
            .mode(mode) \
            .save()


    @staticmethod
    def query_es(nodes, port, clusters_name, spark, index, query_str, type=None, include="", exclude="", timeout=300000):
        df = spark.read.format("org.elasticsearch.spark.sql") \
            .option("es.nodes", nodes) \
            .option("es.resource", index + ('/{}'.format(type) if type else '')) \
            .option("es.port", port) \
            .option("clusters_name", clusters_name) \
            .option("es.mapping.date.rich", "false") \
            .option("es.query", query_str) \
            .option('es.input.json', 'false') \
            .option('es.http.timeout', timeout) \
            .option('es.read.field.include', include) \
            .option('es.read.field.exclude', exclude) \
            .load()
        return df


if __name__ == '__main__':
    pass
