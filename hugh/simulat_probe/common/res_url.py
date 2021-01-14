import requests


class ResUrl:

    def __init__(self, host, path):
        """
        :param host: 地址
        :param path: 接口
        """
        self._host = host
        self._path = path

    def post(self, report_data):
        """
        请求数据
        :param report_data:
        :return:
        """
        # 这里的data可能需要json转格式，到时候再调试
        requests.post(url=self._host + self._path, data=report_data)
