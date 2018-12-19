# encoding=utf8
import test
from test import printme as hw_printme

# 一般字符串
# print("hello world!")
# raw 多行转义转义字符
mystr = ur'''hsj
          is
          smart
          ‘小名:我的小名’
        '''
if __name__ == '__main__':
    print mystr
    test.myFunc()
    test.printme(ur"测试‘’")
    hw_printme(ur"测试-别名‘’")
