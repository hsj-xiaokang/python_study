# encoding=utf8
def testWith():
    t = (0, 1, 2, 3, 4)
    # with t as mytuple:
    for item in t:
        print item
# return 'test'


NAME = "xueweihan"

def get_NAME():
    return NAME

def set_NAME(name_value):
    global NAME
    NAME = name_value


if __name__ == '__main__':
    # testWith()
    print  get_NAME()
    set_NAME("hsj")
    print  get_NAME()
