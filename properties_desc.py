#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/4/29 15:18
# @Author  : 何胜金-heshengjin
# @Site    : 
# @File    : properties_desc.py
# @Software: PyCharm
"""
属性描述符使用详解
__get__
__set__
__del__
"""

class Meter(object):
    def __init__(self,value=0.0):
        super(Meter,self).__init__()
        self.value = float(value)

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        self.value = float(value)

class Foot(object):
    def __get__(self, instance, owner):
        return instance.meter * 3.2808

    def __set__(self, instance, value):
        instance.meter = float(value) / 3.2808


class Distance(object):
    meter = Meter()
    foot = Foot()

if __name__ == '__main__':
    d = Distance()
    print(d.meter,d.foot)
    d.meter = 1
    print(d.meter, d.foot)
    d.meter = 2
    print(d.meter, d.foot)