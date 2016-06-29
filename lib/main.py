# -*- coding: utf-8 -*-
import signal

__author__ = 'CQC'

from login import login, reLogin
from select import loop, thread
from tool import getCurrentTime as time
import config
import sys

def quit(signum, frame):
    print u'程序中止'
    sys.exit()


def main():
    signal.signal(signal.SIGINT, quit)
    signal.signal(signal.SIGTERM, quit)
    print time(), u'欢迎使用山东大学刷课系统'
    login_result = login()
    login_result or reLogin() or exit()
    thread()
    print time(), u'程序执行完毕, 感谢您使用山东大学刷课系统'

