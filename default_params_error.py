#!/usr/bin/env python3
# -*- coding:UTF-8 -*-
"""
https://blog.csdn.net/u012409883/article/details/71440711
Python函数参数默认值的陷阱和原理深究，【默认参数，编译时候确定】

such is true ；(下面才是正确的方式)
def generate_new_list_with(my_list=None, element=None):
    if my_list is None:
        my_list = []
    my_list.append(element)
    return my_list
"""


def generate_new_list_with(my_list=[], element=None):
     my_list.append(element)
     return my_list


list_1 = generate_new_list_with(element=1)
print(list_1)

list_2 = generate_new_list_with(element=2)
print(list_2)