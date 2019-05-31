#!/usr/bin/env python
# encoding: utf-8
'''
@author: heshengjin-何胜金
@contact: 2356899074@qq.com
@software: pycharm
@file: threadingTestLock.py
@time: 2018/12/20 13:36
@desc:并发编程-多线程
+=（原子操作）
'''

import threading

deposit = 0 # 银行存款-主线程中-子线程共享主线程
lock_deposit = threading.Lock()


def change_it(n):
    # 使用外层的变量，自己不去定义变量
    global deposit
    deposit += n  # 存
    deposit -= n  # 取
    # deposit = deposit + n  # 存
    # deposit = deposit - n  # 取


def loop(n):
    for i in range(100000):
        lock_deposit.acquire()  # 先获取锁
        try:
            change_it(n)
        finally:
            lock_deposit.release()  # 确保释放锁

t1 = threading.Thread(target=loop, args=(5,))
t2 = threading.Thread(target=loop, args=(8,))
t1.start()
t2.start()

t1.join()
t2.join()
print(deposit)