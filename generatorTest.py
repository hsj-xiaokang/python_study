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


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
        print a, b, n


if __name__ == '__main__':
    print s
    f = fib(6)
    # while True:
    #     try:
    #         g = next(f)
    #         # print g
    #     except StopIteration, e:
    #         print e
    #         break
    for i in f:
        print i

    # 列表生成器
    generator_ex = (x * x for x in range(10))
    print(generator_ex)
    for i in generator_ex:
        print(i)
