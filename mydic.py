# encoding=utf8
dic = {'jon': '-boy-', 'lili': '--girl--', 'numbers': 123}

# 测试
if __name__ == '__main__':
    print dic['jon']
    print dic["jon"]

    for index, key in enumerate(dic):
        print u'index=%s,key=%s,value=%s' % (index, key, dic[key])

    print '===end==='
