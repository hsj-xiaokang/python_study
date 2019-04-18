#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from enum import Enum

MonthEM = Enum('MonthName', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

# 遍历枚举类型
for name, member in MonthEM.__members__.items():
    print(name, '---------', member, '----------', member.value)

# 直接引用一个常量
print('\n', MonthEM.Jan)



# 另外的一种方式
class Color(Enum):
    red = 1
    orange = 2
    yellow = 3
    green = 4
    blue = 5
    indigo = 6
    purple = 7
    red_alias = 1
for color in Color.__members__.items():
    print(color)
print(Color.red.value)