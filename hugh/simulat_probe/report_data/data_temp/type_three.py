from hugh.simulat_probe.report_data.data_temp.origin_data_base import OriginDataBase


class _OriginTypeThree(OriginDataBase):
    @property
    def type(self):
        """
        数据类型 1-网站，2视频，3-游戏
        :return:
        """
        return 3

    @property
    def send_num(self):
        """
        发送数据包数量
        :return:
        """
        return None

    @property
    def recv_num(self):
        """
        接收数据包数量
        :return:
        """
        return None

    @property
    def delay(self):
        """
        ping时延
        :return:
        """
        return None


class TempTypeThree(_OriginTypeThree):
    """
    请调用这个类，这里只需要抛出最终的type3字典模板
    """

    @property
    def temp_data(self):
        """
        返回探针数据
        :return:
        """
        probe_data = dict(
            source=self.source,
            time=self.time,
            type=self.type,
            source_ip=self.source_ip,
            dest_ip=self.dest_ip,
            task_id=self.task_id,
            dns_delay=self.dns_delay,
            send_num=self.send_num,
            recv_num=self.recv_num,
            delay=self.delay,
            province_code=self.province_code,
            city_code=self.city_code,
            area_code=self.area_code
        )
        return probe_data
