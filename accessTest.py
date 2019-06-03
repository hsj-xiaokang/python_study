#!/usr/bin/env python
# encoding: utf-8
'''
@author: heshengjin-何胜金
@contact: 2356899074@qq.com
@software: pycharm
@file: accessTest.py
@time: 2019/4/21 0021 20:32
@desc:访问属性测试
'''


class Hsj(object):
    nickname = '小康'
    _colleage = '云南师范大学'
    __year = '2016/07/01'
    def __init__(self, name, age):
        self.name=name
        self.age=age

if __name__ == '__main__':
    hsjinstance = Hsj('hsj', 18)
    print(hsjinstance.nickname)
    print(hsjinstance._colleage)
    # print(hsjinstance._Hsj__year) this is true access attr method!
    print(hsjinstance.__year)
