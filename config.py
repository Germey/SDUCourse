# -*- coding: utf-8 -*-
__author__ = 'CQC'

import requests

USERNAME = '201200131012'

PASSWORD = '940629cqc'

BASE_URL = 'http://jwxt.sdu.edu.cn:7890'

LOGIN_URL = BASE_URL + '/pls/wwwbks/bks_login2.login'

SELECT_URL = BASE_URL + '/pls/wwwbks/xk.CourseInput'

KCH = 'sd01330810'

KXH = '100'

SESSION = requests.session()

SELECTED = False

SELECTED_FLAG = [
    u'曾经学习过',
    u'已经选'
]

THREAD_NUMBER = 3