# -*- coding: utf-8 -*-
from requests import RequestException

__author__ = 'CQC'

import config
from pyquery import PyQuery as pq
from tool import getCurrentTime as time
login_data = {
    'stuid': config.USERNAME,
    'pwd': config.PASSWORD,
}

def login():
    try:
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
    except RequestException:
        print time(), u'登录网页请求失败'
        return False


def reLogin(fail_time=0):
    login_result = login()
    if fail_time >= config.MAX_LOGIN_TIME:
        print time(), u'登录重试次数过多，请检查网络状态'
        return False
    if not login_result:
        print time(), u'登录失败，正在重试...'
        fail_time += 1
        return reLogin(fail_time)
    else:
        print time(), u'登录成功，继续刷课...'
    return login_result


