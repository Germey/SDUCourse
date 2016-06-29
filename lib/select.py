# -*- coding:utf-8 -*-
__author__ = 'CQC'

from lxml.etree import XMLSyntaxError
from requests import RequestException
from lib.login import reLogin
import threading
import config
from time import sleep
from tool import getCurrentTime as time
from pyquery import PyQuery as pq

course_data = {
    'p_qxrxk': config.KCH,
    'p_qxrxk_kxh': config.KXH
}

config.SELECTED = False


def selected(result):
    for flag in config.SELECTED_FLAG:
        if flag in result:
            return True
    return False


def select():
    print time(), u'正在尝试选此门课程，第', config.SELECT_COUNT, u'次尝试，请稍候...'
    config.SELECT_COUNT += 1
    try:
        res = config.SESSION.post(config.SELECT_URL, course_data, timeout=config.TIMEOUT)
        html = res.text
        if not html.strip():
            print time(), u'用户登录会话无效，正在重新登录...'
            reLogin() or exit()
        doc = pq(html)
        result = doc('span.t').text()
        print time(), result
        if selected(result):
            config.SELECTED = True
            print time(), u'恭喜你已经选中该门课程'
    except RequestException:
        print time(), u'网页请求失败，继续重试'
    except XMLSyntaxError:
        print time(), u'继续刷课...'


def loop():
    sleep(1)
    while not config.SELECTED:
        select()


def thread():
    threads = []
    for i in range(config.THREAD_NUMBER):
        threads.append(threading.Thread(target=loop))

    for i, t in enumerate(threads):
        t.setDaemon(True)
        print time(), u'正在启动第', i + 1, u'个线程'
        sleep(i)
        t.start()

    for t in threads:
        t.join()
