#!/usr/bin/env python
# encoding: utf-8
'''
@author: heshengjin-何胜金
@contact: 2356899074@qq.com
@software: pycharm
@file: rangTest.py
@time: 2018/12/23 0023 16:16
@desc:1.rang循环生成
      2.多层循环
'''
import os

if __name__ == '__main__':
    print [x * x for x in range(1, 11) if x % 2 == 0]

    print [m + n for m in 'abc' for n in 'xyz']

    # 该目录下面的所有文件名和目录
    print [d for d in os.listdir('.')]
