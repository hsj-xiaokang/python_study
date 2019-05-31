# encoding=utf8　如果不加这一行会报错
class Person(object):
    # 属于类
    __decClsPrivate = r'i am a person class private'
    decClsPublic = r'i am a person class public'

    def __init__(self, name, age):
        # 属于对象
        self.name = name
        self.age = age

    @property
    def getPriveDec(self):
        return self.__decClsPrivate

    # 实现拦截所有的特性访问(属性和方法)，在访问的时候打log啥的
    def __getattribute__(self, item):
        print (r"====access attribute(访问了特性):====" + item)
        # return object.__getattribute__(self, item)
        return super(Person, self).__getattribute__(item)

    # 对象获取不存在的属性值，会自动调用__getattr__方法
    def __getattr__(self, attr):
        return (u'未找到属性%s' % attr)


if __name__ == '__main__':
    aPerson = Person(r'hsj-xiaokang', 18)
    # 什么叫做动态语言，类似js
    print( aPerson.nameage)
    aPerson.nameage = u"xiaokang-26"
    print( aPerson.nameage)

    print( aPerson.name)
    print( aPerson.decClsPublic)
    print( aPerson.getPriveDec)

    aPerson.decClsPublic = u'我是aPerson,我修改了Person类对象属性?哈哈，修改不了，被你自己覆盖了！类似于js,会自己覆盖属性哈哈'
    bPerson = Person(r'lby-ayou', 18)
    print( bPerson.name)
    print( bPerson.decClsPublic)
    print( aPerson.decClsPublic)
    print( bPerson.getPriveDec)

    print(bPerson._Person__decClsPrivate)
