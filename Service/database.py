# -*- coding: utf-8 -*-
# @File       : database.py
# @Author     : Yuchen Chai
# @Date       : 2020/1/25 14:45
# @Description: 数据库类，

from Service import settings as ss
import os
from Service.logger import logger

class database:
    '''
    数据库类的基类，用于连接不同的数据库(Mongodb, txt, excel等等)
    '''

    def __init__(self, p_path, p_name, p_type):
        '''
        初始化数据基类
        :param p_path: 数据库保存路径
        :param p_name: 数据库名称
        :param p_type: 数据库类型（Mongodb, txt, excel等）
        '''

        self._name = p_name
        self._type = p_type
        self._database_path = p_path + p_name + "." + p_type
        self._database_available = True

        logger.debug("数据库选用模式为{0}".format(p_type))

        # 如果是Mongdo的形式，无需检查路径
        if p_type == ss.DATABASE_TYPES["Mongodb"]:
            self._path_check = False
        pass

    def _Database_Path_Existing(self):
        '''
        检查数据库文件是否存在
        :return:
        '''

        # 如果无需检查，则返回
        if not self._path_check:
            return

        # 检查数据库的路径是否存在
        if not os.path.exists(self._database_path):
            logger.info(r"{0} 不存在，开始创建".format(self._name))
            self._Database_CreateFile()
            pass
        else:
            pass
        pass

    def _Database_CreateFile(self):
        '''
        创建数据库
        :return:
        '''
        raise("_Database_CreateFile函数未初始化")