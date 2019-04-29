#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/4/29 16:36
# @Author  : 何胜金-heshengjin
# @Site    : 
# @File    : enum_test.py
# @Software: PyCharm
"""
枚举的使用
"""

from enum import Enum, unique
# import enum

m = Enum("month",('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

# for name,meber in m._member_map_.items():
#     print(name, '---------', meber, '----------', meber.value)

@unique
class Month2(Enum):
    Jan = 'January'
    Feb = 'February'
    Mar = 'March'
    Apr = 'April'
    May = 'May'
    Jun = 'June'
    Jul = 'July'
    Aug = 'August'
    Sep = 'September '
    Oct = 'October'
    Nov = 'November'
    Dec = 'December'


if __name__ == '__main__':
    print(Month2.Jan.name)
    print(Month2.Jan.value)
