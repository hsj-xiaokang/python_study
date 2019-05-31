#!/usr/bin/env python3
# -*- coding:UTF-8 -*-
"""
python的类变量和成员变量
"""


class TestClass(object):
    val1 = 'name class'
    val2 = []

    def __init__(self):
        self.name = 'name class - init'
        self.addr = [8]


if __name__ == '__main__':
    inst = TestClass()
    inst1 = TestClass()

    print(TestClass.val1)
    print(inst.val1)
    print(inst1.val1)

    print(TestClass.val2)
    print(inst.val2)
    print(inst1.val2)

    # print(inst.name)
    # print(inst1.name)
    # print(inst.addr)
    # print(inst1.addr)

    print('=======================')

    TestClass.val1 = 'name class v1'
    print(TestClass.val1)
    print(inst.val1)
    print(inst1.val1)

    TestClass.val2.append(1)
    print(TestClass.val2)
    print(inst.val2)
    print(inst1.val2)

    # inst.name = 'name class -init -change'
    # print(inst.name)
    # print(inst1.name)
    # print(inst.addr)
    # print(inst1.addr)

    print('=======================')

    inst.val1 = 'name class v2'
    print(TestClass.val1)
    print(inst.val1)
    print(inst1.val1)

    inst.val2.append(2)
    print(TestClass.val2)
    print(inst.val2)
    print(inst1.val2)

    # inst.addr.append(9)
    # print(inst.name)
    # print(inst1.name)
    # print(inst.addr)
    # print(inst1.addr)