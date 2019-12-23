#!/usr/bin/env python
# -- coding: utf-8 --#

from gevent import monkey;monkey.patch_all() #有io时需要此句去执行切换，否则会是顺序执行
import gevent
from urllib import request

def f(n):
    for i in range(n - 5, n):
        print(gevent.getcurrent(), i)
        gevent.sleep(1)

def getHttp(url):
    print('GET from url : {0}'.format(url))
    resp = request.urlopen(url)
    data = resp.read().decode()
    print('{0} date form {1}'.format(len(data), url))

if __name__ == '__main__':
    # g1 = gevent.spawn(f, 10)
    # g2 = gevent.spawn(f, 20)
    # g3 = gevent.spawn(f, 30)
    #
    # g1.join()
    # g2.join()
    # g3.join()

    gevent.joinall([gevent.spawn(getHttp, 'https://www.baidu.com'),gevent.spawn(getHttp, 'https://www.python.org/'),gevent.spawn(getHttp, 'https://github.com/')])