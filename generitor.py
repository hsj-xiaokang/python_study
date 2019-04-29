#! /usr/bim/env python3
# -*- coding:utf-8 -*-

"""
生成器使用
"""

g = (x*x for x in range(100))
print(g)

# for a in g:
#     print(a)


def my_function():
    for i in range(10):
        yield i


my = my_function()
print(my)
# for amy in my:
#     print(amy)

# print(next(my))
# print(next(my))
# print(next(my))
# print(next(my))
# print(next(my))
# print(next(my))
# print(next(my))
# print(next(my))
# print(next(my))
# print(next(my))
# print(next(my))
