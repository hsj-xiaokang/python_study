# encoding=utf8
def printme(str):
    "打印任何传入的字符串"
    print(str)
    return


def myFunc():
    print('my first function!')

# 单独的运行当前的文件就是__name__=__main__
# import就是当前文件的名字
if __name__ == '__main__':
    printme('hsj is smart!')
    myFunc()
