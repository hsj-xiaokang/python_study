#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/4/29 14:38
# @Author  : 何胜金-heshengjin
# @Site    : 
# @File    : extend_class.py
# @Software: PyCharm
"""
类的继承性
"""


class Parent(object):
    def __init__(self,age):
        self.__name = "parent's name"
        self.age = age

    def get_p_name(self):
        print(self.__name)

    def get_p_age(self):
        print("parent's age is {}".format(self.age))
        return self.age


class Chirld(Parent):
    def __init__(self,age,address):
        super(Chirld,self).__init__(age)
        self.addres = address

    def get_p_name(self):
        print("chirld's name is none")

    def get_c_age(self):
        print("chirld's age is None,but parent's age is  {}".format(super(Chirld,self).get_p_age()))

if __name__ == '__main__':
    c = Chirld(18,"云南省昆明市官渡")
    print(c.get_p_name())
