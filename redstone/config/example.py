#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    redstone.config.dev
    ~~~~~~~~~~~~~~~~~~~

    DEV配置

    :author:    lightless <root@lightless.me>
    :homepage:  None
    :license:   GPL-3.0, see LICENSE for more details.
    :copyright: Copyright (c) 2017 lightless. All rights reserved
"""

DEBUG = True
SECRET_KEY = '0q289aidfa23-098rawd#vajeifj'

# LOG配置
LOG_TO_FILE = True
LOG_FILENAME = "redstone.log"
LOG_PATH = "logs"

ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost"
]

EXTRA_INSTALLED_APPS = [

]

EXTRA_MIDDLEWARE = [

]

# MySQL连接配置
DATABASE_NAME = "redstone"
DATABASE_USER = "redstone"
DATABASE_PASSWORD = "123!@#"
DATABASE_HOST = "127.0.0.1"
DATABASE_PORT = "5432"
# DATABASE_OPTIONS = {
#     'init_command': 'SET default_storage_engine=INNODB;SET NAMES utf8mb4',
#     'charset': 'utf8mb4',
# }

# ActiveMQ连接配置
ACTIVEMQ_HOST = "127.0.0.1"
ACTIVEMQ_PORT = "61613"
ACTIVEMQ_USERNAME = "redstone"
ACTIVEMQ_PASSWORD = "123456"

# ActiveMQ队列信息
ACTIVEMQ_QUEUES = {
    "SPIDER_TASK": "redstone.task.spider_task",
    "SPIDER_RESULT": "redstone.result.spider_result",
}
