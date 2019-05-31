#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/4/29 17:02
# @Author  : 何胜金-heshengjin
# @Site    : 
# @File    : type_test.py
# @Software: PyCharm
"""
type()使用

type() 函数是一个元类

可以看到，在 Python 中，类也是对象，你可以动态的创建类。
    其实这也就是当你使用关键字 class 时 Python 在幕后做的事情，而这就是通过元类来实现的。
"""

def printHello(self,name='Py'):
    print("helloMethod {}".format(name))

# 创建一个Hello类
Hello = type('aHello',(object,),dict(helloMethod=printHello))

h = Hello()

h.helloMethod(name="测试type定义的类的方法")

print(type(Hello))

print(type(h.__class__))

print(Hello.__name__)

print(h.__class__)