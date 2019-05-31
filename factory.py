#!/usr/bin/env python3
# -*- coding:UTF-8 -*-
"""
工厂模式
"""

#水果
class Fruit(object):
    def __init__(self):
        pass

    def getTypeFruit(self):
        print('fruit')


#apple
class Apple(Fruit):
    def __init__(self):
        pass

    def getTypeFruit(self):
        print('Apple')


# bananer
class Banane(Fruit):
    def __init__(self):
        pass

    def getTypeFruit(self):
        print('Banane')

class FruitFactory(object):
    # fruits_names = {'apple': 'apple', 'banane': 'banane'}
    fruits = {'apple':Apple,'banane':Banane}

    def __new__(cls, name):
        if name in cls.fruits.keys():
            return cls.fruits[name]()
        else:
            return Fruit()

if __name__ == '__main__':
    FruitFactory('apple').getTypeFruit()
    FruitFactory('banane').getTypeFruit()
    FruitFactory('tomato').getTypeFruit()

    print(FruitFactory.fruits)