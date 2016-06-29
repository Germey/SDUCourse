# -*- coding: utf-8 -*-

__author__ = 'CQC'

import config
from pyquery import PyQuery as pq
from tool import getCurrentTime as time
login_data = {
    'stuid': config.USERNAME,
    'pwd': config.PASSWORD,
}

def login():
    print time(), u'正在尝试登录选课系统，请稍候...'
    res = config.SESSION.post(config.LOGIN_URL, login_data)

    status = res.status_code

    if status == 200:
        html = res.text
        doc = pq(html)
        login_status = doc('span.t').text()
        if not login_status:
            print time(), doc.text()
            return False
        else:
            print time(), login_status
            return True
    else:
        print time(), u'登录失败，请稍后重试'
        return False
