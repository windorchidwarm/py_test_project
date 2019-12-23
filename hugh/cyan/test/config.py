#!/usr/bin/env python
# -- coding: utf-8 --#

import os
import configparser

class ConfigUtils(object):
    def __init__(self, fileName):
        super(ConfigUtils, self).__init__()
        try:
            self.path = os.path.dirname(os.path.realpath(__file__)).replace('common', '')
            self.config = configparser.ConfigParser()
            self.config.read(self.path + "/fdfs_client.cfg")
            # active = self.config.get("profiles", "active")
            # cfgFiles = [self.path + "/application.cfg",
            #             self.path + "/application_" + active + ".cfg"]
            # self.config.read(cfgFiles)
        except IOError as e:
            print(e)

    def getConf(self, section, option, defult=None):
        value = self.config.get(section, option)
        if (value is None or value.strip() == ''):
            return defult
        return value

    def getConfSection(self, section):
        items = self.config.items(section)
        value = {}
        for item in items:
            value[item[0]] = item[1]
        return value

    def getLogConfig(self):
        return self.path + "/log.json"


config = ConfigUtils("")