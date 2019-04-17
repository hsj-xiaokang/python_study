# encoding=utf8
"""
多行注释
原来Python这样
"""
mystr = r'''
        这里不是注释
        多行操作
        '''


def createGenerator():
    mylist = range(3)
    for i in mylist:
        yield i * i
        print  (u'i=%s' % i)


# 执行代码
if __name__ == '__main__':
    mygenerator = createGenerator()
    for i in mygenerator:
        print(i)
    # 第二遍的时候就不会打印，原因是没有了
    for i in mygenerator:
        print(i)
    print( mystr)