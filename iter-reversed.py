#! /usr/bin/env python3
# -*- coding:utf-8 -8-
"""
迭代器和生成器综合例子
扯淡的python，一种无聊的代码风格要求
"""


class MyIterReversed(object):
    # 构造函数
    def __init__(self,start):
        super(MyIterReversed,self).__init__()
        self.start = start

     # 遍历重写
    def __iter__(self):
        n = self.start
        while n > 0:
            yield  n
            n -= 1

    # 反转重写
    def __reversed__(self):
        n = 1
        while n <= self.start:
             yield  n
             n += 1


# 遍历
for i in MyIterReversed(30):
    print(i)

for r in reversed(MyIterReversed(30)):
    print(r)

