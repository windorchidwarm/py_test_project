import time
import random

from hugh.simulat_probe.report_data.data_business.base import CheckData


class BusinessTypeOne(CheckData):

    def __init__(self, temp_data):
        # 拿到模板数据
        self._temp_data = temp_data

    def probe_data(self):
        """
        返回修改完成的type1字典
        :return:
        """
        funcs = (self.source, self.type, self.time, self.source_ip, self.dest_ip, self.task_id, self.dns_delay,
                 self.connect_delay, self.byte_delay, self.text_transfer_delay, self.text_open_delay,
                 self.text_length, self.download_rate, self.first_screen_delay, self.first_page_download_rate,
                 self.status, self.error_code, self.province_code, self.city_code, self.area_code)
        # 验证是否有可调用函数
        self.yes_funcs(temp_data=self._temp_data, func_name=[func.__name__ for func in funcs])
        for i in funcs:
            i()

        # 匹配模板中有的字段，得到新的funcs列表
        funcs = self.funcs(temp_data=self._temp_data, funcs=funcs)
        if funcs:
            [func(is_random=False) for func in funcs]
        else:
            raise KeyError('未匹配到任何可用的字段')
        return self._temp_data

    def source(self, *, is_random=False):
        """
        修改该字段的数据
        :param is_random 是否生成告警数据，True时，生成满足告警的数据，False时，生成正常的数据，默认正常
        :return:
        """
        # 通过 is_random 来控制是否生成该字段的告警数据
        source = 0
        self._temp_data['source'] = source

    def type(self, *, is_random=False):
        """
        类型
        :return:
        """
        self._temp_data['type'] = 1

    def time(self, *, is_random=False):
        """
        修改字段的数据

        :return:
        """

        self._temp_data['time'] = time.time()

    def source_ip(self, *, is_random=False):
        """
        修改探针ip
        :return:
        """
        self._temp_data['source_ip'] = ''

    def dest_ip(self, *, is_random=False):
        """

        :return:
        """
        self._temp_data['dest_ip'] = ''

    def task_id(self, *, is_random=False):
        """

        :return:
        """

        self._temp_data['task_id'] = None

    def dns_delay(self, *, is_random=False):
        """
        dns时延，单位毫秒
        :return:
        """
        dns_delay = random.uniform(1.1, 5.4)
        self._temp_data['dns_delay'] = dns_delay

    def connect_delay(self, *, is_random=False):
        """
        连接时延, 单位毫秒
        :return:
        """
        connect_delay = random.uniform(1.5, 19.2)
        self._temp_data['connect_delay'] = connect_delay

    def byte_delay(self, *, is_random=False):
        """
        首字节时延, 单位毫秒
        :return:
        """
        byte_delay = random.uniform(1.5, 29.2)
        self._temp_data['byte_delay'] = byte_delay

    def text_transfer_delay(self, *, is_random=False):
        """
        网页传输时延，单位毫秒
        :return:
        """
        text_transfer_delay = random.uniform(4.5, 94.3)
        self._temp_data['text_transfer_delay'] = text_transfer_delay

    def text_open_delay(self, *, is_random=False):
        """
        网页打开时延，单位毫秒
        :return:
        """
        text_open_delay = random.uniform(6.5, 321.1)
        self._temp_data['text_open_delay'] = text_open_delay

    def text_length(self, *, is_random=False):
        """
        网页文本大小，单位KB
        :return:
        """
        text_length = random.uniform(7.6, 762.8)
        self._temp_data['text_length'] = text_length

    def download_rate(self, *, is_random=False):
        """
        下载速率，单位KB/s
        :return:
        """
        download_rate = random.uniform(8.5, 213.2)
        self._temp_data['download_rate'] = download_rate

    def first_screen_delay(self, *, is_random=False):
        """
        首屏时延，单位毫秒
        :return:
        """
        first_screen_delay = random.uniform(2.1, 82.2)
        self._temp_data['first_screen_delay'] = first_screen_delay

    def first_page_download_rate(self, *, is_random=False):
        """
        首页下载速率， 单位KB/s
        :return:
        """
        first_page_download_rate = random.uniform(23.1, 8921.2)
        self._temp_data['first_page_download_rate'] = first_page_download_rate

    def status(self, *, is_random=False):
        """
        访问状态 1 - 正常, 2 - 失败
        :return:
        """
        self._temp_data['status'] = 1

    def error_code(self, *, is_random=False):
        """

        :return:
        """
        if self._temp_data['status'] == 2:
            self._temp_data['error_code'] = 404
        else:
            self._temp_data['error_code'] = None

    def province_code(self, *, is_random=False):
        """
        省行政区划代码
        :return:
        """
        self._temp_data['province_code'] = 440000

    def city_code(self, *, is_random=False):
        """
        市行政区划代码
        :return:
        """
        cities = [440100, 440200, 440300, 440400, 440500, 440600, 440700, 440800, 440900, 441200, 441300, 441400,
                  441500,
                  441600, 441700, 441800, 441900, 442000, 445100, 445200, 445300]
        slt_city = random.choice(cities)
        self._temp_data['city_code'] = slt_city

    def area_code(self, *, is_random=False):
        """
        区县行政区划代码
        :return:
        """
        areas = [440103, 440104, 440105, 440106, 440111, 440112, 440113, 440114, 440115, 440116, 440183, 440184, 440188,
                 440189, 440203, 440204, 440205, 440222, 440224, 440229, 440232, 440233, 440281, 440282, 440283, 440303,
                 440304, 440305, 440306, 440307, 440308, 440309, 440402, 440403, 440404, 440486, 440487, 440488, 440507,
                 440511, 440512, 440513, 440514, 440515, 440523, 440524, 440604, 440605, 440606, 440607, 440608, 440609,
                 440703, 440704, 440705, 440781, 440783, 440784, 440785, 440786, 440802, 440803, 440804, 440811, 440823,
                 440825, 440881, 440882, 440883, 440884, 440902, 440903, 440923, 440981, 440982, 440983, 440984, 441202,
                 441203, 441223, 441224, 441225, 441226, 441283, 441284, 441285, 441302, 441303, 441322, 441323, 441324,
                 441325, 441402, 441421, 441422, 441423, 441424, 441426, 441427, 441481, 441482, 441502, 441521, 441523,
                 441581, 441582, 441602, 441621, 441622, 441623, 441624, 441625, 441626, 441702, 441721, 441723, 441781,
                 441782, 441802, 441821, 441823, 441825, 441826, 441827, 441881, 441882, 441883, 445102, 445121, 445122,
                 445185, 445186, 445202, 445221, 445222, 445224, 445281, 445284, 445285, 445302, 445321, 445322, 445323,
                 445381, 445382]
        slt_area = random.choice(areas)
        self._temp_data['area_code'] = slt_area
