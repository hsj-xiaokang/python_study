#!/usr/bin/env python
# encoding: utf-8
'''
@author: heshengjin-何胜金
@contact: 2356899074@qq.com
@software: pycharm
@file: decoratorTest.py
@time: 2018/12/20 15:15
@desc:装饰器
'''
# ===========一般装饰器================
def debug(func):
    def wrapper(*args, **kwargs):  # 指定宇宙无敌参数
        print( "[DEBUG]: enter {}()".format(func.__name__))
        print( 'Prepare and say...'),
        return func(*args, **kwargs)
    return wrapper  # 返回

# @debug
def say1(something):
    print( r"hello {}!".format(something))
# 如果没有使用@语法，等同于
say1 = debug(say1)

# ===============带参数的装饰器=============
def logging(level):
    def wrapper(func):
        def inner_wrapper(*args, **kwargs):
            print( "[{level}]: enter function {func}()".format(
                level=level,
                func=func.__name__))
            return func(*args, **kwargs)
        return inner_wrapper
    return wrapper

# @logging(level='INFO')
def say2(something):
    print( r"say2 {}!".format(something))

# 如果没有使用@语法，等同于
say2 = logging(level='INFO')(say2)

# @logging(level='DEBUG')
# def say2(something):
#     print( r"say2 {}...".format(something))


if __name__ == "__main__":
    say1(r'一般装饰器')
    say2(r'带参数的装饰器hello')
    # do(r"带参数的装饰器my work")