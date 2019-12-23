#encoding:utf-8

import os
import configparser

class ConfigUtils(object):
    def __init__(self, fileName):
        try:
            self.path = os.path.dirname(os.path.realpath(__file__)).replace("cyan", "")
            self.config = configparser.ConfigParser()
            self.config.read(self.path + "/application.cfg")
            active = self.config.get("profiles", "active")
            cfgFiles = [self.path + "/application.cfg",
                self.path + "/application-" + active + ".cfg"]
            self.config.read(cfgFiles)
        except IOError as e:
            print(e)

    def getConf(self, section, option, default = None):
        value = self.config.get(section, option)
        if(value is None or value.strip() == ''):
            value = default
        return value

config = ConfigUtils("")