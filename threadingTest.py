#!/usr/bin/env python
# encoding: utf-8
'''
@author: heshengjin-何胜金
@contact: 2356899074@qq.com
@software: pycharm
@file: threadingTest.py
@time: 2018/12/20 12:08
@desc:多线程编程-开启线程的两种方式-和java一样继承和runable方式
'''
import threading
import time

# <type 'int'>
# <type 'tuple'>
a = (6)
b = (6,)
print( type(a))
print( type(b))


# ==============================方式1：runable方式===============================
def loop(x):
    print("******%s start******" % threading.current_thread().name)
    for i in range(x):
        time.sleep(1)
        print("%s:%d" % (threading.current_thread().name, i))
    print("******%s stop******" % threading.current_thread().name)


print("----%s start----" % threading.current_thread().name)
# threading.Thread参数是tuple，只要一个len()==1
t1 = threading.Thread(target=loop, args=(6,))
# t1.setDaemon(True) 主线程结束就结束所有
t1.setDaemon(True)
t1.start()
# t1.join()所有子线程结束才结束主线程
t1.join()
print("----%s stop-----" % threading.current_thread().name)




