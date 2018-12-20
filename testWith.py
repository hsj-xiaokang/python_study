#!/usr/bin/env python
# encoding: utf-8
'''
@author: heshengjin-何胜金
@contact: 2356899074@qq.com
@software: pycharm
@file: meizi.py
@time: 2018/12/19 17:25
@desc:testWith
'''
import types
import os
import random

def testWith():
    # 不存在就创建目录
    save_path = ur"测试python-with"
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    # 文件
    filename = str(random.randrange(1000))
    path = save_path + "/" + filename + ".txt"
    with open(path, "w+") as fp:
        slist = [ur'窦靖童景甜唐艺昕机场“势不三立”有戏看了',ur'http://lady.163.com/18/1219/00/E3BL885R00267VQQ.html']
        for s in slist:
            fp.write("%s\n" % (s.encode("utf8")))

def mytuple():
    t = (0, 1, 2, 3, 4)
    print type(t)
    return t

NAME = "xueweihan"

def get_NAME():
    return NAME

def set_NAME(name_value):
    global NAME
    NAME = name_value


if __name__ == '__main__':
    testWith()
    print  get_NAME()
    set_NAME("hsj")
    print  get_NAME()
