#!/usr/bin/env python
# encoding: utf-8
'''
@author: heshengjin-何胜金
@contact: 2356899074@qq.com
@software: pycharm
@file: ${NAME}.py
@time: ${DATE} ${TIME}
@desc:
'''


def fun():
    for i in range(20):
        # 有种return的感觉
        yield i+20
        print('good', i)


# -*- coding: UTF-8 -*-
def fibon(n):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a + b

# 引用函数
for x in fibon(10):
    print(x , end = '\n ')

# if __name__ == '__main__':
    # for x in fun():
        # print(x)
