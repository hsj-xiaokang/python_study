
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/4/29 17:57
# @Author  : 何胜金-heshengjin
# @Site    : 
# @File    : closure_test.py
# @Software: PyCharm
"""
闭包测试
 nonlocal只会在局部查找
"""

def study_time(time):
    def insert_time(min):
        nonlocal  time
        time = time + min
        return time

    return insert_time


f = study_time(0)
print(f(2))

print(f(10))
