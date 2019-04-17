#!/usr/bin/env python
# encoding: utf-8
'''
@author: heshengjin-何胜金
@contact: 2356899074@qq.com
@software: pycharm
@file: threadingTest.py
@time: 2018/12/20 12:08
@desc:多线程编程-开启线程的两种方式-和java有点类似继承和runable方式
'''
import threading
from threading import Thread
import time

# <type 'int'>
# <type 'tuple'>
a = (6)
b = (6,5,6.7,8,9,0,4,4,6,)
print( type(a))
print( type(b))


# ==============================方式2：继承方式===============================

class Sayhi(Thread):
    def __init__(self, name):
        super(Sayhi,self).__init__()
        self.name = name

    def run(self):
        time.sleep(2)
        print(r'%s say hello' % (self.name))
        print(threading.current_thread().name)


if __name__ == '__main__':
    t = Sayhi('mike')
    t.start()
    # t.join()所有子线程结束才结束主线程
    t.join()
    print("主线程")
    print(threading.current_thread().name)