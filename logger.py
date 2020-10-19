#!/usr/bin/env python
# -*- coding: gb18030 -*-
########################################################################
# 
# Copyright (c) 2019 Baidu.com, Inc. All Rights Reserved
# 
########################################################################

"""
File: logger.py
Author: zhanghao55(zhanghao55@baidu.com)
Date: 2019/09/19 20:49:02
"""

import os
import logging
import logging.handlers

def init_log(
        log_path=None,
        stream_level=logging.DEBUG,
        file_level=logging.DEBUG,
        when="D",
        backup=7,
        format="[%(asctime)s][%(filename)s:%(funcName)s:%(lineno)s][%(levelname)s]:%(message)s",
        datefmt=None):
    """
    init_log - initialize log module
    Args:
      log_path      - Log file path prefix.
                      Log data will go to two files: log_path.log and log_path.log.wf
                      Any non-exist parent directories will be created automatically
      level         - msg above the level will be displayed
                      DEBUG < INFO < WARNING < ERROR < CRITICAL
                      the default value is logging.INFO
      when          - how to split the log file by time interval
                      'S' : Seconds
                      'M' : Minutes
                      'H' : Hours
                      'D' : Days
                      'W' : Week day
                      default value: 'D'
      format        - format of the log
                      default format:
                      %(levelname)s: %(asctime)s: %(filename)s:%(lineno)d * %(thread)d %(message)s
                      INFO: 12-09 18:02:42: log.py:40 * 139814749787872 HELLO WORLD
      backup        - how many backup file to keep
                      default value: 7
    Raises:
        OSError: fail to create log directories
        IOError: fail to open log file
    """
    formatter = logging.Formatter(format, datefmt)
    logger = logging.getLogger()
    logger.handlers = []
    logger.setLevel(file_level)

    # console Handler
    consoleHandler = logging.StreamHandler()
    consoleHandler.setLevel(stream_level)
    consoleHandler.setFormatter(formatter)
    logger.addHandler(consoleHandler)

    if log_path is None:
        return
    dir = os.path.dirname(log_path)
    if not os.path.isdir(dir):
        os.makedirs(dir)

    handler = logging.handlers.TimedRotatingFileHandler(
        log_path + ".log", when=when, backupCount=backup)
    handler.setLevel(file_level)
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    handler = logging.handlers.TimedRotatingFileHandler(
        log_path + ".log.wf", when=when, backupCount=backup)
    handler.setLevel(logging.WARNING)
    handler.setFormatter(formatter)
    logger.addHandler(handler)


def set_level(level):
    """
    Reak-time set log level
    """
    logger = logging.getLogger()
    logger.setLevel(level)
    logging.info('log level is set to : %d' % level)


def get_level():
    """
    get Real-time log level
    """
    logger = logging.getLogger()
    return logger.level


if __name__ == "__main__":
    pass
