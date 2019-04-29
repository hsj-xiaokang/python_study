#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/4/29 14:17
# @Author  : 何胜金-heshengjin
# @Site    : 
# @File    : scope_test.py
# @Software: PyCharm
"""
测试作用域的使用
"""


class TestScope(object):
    def __init__(self):
        super(TestScope,self).__init__()
        self.name = '测试作用域-name'
        self._age = '测试作用域-age'
        self.__sex = '测试作用域-sex'

if __name__ == '__main__':
    a = TestScope()
    print(a.name)
    print(a._age)
    # print(a.__sex)
    # 正确的使用方式-强制直接访问私有的变量
    print(a._TestScope__sex)

