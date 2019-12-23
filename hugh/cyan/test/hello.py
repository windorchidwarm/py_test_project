#encoding:utf-8

import time
import math
import datetime
import random
import functools

def sortNum():
    list = [1, 19, 2, 23]
    list.sort()
    print(list)

def fib(num):
    if(num == 1) or (num == 2):
        print(1)
    else :
        x, y = 1, 1
        z = 0
        for i in range(2, num):
            z = x + y
            x = y
            y = z
            print(z)
        else:
            print(z)

def multTabe():
    for i in range(1, 10):
        for j in range(1, i + 1):
            print("%d*%d=%d " % (j, i, i*j), end='')
        print()

def suspendTime():
    print(time.time())
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    time.sleep(1)
    print(time.time())
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

def primeNum(x, y):
    h, leap = 0, 1
    for i in range(x, y + 1):
        k = int(math.sqrt(i))
        for j in range(2, k + 1):
            if i % j == 0:
                leap = 0
                break
        if leap == 1:
            print(i)
            h += 1
        leap = 1
    print(h)

def narcissuNum():
    for m in range(100, 1000):
        i = int(m / 100)
        j = int(m / 10) % 10
        k = m % 10
        if m == i ** 3 + j ** 3 + k ** 3:
            print(m)

def reduceNum(num):
    print("%d = " % num, end='')
    while num not in [1]:
        for index in range(2, num + 1):
            if num % index == 0:
                num = int(num/index)
                if num == 1:
                    print(index)
                else:
                    print("{} * ".format(index), end='')
                break

def datetimeTest():
    print(datetime.date.today().strftime("%Y/%m/%d"))
    mydate = datetime.date(1945, 1, 3)
    print(mydate.strftime("%Y/%m/%d"))
    mydate = mydate + datetime.timedelta(days=4)
    print(mydate)
    mydate = mydate.replace(year=mydate.year + 1)
    print(mydate.strftime("%Y/%m/%d"))
    print(mydate.timetuple())
    tdate = datetime.datetime(1944, 2, 4, 13, 24, 40)
    print(tdate.timetuple())
    tdate = tdate.replace(second=tdate.second + 1, minute=tdate.minute+3)
    print(tdate.strftime("%Y-%m-%d %H:%M:%S"))

def calLetters(str):
    letters, space, digits, others = 0, 0, 0, 0
    i = 0
    while i < len(str):
        c = str[i]
        i += 1
        if c.isalpha():
            letters += 1
        elif c.isspace():
            space += 1
        elif c.isdigit():
            digits += 1
        else:
            others += 1
    print("%d %d %d %d" % (letters, space, digits, others))

def perfectNum():
    for num in range(1, 1001):
        sum = 0
        for i in range(1, num):
            if num % i == 0:
                sum += i
        if sum == num:
            print(num)

def testCalFloat():
    a = 1.0
    b = 2.0
    list = []
    for i in range(1, 21):
        list.append(b/a)
        a, b = b, a + b
    print(functools.reduce(lambda x,y:x + y, list))

def serisCal():
    # n = 1
    # sum = 0
    # for i in range(1, 21):
    #     n *= i
    #     print(n)
    #     sum += n
    # print(sum)
    ss = 0
    l = range(1, 21)
    def myopt(x):
        r = 1
        for i in range(1, x + 1):
            r *= i
        print(r)
        return r
    ss = sum(map(myopt, l))
    print(ss)

def printRevers(list):
    list.insert(2, 19)
    list.sort()
    for a in list[::-1]:
        print(a)
    print(",".join(str(n) for n in list))
    print(random.choice(['1', 'xx', 'yy']))

# sortNum()
# fib(9)
# multTabe()
# suspendTime()
# primeNum(1, 200)
# narcissuNum()
# reduceNum(6)
# reduceNum(60)
# reduceNum(8)
# reduceNum(99)
# datetimeTest()
# calLetters("muy 192 %k__4387438")
# perfectNum()
# testCalFloat()
# serisCal()
# printRevers([1, 3, 5, 2])

class bcolors:
    WARNING = '\033[93m'
    ENDC = '\033[0m'

def varfunc():
    var = 0
    print("%d" % var)
    var += 1

class Static:
    staticVar = 5
    def varfunc(self):
        self.staticVar += 1
        print(self.staticVar)


# if __name__ == '__main__':
    # a = 0o77
    # print(a & 3)
    # print(a & 4)
    # print(random.uniform(10, 20))
    # print(random.randint(10, 20))
    # print(random.choice(['1', 'xx', 'yy']))
    # print(random.sample(['mm', 'sm', 'dt'], 2))
    # list = [1, 4, 5, 9, 20]
    # random.shuffle(list)
    # print(list)
    # for i in range(3):
    #     varfunc()
    # print(Static.staticVar)
    # a = Static()
    # staticVar = 3
    # for i in range(3):
    #     staticVar += 5
    #     print(staticVar)
    #     a.varfunc()
    # printRevers([1, 3, 5, 2])
    # print(bcolors.WARNING + "警告字体的颜色？" + bcolors.ENDC + "明后")