#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : logic_gate.py
# Author: BBD
# Date  : 2020/6/4


class LogicGate:

    def __init__(self, n):
        self.label = n
        self.output = None

    def __str__(self):
        pass

    def getLable(self):
        return self.label

    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output

class BinaryGate(LogicGate):

    def __init__(self, n):
        super().__init__(n)
        self.pinA = None
        self.pinB = None

    def getPinA(self):
        return int(input('pin a is '))

    def getPinB(self):
        return int(input('pin b is '))

class UnaryGate(LogicGate):

    def __init__(self, n):
        super().__init__(n)
        self.pin = None

    def getPin(self):
        return int(input('pin is '))

class AndGate(BinaryGate):
    def __init__(self, n):
        super().__init__(n)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a == 1 and b == 1:
            return 1
        else:
            return 0
class OrGate(BinaryGate):
    def __init__(self, n):
        super().__init__(n)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a == 0 and b == 0:
            return 0
        else:
            return 1

class NotGate(UnaryGate):
    def __init__(self, n):
        super().__init__(n)

    def performGateLogic(self):
        a = self.getPin()
        if a == 1:
            return 0
        else:
            return 1
if __name__ == '__main__':
    '''
    '''
    g3 = NotGate('g3')
    g3.getOutput()