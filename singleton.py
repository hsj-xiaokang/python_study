#!/usr/bin/env python3
# -*- coding:UTF-8 -*-
"""
单列模式
"""

class singleton(object):
    __instance = None
    name = 'none name init'
    age = 18
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls, *args, **kwargs)

        return cls.__instance

    def __init__(self):
        print("--init--")
        self.nameV2 = 'nameV2'
        self.ageV2 = 28

s1 = singleton()
s2 = singleton()
print(id(s1))
print(id(s2))
print('================================')
s1.name = "singleton-1"
s2.name = "singleton-2"
print(s1._singleton__instance)
print(s2._singleton__instance)
print(s1.name)
print(s2.name)

s1.nameV2 = "singleton-v1"
s2.nameV2 = "singleton-v2"
print(s1.nameV2)
print(s2.nameV2)