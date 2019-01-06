#!/usr/bin/env python
# encoding: utf-8
'''
@author: heshengjin-何胜金
@contact: 2356899074@qq.com
@software: pycharm
@file: IterableTest.py
@time: 2018/12/23 0023 16:13
@desc:Iterable是不是可以迭代的判断
'''
import collections

if __name__ == '__main__':
     print isinstance([1, 2, 3], collections.Iterable)
     print isinstance(122, collections.Iterable)
     print list(range(0, 100))

