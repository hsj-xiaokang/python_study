#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class UserInfo(object):
    def __init__(self, name, age, account):
        self.name = name
        self._age = age
        self.__account = account

    def get_account(self):
        return self.__account


if __name__ == '__main__':
    userInfo = UserInfo('两点水', 23, 347073565);
    # 打印所有属性
    # print(dir(userInfo))
    # 打印构造函数中的属性
    # print(userInfo.__dict__)
    # print(userInfo.get_account())
    # 用于验证双下划线是否是真正的私有属性
    print(userInfo._UserInfo__account)
    print(userInfo.name)
    print(userInfo._age)

    # 私有属性以两个下划线开头。
    # 私有属性只能在类内部访问，类外面访问会出错。
    # 私有属性之所以不能在外面直接通过名称来访问，其实质是因为python做了一次名称变换。
    # userInfo._UserInfo__account
    # print(userInfo.__account)
