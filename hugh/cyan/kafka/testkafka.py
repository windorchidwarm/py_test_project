#!/usr/bin/env python
# -- coding: utf-8 --#
# @Time : 2019/9/6 11:35 
# @Author : Aries 
# @Site :  
# @File : testkafka.py 
# @Software: PyCharm

from pykafka import KafkaClient


zookeeper_hosts = '''10.28.103.17:2181,10.28.103.18:2181,10.28.103.19:2181,10.28.103.20:2181,10.28.103.21:2181'''
kafka_hosts = '''10.28.103.17:9092,10.28.103.18:9092'''
kafka_hosts_lone = '''ops7.bbdops.com:9092'''
zookeeper_hosts_lone = '''ops7.bbdops.com:2181'''


def kafka_consumer():
    # client = KafkaClient(zookeeper_hosts=zookeeper_hosts)
    client = KafkaClient(hosts=kafka_hosts_lone)
    # client = KafkaClient(zookeeper_hosts = zookeeper_hosts_lone)
    print(client.topics)

if __name__ == '__main__':
    kafka_consumer()
    print('------------')