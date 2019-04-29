#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/4/29 14:52
# @Author  : 何胜金-heshengjin
# @Site    : 
# @File    : magic_method.py
# @Software: PyCharm
"""
魔术方法
"""


class MagicMethod(object):
    def __new__(cls, *args, **kwargs):
        return super(MagicMethod,cls).__new__(cls)

    def __init__(self,name,author):
        super(MagicMethod,self).__init__()
        self.name = name
        self.author = author

    def __getattr__(self, item):
        print("__getattr__,属性【不存在时候】调用该方法")
        return super(MagicMethod,self).__getattr__(item)

    def __getattribute__(self, item):
        print("__getattribute__,属性【存不存在都会】被调用")
        return super(MagicMethod,self).__getattribute__(item)

    def __setattr__(self, key, value):
        print("设置属性时候调用")
        return super(MagicMethod,self).__setattr__(key, value)

    def __delattr__(self, item):
        print("删除属性调用")
        return super(MagicMethod,self).__delattr__(item)

if __name__ == '__main__':
    # for m in dir(MagicMethod("MagicMethod_class","heshengjin-何胜金")):
    #       print(m)
    m = MagicMethod("MagicMethod","何胜金")
    print(m.author)
    print(m.hsj)
