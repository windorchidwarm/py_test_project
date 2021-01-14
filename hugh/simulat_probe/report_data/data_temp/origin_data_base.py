import time


class OriginDataBase:

    @property
    def source(self):
        """
        探针数据来源
        :return:
        """
        return 1

    @property
    def type(self):
        """
        数据类型 1-网站，2视频，3-游戏
        :return:
        """
        return 1

    @property
    def time(self):
        """
        探针上报时间
        :return:
        """
        return time.time()

    @property
    def source_ip(self):
        """
        探针ip
        :return:
        """
        return ''

    @property
    def dest_ip(self):
        """
        目的主机IP
        :return:
        """
        return ''

    @property
    def task_id(self):
        """
        任务ID
        :return:
        """
        return None

    @property
    def dns_delay(self):
        """
        dns时延，单位毫秒
        :return:
        """
        return None

    @property
    def province_code(self):
        """
        省行政区划代码
        :return:
        """
        return None

    @property
    def city_code(self):
        """
        市行政区划代码
        :return:
        """
        return None

    @property
    def area_code(self):
        """
        区县行政区划代码
        :return:
        """
        return None