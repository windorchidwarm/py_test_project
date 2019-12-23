#!/usr/bin/env python
# -- coding: utf-8 --#

import argparse
import json

class DistributionRatio:
    def __init__(self, seat, **people):
        '''
        初始化方法，须传入席位，以及类别和对应的数据
        :param seat:
        :param people:
        '''
        self.seat = seat
        self.people = people

    def distribution(self):
        '''
        分配席位的方法
        直接用的初始化1 然后根据Q值法分配
        如果优化 可以采用先按照等比例分配下限 然后再采用Q值法
        :return:
        '''
        self.perSeat = {}

        # 如果座位数大于分组数则初始化 否则直接按人数顺序分配 这里暂不判断 仅仅为demo

        for key in self.people.keys():
            self.perSeat[key] = 1

        waitPer = ''
        waitNum = 0
        waitQ = 0

        shouldWaitSeat = self.seat - len(self.people)

        while shouldWaitSeat > 0:
            for key in self.people.keys():
                nWaitSeat = int(self.perSeat[key])
                nWaitNum = int(self.people[key])
                nWaitQ = 0
                if nWaitSeat != 0:
                    nWaitQ = nWaitNum ** 2 / (nWaitSeat * (nWaitSeat + 1))
                else:
                    nWaitQ = 0

                if waitPer.strip() == '':
                    waitPer = key
                    waitNum = nWaitNum
                    waitQ = nWaitQ

                if nWaitQ > waitQ or (nWaitQ == waitQ and nWaitNum > waitNum):
                    waitPer = key
                    waitNum = nWaitNum
                    waitQ = nWaitQ

            self.perSeat[waitPer] = self.perSeat[waitPer] + 1
            print(self.perSeat, end='')
            print(" -----> ", end='')
            print(waitQ)
            waitPer = ''
            waitNum = 0
            waitQ = 0
            shouldWaitSeat -= 1
        print(self.perSeat)
        print(self.people)
        return  self.perSeat

parser = argparse.ArgumentParser(description='node args')
parser.add_argument('-nd', '--nodeArgs', type=str)
args = parser.parse_args()
print(args)
print(args.nodeArgs)
print("*************")
some = args.nodeArgs.replace("*", "\"")
nodeArgs = json.loads(some)
print(nodeArgs)

if __name__ == '__main__':
    print(nodeArgs)
    print(nodeArgs["1"])
    dd = DistributionRatio(seat = 21, a = 103, b = 63, c = 34, d = 35)
    perSeat = dd.distribution()
    print("最终分配结果为:%s" % str(perSeat))
