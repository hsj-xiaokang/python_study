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
import collections.abc

if __name__ == '__main__':
     print (isinstance([1, 2, 3], collections.abc.Iterable))
     print (isinstance(122, collections.abc.Iterable))


     # python range() 函数可创建一个整数列表
     # Python3.x中range()函数返回的结果是一个整数序列的对象，而不是列表。
     print (list(range(0, 100)))

