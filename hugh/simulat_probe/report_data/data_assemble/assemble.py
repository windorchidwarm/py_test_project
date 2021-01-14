import random


class Assemble:

    def __init__(self, business_one, business_two, business_three):
        """
        接受修改好的数据
        :param business_one:
        :param business_two:
        :param business_three:
        """
        self._business_one = business_one
        self._business_two = business_two
        self._business_three = business_three

    def single_element(self):
        """
        生成最终的上报数据
        :return:
        """
        # 这里写简单的随机规则，组装成list，可能会有参数
        report_list = [self._business_one, self._business_two, self._business_three]
        random.shuffle(report_list)
        report_list = report_list[0: random.randint(0, len(report_list))]
        return report_list
