from hugh.simulat_probe.report_data.data_temp.origin_data_base import OriginDataBase


class _OriginTypeTwo(OriginDataBase):
    @property
    def type(self):
        """
        数据类型 1-网站，2视频，3-游戏
        :return:
        """
        return 2

    @property
    def connect_delay(self):
        """
        连接时延, 单位毫秒
        :return:
        """
        return None

    @property
    def download_rate(self):
        """
        下载速率，单位KB/s
        :return:
        """
        return None

    @property
    def error_code(self):
        """
        # 错误码，“status” 失败时返回，http返回状态码
        :return:
        """
        return 404

    @property
    def download_time(self):
        """
        视频下载时间，单位毫秒
        :return:
        """
        return None

    @property
    def video_length(self):
        """
        视频内容大小，单位KB (预留接口)
        :return:
        """
        return None

    @property
    def frame_delay(self):
        """
        首帧到达时延, 单位毫秒
        :return:
        """
        return None

    @property
    def real_url(self):
        """
        视频真实地址
        :return:
        """
        return None

    @property
    def first_buffer_time(self):
        """
        首次缓冲时长, 单位毫秒
        :return:
        """
        return None

    @property
    def kpbs(self):
        """
        码率，单位KBbs
        :return:
        """
        return None

    @property
    def video_duration(self):
        """
         视频时间，单位秒
        :return:
        """
        return None

    @property
    def buffer_time(self):
        """
        总缓冲时间, 单位毫秒
        :return:
        """
        return None

    @property
    def delay_number(self):
        """
        卡顿次数
        :return:
        """
        return None

    @property
    def delay_rate(self):
        """
        卡顿率，单位为百分之，如23%
        :return:
        """
        return None


class TempTypeTwo(_OriginTypeTwo):
    """
    请调用这个类，这里只需要抛出最终的type2字典模板
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
            connect_delay=self.connect_delay,
            download_time=self.download_time,
            video_length=self.video_length,
            download_rate=self.download_rate,
            frame_delay=self.frame_delay,
            real_url=self.real_url,
            first_buffer_time=self.first_buffer_time,
            kpbs=self.kpbs,
            video_duration=self.video_duration,
            buffer_time=self.buffer_time,
            delay_number=self.delay_number,
            delay_rate=self.delay_rate,
            error_code=self.error_code,
            province_code=self.province_code,
            city_code=self.city_code,
            area_code=self.area_code

        )
        return probe_data
