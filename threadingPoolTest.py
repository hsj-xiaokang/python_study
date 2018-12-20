#!/usr/bin/env python
# encoding: utf-8
'''
@author: heshengjin-何胜金
@contact: 2356899074@qq.com
@software: pycharm
@file: threadingPoolTest.py
@time: 2018/12/20 15:08
@desc:线程池
'''
import time
import threadpool


def sayhello(str):
    print "",str
    time.sleep(2)

name_list =['xiaozi','aa','bb','cc']

start_time = time.time()

pool = threadpool.ThreadPool(10)
requests = threadpool.makeRequests(sayhello, name_list)
[pool.putRequest(req) for req in requests]
pool.wait()

print '%d second'% (time.time()-start_time)