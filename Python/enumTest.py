#!/usr/bin/env python
# encoding: utf-8
'''
@author: heshengjin-何胜金
@contact: 2356899074@qq.com
@software: pycharm
@file: enumTest.py
@time: 2019/4/21 0021 21:40
@desc:枚举测试
'''
from enum import Enum, unique
# instance=>MonthInstance
# aliceName=>MonthName
MonthInstance = Enum('MonthName', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

# 遍历枚举类型
for name, member in MonthInstance.__members__.items():
    print(name, '---------', member, '----------', member.value)

# 直接引用一个常量
print('\n', MonthInstance.Jan)

# instance=>Month
# aliceName=>Month
@unique
class Month(Enum):
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
    print(Month.Jan, '----------',
          Month.Jan.name, '----------', Month.Jan.value)
    for name, member in Month.__members__.items():
        print(name, '----------', member, '----------', member.value)