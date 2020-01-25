# -*- coding: utf-8 -*-
# @File       : run.py
# @Author     : Yuchen Chai
# @Date       : 2020/1/25 14:43
# @Description: 用于启动服务

import datetime
from Service.logger import logger
from Service.job import JOB
from Service import settings as ss
from apscheduler.schedulers.background import BackgroundScheduler

logger.info(r"服务开始启动")

# 设置定时器
scheduler = BackgroundScheduler()
scheduler.add_job(JOB, ss.SCHEDULER_MODE, seconds = ss.SCHEDULER_INTERVAL)
logger.info(r"定时器设置完毕，运行间隔：{0}小时".format(ss.SCHEDULER_INTERVAL/3600))

# 首次运行任务
JOB()

scheduler.start()

try:
    while(True):
        pass
except(KeyboardInterrupt, SystemExit):
    scheduler.shutdown()