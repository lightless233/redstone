#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    redstone.core.engines.base
    ~~~~~~~~~~~~~~~~~~~~~~~~~~

    基础引擎，所有engine的父类，提供固定的接口

    :author:    lightless <root@lightless.me>
    :homepage:  None
    :license:   GPL-3.0, see LICENSE for more details.
    :copyright: Copyright (c) 2017 lightless. All rights reserved
"""

# todo: 各种引擎抽出来共同的基础类

import abc
import multiprocessing
import queue
import threading
from typing import Union, List

try:
    from dataclasses import dataclass

    @dataclass(frozen=True)
    class EngineStatus:
        READY = 0x00
        RUNNING = 0x01
        STOP = 0x02
except ImportError:
    class EngineStatus:
        READY = 0x00
        RUNNING = 0x01
        STOP = 0x02


class STBaseEngine(object, metaclass=abc.ABCMeta):
    """
    单线程的基础类
    """

    def __init__(self, in_queue, out_queue):
        """
        :param in_queue: 输入队列
        :param out_queue: 输出队列
        """
        super(STBaseEngine, self).__init__()

        # 引擎的名称
        self.name = "SingleThreadEngine"

        # 工作线程
        self.thread: threading.Thread = None

        # 引擎状态
        self._status = EngineStatus.READY

        # 工作标志
        self._ev: threading.Event = threading.Event()

        # 输入、输出队列
        self._in_queue: Union[queue.Queue, queue.PriorityQueue] = None
        self._out_queue: Union[queue.Queue, queue.PriorityQueue] = None

    def start(self):
        self._status = EngineStatus.RUNNING
        self.thread = threading.Thread(target=self._worker, name=self.name)
        self.thread.start()

    def stop(self, force=True):
        def _stop():
            self._status = EngineStatus.STOP
            self._ev.set()
        if force:
            _stop()
        else:
            while True:
                if self._in_queue.empty():
                    _stop()
                else:
                    self._ev.wait(1)

    def is_alive(self):
        return self.thread.is_alive()

    def get_task_from_queue(self, timeout=1):
        """
        从输入队列中获取任务
        :param timeout: 超时时间，默认为1s
        :return: task
        """
        return self._in_queue.get(block=False)

    def put_result_to_queue(self, result):
        """
        向输出队列中放置结果
        :param result: 需要放到队列中的结果
        :return:
        """
        self._out_queue.put(result, block=False)

    @abc.abstractmethod
    def _worker(self):
        pass


class MTBaseEngine(object, metaclass=abc.ABCMeta):
    def __init__(self, in_queue, out_queue, pool_size=None):
        """
        多线程引擎的基类
        :param in_queue: 输入队列
        :param out_queue: 输出队列
        """
        super(MTBaseEngine, self).__init__()

        # 引擎名称
        self.name = "MultiThreadEngine"

        # 线程池
        self.thread_pool: List[threading.Thread] = []

        # 线程池大小
        self.pool_size = pool_size if pool_size else multiprocessing.cpu_count() * 2 + 1

        # 引擎状态
        self._status = EngineStatus.READY

        # 工作标志
        self._ev = threading.Event = threading.Event()

        # 输入输出队列
        self._in_queue: Union[queue.Queue, queue.PriorityQueue] = in_queue
        self._out_queue: Union[queue.Queue, queue.PriorityQueue] = out_queue

    def start(self):
        self._status = EngineStatus.RUNNING
        self.thread_pool = [
            threading.Thread(target=self._worker, name="{}-{}".format(self.name, idx)) for idx in range(self.pool_size)
        ]
        _ = [_thread.start() for _thread in self.thread_pool]

    def stop(self, force=True):
        def _stop():
            self._status = EngineStatus.STOP
            self._ev.set()

        if force:
            _stop()
        else:
            while True:
                if self._in_queue.empty():
                    _stop()
                else:
                    self._ev.wait(1)

    def is_alive(self):
        return any([x.is_alive() for x in self.thread_pool])

    def get_task_from_queue(self):
        return self._in_queue.get(block=False)

    def put_result_to_queue(self, result):
        self._out_queue.put(result)

    @abc.abstractmethod
    def _worker(self):
        pass
