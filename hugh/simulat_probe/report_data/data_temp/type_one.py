from hugh.simulat_probe.report_data.data_temp.origin_data_base import OriginDataBase


class _OriginTypeOne(OriginDataBase):

    @property
    def connect_delay(self):
        """
        连接时延, 单位毫秒
        :return:
        """
        return None

    @property
    def byte_delay(self):
        """
        首字节时延, 单位毫秒
        :return:
        """
        return None

    @property
    def text_transfer_delay(self):
        """
        网页传输时延, 单位毫秒
        :return:
        """
        return None

    @property
    def text_open_delay(self):
        """
        网页打开时延，单位毫秒
        :return:
        """
        return None

    @property
    def text_length(self):
        """
        网页文本大小，单位KB
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
    def first_screen_delay(self):
        """
        首屏时延，单位毫秒
        :return:
        """
        return None

    @property
    def first_page_download_rate(self):
        """
        首页下载速率， 单位KB/s
        :return:
        """
        return None

    @property
    def status(self):
        """
        访问状态 1 - 正常, 2 - 失败
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


class TempTypeOne(_OriginTypeOne):
    """
    请调用这个类，这里只需要抛出最终的type1字典模板
    """

    @property
    def temp_data(self):
        """
        返回探针数据
        :return:
        """
        temp_data = dict(
            source=self.source,
            type=self.type,
            time=self.time,
            source_ip=self.source_ip,
            dest_ip=self.dest_ip,
            task_id=self.task_id,
            dns_delay=self.dns_delay,
            connect_delay=self.connect_delay,
            byte_delay=self.byte_delay,
            text_transfer_delay=self.text_transfer_delay,
            text_open_delay=self.text_open_delay,
            text_length=self.text_length,
            download_rate=self.download_rate,
            first_screen_delay=self.first_screen_delay,
            first_page_download_rate=self.first_page_download_rate,
            status=self.status,
            error_code=self.error_code,
            province_code=self.province_code,
            city_code=self.city_code,
            area_code=self.area_code
        )
        return temp_data
