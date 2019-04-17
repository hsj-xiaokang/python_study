#!/usr/bin/env python
# encoding: utf-8
s = '''
@author: heshengjin-何胜金
@contact: 2356899074@qq.com
@software: pycharm
@file: generatorTest.py
@time: 2018/12/23 0023 16:28
@desc:generator列表生成器-保留的仅仅是算法，使用的时候才开始
'''

if __name__ == '__main__':
    # 列表生成器
    generator_ex = (x * x for x in range(10))
    print(generator_ex)
    for i in generator_ex:
        print(i)
