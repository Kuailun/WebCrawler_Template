# -*- coding: utf-8 -*-
# @File       : job.py
# @Author     : Yuchen Chai
# @Date       : 2020/1/25 15:12
# @Description: 网络爬虫任务

import datetime
import time
from Service.logger import logger

def JOB():
    '''
    定义爬虫需要爬取的任务
    :return:
    '''
    logger.info(r"开始运行任务")
    start_time = time.time()



    end_time = time.time()
    logger.info(r"本次程序运行耗时：{0}秒".format(end_time - start_time))
    # raise(r"JOB函数未改写")