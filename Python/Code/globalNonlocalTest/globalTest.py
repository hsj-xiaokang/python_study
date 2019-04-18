#!usr/bin/env python
# -*- coding: UTF-8 -*-
# outer()没有局部变量a，则往上使用全局变量a
'''
博客地址：
https://blog.csdn.net/qw_sunny/article/details/80972357
'''
# def outer():
#     def inner():
#         global a
#         a = 8  # a3  既是inner局部变量，又是模块全局变量
#         print(a)  # a3 8，在inner的局部作用域中找到了a3
#     inner()  # inner()函数结束，a3作为inner局部变量被释放
#     print(a)  # a3 9,在outer局部作用域中没找到a，往上在全局作用域中找到了全局变量a3
# outer()  # outer()函数结束，a2作为outer局部变量被释放
# print(a)  # a3 8，在当前模块全局作用域中找到了a3


# a = 10  # a1 当前模块全局变量
# def outer2():
#     a = 9 # a2 outer2作用域局部变量
#     print(a) # a2 9,还未被a3改变
#     def outer1():
#         print(a) # a2 9,在outer1中没找到局部变量a，则寻找外层(outer2)变量a2(还未被a3改变)
#         def inner():
#             nonlocal a
#             a = 0  # a3 既是inner局部变量，又是再外层outer2作用域变量
#             print(a)  # a3 0, 找到inner局部变量a3
#         inner()  # inner()函数结束，a3作为外层变量(outer2局部变量)被保留成为a2
#         print(a)  # a2 0,在outer1中没找到局部变量a，则寻找外层(outer2)变量a2(被a3改变)
#     outer1()
#     print(a) # a2 0, 在outer1中找到outer1局部变量a2(被a3改变)
# outer2()
# print(a)  # a1 10，在当前模块全局作用域中找到了a1

###############################################全局变量不是外层变量，不被nonlocal寻找###################################
# a = 10  # a1 当前模块全局变量
# def outer():
#     def inner():
#         nonlocal a  # 在当前作用域外层即outer局部作用域中没找到outer局部变量a，outer外层为全局作用域，nonlocal不继续寻找，报错
#         a = 8
#         print(a)
#     inner()
#     print(a)
# outer()
# print(a)  # a1 10，在当前模块全局作用域中找到了a1

a = 10  # a1 当前模块全局变量
def outer2():
    nonlocal a  # outer2下一层为全局作用域，nonlocal不寻找全局变量，报错
    a = 8
    print(a)
outer2()
print(a)  # a1 10，在当前模块全局作用域中找到了a1