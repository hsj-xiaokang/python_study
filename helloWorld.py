# encoding=utf8
import test
from test import printme as hw_printme

# 一般字符串
# print("hello world!")
# raw 多行转义转义字符
mystr = r'''hsj
          is
          smart
          ‘小名:我的小名’
        '''

mystr2 = r"""hsj
          is
          smart
          ‘小名:我的小名’
        """
if __name__ == '__main__':
    print(mystr2)
    test.myFunc()
    test.printme(r"测试‘’")
    hw_printme(r"测试-别名‘’")
