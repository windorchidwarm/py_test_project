#encoding:utf-8

__all__ = ['Utest']

class Utest:
    def __init__(self, myword):
        self.myword = myword

    def sayHello(self):
        print(self.myword)

defaultUtest = Utest("myonwn")