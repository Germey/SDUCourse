# -*- coding: utf-8 -*-
__author__ = 'CQC'

import requests

MAX_LOGIN_TIME = 3

SELECTED_FLAG = [
    u'曾经学习过',
    u'已经选'
]

SESSION = requests.session()

SELECTED = False

BASE_URL = 'http://jwxt.sdu.edu.cn:7890'

LOGIN_URL = BASE_URL + '/pls/wwwbks/bks_login2.login'

SELECT_URL = BASE_URL + '/pls/wwwbks/xk.CourseInput'

##
# --------------------------------------------------------------------------
# 用户配置项
# --------------------------------------------------------------------------
# USERNAME: 学号
#
##

USERNAME = '201200131012'

PASSWORD = '940629cqc'

KCH = 'sd01330810'

KXH = '100'

THREAD_NUMBER = 3