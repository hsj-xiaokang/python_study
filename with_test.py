#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/4/30 14:57
# @Author  : 何胜金-heshengjin
# @Site    : 
# @File    : with_test.py
# @Software: PyCharm
"""
with
Python with语句定义及使用:https://blog.csdn.net/windy135/article/details/82584883
"""
from builtins import object


class Sample(object):
    def __enter__(self):
        print('in enter')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print( "type: ", exc_type)
        print( "val: ", exc_val)
        print( "tb: ", exc_tb)

    def do_something(self):
        bar = 1 / 0
        return bar + 10

    def do_something2(self):
        bar = 1 / 1
        return bar + 10


with Sample() as sample:
    print (sample.do_something2())
