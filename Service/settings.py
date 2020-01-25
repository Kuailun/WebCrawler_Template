# -*- coding: utf-8 -*-
# @File       : settings.py
# @Author     : Yuchen Chai
# @Date       : 2020/1/25 14:46
# @Description: 用于设置服务中的各项参数

"""运行的相关设置"""
# -----------------------------------------------------------------------------
# 定时器设置参数
# -----------------------------------------------------------------------------
SCHEDULER_TYPES = {"Interval":"interval"}
SCHEDULER_MODE = SCHEDULER_TYPES["Interval"]
SCHEDULER_INTERVAL = 43200


"""模板的相关设置"""
# -----------------------------------------------------------------------------
# 数据库模板设置参数
# -----------------------------------------------------------------------------
DATABASE_TYPES = {"TXT":"txt","MongoDb":"mongodb","Excel":"xls"}

# -----------------------------------------------------------------------------
# 日志记录的设置
# -----------------------------------------------------------------------------
# 是否输出到控制台
LOGGING_CONSOLE_FLAG = True

# 是否输出到文件
LOGGING_FILE_LOG = True

# 输出日志的等级
LOGGING_LEVEL = ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']
LOGGING_CURRENT_LEVEL = LOGGING_LEVEL[0]