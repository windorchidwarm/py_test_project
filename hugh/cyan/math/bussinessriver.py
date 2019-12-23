#!/usr/bin/env python
# -- coding: utf-8 --#

import random
import copy

class BussinessRiver:

    def __init__(self,merchants, servants, capacity):
        '''
        :param merchants: 商人数
        :param servants: 随从数
        :param capacity: 渡船容量
        '''
        self.merchants = merchants
        self.servants = servants
        self.capacity = capacity

    def allowSet(self):
        '''
        允许状态集合
        :return:
        '''
        allowset = []

        for i in range(self.merchants + 1):
            for j in range(self.servants + 1):
                if i == 0:
                    allowset.append([i, j])
                elif i == self.merchants:
                    allowset.append([i, j])
                elif i >= j and (self.merchants - i) >= (self.servants - j):
                    allowset.append([i, j])
        return  allowset

    def allowAction(self):
        '''
        允许行动模型
        :return:
        '''
        allowaction = []
        for i in range(self.capacity + 1):
            for j in range(self.capacity + 1):
                if (i + j) <= self.capacity and (i + j) != 0:
                    allowaction.append([i, j])
        return  allowaction

    def solve(self, allowactionset, allowstate):
        '''
        随机的方式去寻找正确的路径，经常会出现往返的情况
        :param allowactionset:
        :param allowstate:
        :return:
        '''
        count = 1;
        current = (self.merchants, self.servants)
        while current != [0, 0]:
            move = allowactionset[random.randint(0, len(allowactionset) - 1)]
            temp = [current[0] + ((-1) ** count) * move[0], current[1] + ((-1) ** count) * move[1]]
            if(temp in allowstate):
                current = [current[0] + ((-1) ** count) * move[0], current[1] + ((-1) ** count) * move[1]]
                if(count % 2 == 1):
                    print("[%d]个商人，[%d]个随从从此岸到彼岸" % (move[0], move[1]))
                elif(count % 2 == 0):
                    print("[%d]个商人，[%d]个随从从彼岸回到此岸" % (move[0], move[1]))

                count += 1

    def solve2(self, allowactionset, allowsate):
        '''
        循环试探每一步的进行路径，如果可以通过则继续作为分支开启下一次循环
        可优化地方，对重复或者循环没有很好的判断，如果数据量比较大则运算会比较复杂，也可能失败
        :param allowactionset:
        :param allowsate:
        :return:
        '''
        currentWill = {}
        currentNow = {}
        strKey = "_".join([str(self.merchants), str(self.servants), str(1)])
        currentNow[strKey] = [[self.merchants, self.servants]]
        step = 1
        print(currentNow)
        last = []
        while True:
            for i in range(len(allowactionset)):
                move = allowactionset[i]
                for strKey in currentNow.keys():
                    count = int(strKey.split("_")[2])
                    currentPre = currentNow[strKey]
                    cNow = len(currentPre)
                    current = currentPre[cNow - 1]
                    temp = [current[0] + ((-1) ** count) * move[0], current[1] + ((-1) ** count) * move[1]]
                    if(temp in allowsate):
                        # currentNowAft = currentPre[:] #还可以如下方式切片
                        # currentNowAft = list(currentPre)
                        # currentNowAft = copy.copy(currentPre)
                        currentNowAft = copy.deepcopy(currentPre) #如果列表中含义列表，则上述几个子列表指向的是同一个列表，仅此方式会复制新的子列表
                        currentNowAft.append(temp)
                        if (count % 2 == 1):
                            print("[%d]个商人，[%d]个随从从此岸到彼岸，列表为%s" % (move[0], move[1], str(currentNowAft)))
                        elif (count % 2 == 0):
                            print("[%d]个商人，[%d]个随从从彼岸回到此岸，列表为%s" % (move[0], move[1],  str(currentNowAft)))
                        count += 1
                        strKey = "_".join([str(temp[0]), str(temp[1]), str(count)])
                        if temp != [3,3]:
                            currentWill[strKey] = currentNowAft

                        if temp == [0, 0]:
                            last = temp
                            print("当前的路线为[%s]" % currentNowAft)
                            break

            currentNow.clear()
            print(currentWill)
            print(currentWill.keys())
            currentNow = currentWill
            currentWill = {}
            if last == [0, 0]:
                break
            if step % 30 == 0:
                break
            else:
                step += 1


def main():
    boat = BussinessRiver(3, 3, 2)
    allowset = boat.allowSet()
    allowaction = boat.allowAction()

    print(allowset)
    print(allowaction)

    # boat.solve(allowaction, allowset)
    boat.solve2(allowaction, allowset)


if __name__ == '__main__':
    main()