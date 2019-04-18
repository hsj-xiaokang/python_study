#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
from enum import Enum


class User(Enum):
    Twowater = 98
    Liangdianshui = 30
    Tom = 12
    listTest=[1,2,3]
    strTest = '[1, 2, 3]'


Twowater = User.Twowater
Liangdianshui = User.Liangdianshui
listTest = User.listTest
strTest = User.strTest

print(Twowater == Liangdianshui, Twowater == User.Twowater , listTest == User.listTest, strTest == User.strTest)
print(Twowater is Liangdianshui, Twowater is User.Twowater , listTest is User.listTest, strTest is User.strTest)

try:
    print('\n'.join('  ' + s.name for s in sorted(User)))
except TypeError as err:
    print(' Error : {}'.format(err))
