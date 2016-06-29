import time

__author__ = 'CQC'



def getCurrentTime():
    return time.strftime('[%Y-%m-%d %H:%M:%S]',time.localtime(time.time()))