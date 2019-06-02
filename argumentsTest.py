#!/usr/bin/env python
# encoding: utf-8
'''
@author: heshengjin-何胜金
@contact: 2356899074@qq.com
@software: pycharm
@file: argumentsTest.py
@time: 2018/12/22 0022 16:37
@desc:可变参数实际函数内部是一个tuple（不可变了,但是不是真的不可改变）
      关键字参数实际还是一个dict（只是一个copy拷贝，完全不是外面那个,***浅拷贝***）
      一般的就是就是类似Java参数一般基本数值和引用传递（测试参数引用传递,类似Java等参数方式）
'''


def test(n, *g, **kw):
    print( '--------------change----------------------')
    # 一半参数list
    print( isinstance(n, list))

    # 可变参数tuple
    print( isinstance(g, list))

    # 关键字参数，copy的dict
    print( isinstance(kw, dict))

    # 改变一半参数
    n.append(100)

    # 改变可变参数,tuple不可以改变
    g[3].append(100)

    # 改变关键字参数，改变copy的那个
    kw['lby'].append(100)

    print( n)
    print( g)
    print( kw)

# -*- coding: UTF-8 -*-

def print_user_info( name ,  age  , sex = '男' ,**g):
    # 打印用户信息
    print('昵称：{}'.format(name) , end = ' ')
    print('年龄：{}'.format(age) , end = ' ')
    print('性别：{}'.format(sex) ,end = ' ' )
    print(g)
    # print('爱好：{}'.format(hobby))
    return;

# 调用 print_user_info 函数
print_user_info( '两点水' ,18 , '女',g=[1,2,3])


if __name__ == '__main__':

    # 一般参数list
    n = [7, 8, 9]

    # 可变参数，list
    g = [1, 2, 3, [1, 2, 3]]
    # list
    # print isinstance(g, list)

    # 关键字参数，字典
    # dict
    kw = {'hsj': 27, 'lby': [1, 2, 3, 4]}
    # print isinstance(k, dict)

    print( '--------------start----------------------')
    print( n)
    print( g)
    print( kw)

    test(n, *g, **kw)
    print( '---------------end---------------------')
    print(n)
    print( g)
    print( kw)

