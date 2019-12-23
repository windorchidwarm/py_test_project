#encoding:utf-8
from hugh.cyan.test import testsoso
from hugh.cyan.utest.utest import Utest, defaultUtest
from hugh.cyan.config.conf import config
import os
import subprocess
import json
import importlib
from hugh.config.settings import *
# from hugh.cyan.math.mtest import *
import hugh.cyan.test.testsoso

COMPONENT_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.join("hugh",os.path.join("cyan", "math")))
#.replace(os.path.join("bz","schedule"),''),"component")

if __name__ == '__main__':
    # my = Utest("helloworkd")
    # my.sayHello()
    # defaultUtest.sayHello()
    # print(config.getConf("app", "app_name"))
    # print(config.getConf("test", "test1"))
    # testStr = '''you are a test {mynina} test'''.format(mynina = "mds")
    # testStr1 = '''dlsdk {0} dslsd {1}'''.format("#$$", "own")
    # print(testStr)
    # print(testStr1)
    nodes = {"1":{"nid":"1","eid":"2","type":"11","isEnd":"0"},"2":{"type":"11","isEnd":"0"},"3":{"type":"21","isEnd":"1"}}
    retDict = {}
    retDict['test'] = json.dumps(nodes, separators=(',',':'))
    print(retDict)
    # componentArgs = retDict.get('test', '').replace("\"", "*")
    # print(COMPONENT_PATH)
    # print(componentArgs)
    # cmd = '''python {filename} -nd={component_args} '''.format(filename=os.path.join(COMPONENT_PATH, "distributionratio.py"),
    #                                                                  component_args=componentArgs)
    # print(cmd)
    # p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    # errorInfo = []
    # while p.poll() is None:
    #     line = p.stdout.readline()
    #     line = line.strip()
    #     if p.stderr is not None:
    #         errorInfo.append(p.stderr.readline())
    #     if line:
    #         print('localSubmitCmd output: [{0}]'.format(line))
    # if p.returncode == 0:
    #     print(p.returncode)
    # else:
    #     print("\n".join(errorInfo))

    COMPONENT_PATH_NOW = os.path.join(os.path.dirname(os.path.realpath(__file__)),os.path.join("hugh", os.path.join("cyan", "math")))
    COMPONENT_PATH_NOW = os.path.join(COMPONENT_PATH_NOW, 'mtest.py')

    print(MODE)
    # print(stest(nodes))


    # m = importlib.import_module('hugh.cyan.math.mtest', COMPONENT_PATH_NOW)
    # print(m)
    # cls = getattr(m, 'dtest')
    # cls().executeNodes(nodes)
    # tt = __import__("hugh.cyan.math.mtest", fromlist = True)
    # print(tt)
    # cls = getattr(tt, 'dtest')  # 通过getattr()获取模块内容，获取类名
    # cls().executeNodes(nodes)
    testsoso.test()

