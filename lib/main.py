# -*- coding: utf-8 -*-
__author__ = 'CQC'

from login import login, reLogin
from select import loop, thread
from tool import getCurrentTime as time
import config

def main():
    print time(), u'欢迎使用山东大学刷课系统，您要刷课的课程号为', config.KCH, u'课序号为', config.KXH
    login_result = login()
    login_result or reLogin() or exit()
    thread()
    #loop()
