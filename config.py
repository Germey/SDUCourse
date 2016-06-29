# -*- coding: utf-8 -*-
__author__ = 'CQC'

import requests
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
#
# --------------------------------------------------------------------------
# 开发配置项
# --------------------------------------------------------------------------
# SELECTED_FLAG: 选中课程判断标志
# SESSION: 会话
# BASE_URL: 选课链接
# LOGIN_URL: 登录链接
# SELECT_URL: 刷课链接
# SELECTED: 是否选中标志
# NEED_LOGIN_FLAG: 需要登录判断标志
# --------------------------------------------------------------------------
#

SELECTED_FLAG = [
    u'曾经学习过',
    u'已经选'
]

NEED_LOGIN_FLAG = [
    u'请先登录再使用'
]

SESSION = requests.session()

SELECTED = False

BASE_URL = 'http://jwxt.sdu.edu.cn:7890'

LOGIN_URL = BASE_URL + '/pls/wwwbks/bks_login2.login'

SELECT_URL = BASE_URL + '/pls/wwwbks/xk.CourseInput'

SELECT_COUNT = 1

#
# --------------------------------------------------------------------------
# 用户配置项
# --------------------------------------------------------------------------
# USERNAME: 学号
# PASSWORD: 选课密码
# KCH: 课程号
# KXH: 课序号
# THREAD_NUMBER: 刷课线程数
# MAX_LOGIN_TIME: 登录失败重试次数
# TIMEOUT: 连接超时时间，单位秒
# SELECT_COUNT: 选课尝试次数
# --------------------------------------------------------------------------
#

USERNAME = '201300130043'

PASSWORD = '950830'

COURSE = [
    {
        'KCH': '0133303210',
        'KXH': '100',
    },
    # {
    #     'KCH': 'sd01331370',
    #     'KXH': '100',
    # }
]

THREAD_NUMBER = 3

MAX_LOGIN_TIME = 3

TIMEOUT = 30
