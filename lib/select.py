# -*- coding:utf-8 -*-

__author__ = 'CQC'
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
    print time(), u'正在尝试选此门课程，请稍候...'
    res = config.SESSION.post(config.SELECT_URL, course_data)
    html = res.text
    doc = pq(html)
    result = doc('span.t').text()
    print time(), result
    if selected(result):
        config.SELECTED = True
        print time(), u'恭喜你已经选中该门课程'


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
        t.start()

    for t in threads:
        t.join()

    print time(), u'程序执行完毕'
