#!/usr/bin/env python
# encoding: utf-8
'''
@author: heshengjin-何胜金
@contact: 2356899074@qq.com
@software: pycharm
@file: reTest.py
@time: 2018/12/19 0019 23:21
@desc:正则表达式的使用demo学习
'''

# 查找以@author:开头的语句
def find_str_start():
    with open('text.txt') as f:
        for line in f:
            if line.startswith(r'@author:'):
                print line


# 查找以@author:开头的语句，@author结尾的语句
def find_str_start_end():
    with open('text.txt') as f:
        for line in f:
            # print line[-2:-1] 最后一个字符
            # python文件\n结尾-切片
            if line.startswith(r'@author:') and line[:-1].endswith('hsj'):
                print line


A = '_iAmA'


# 判断一个字符串是不是下划线开始或者字母开始-比较大小，数学操作
def pd():
    print A and (A.startswith('_') or 'a' <= A[0] <= 'Z')


# 开始
if __name__ == '__main__':
    # find_str_start()
    # find_str_start_end()
    pd()