#! /usr/bin/env python3
# -*- coding:utf-8 -*-
1.
# while else  和for  else
#  因为else语句不是独立语句而是语句块，语句块只有当回退到和与闭合的块
# 一样的缩进量时语句结束，所以else语句不会单独结束

'''
while else  和for  else
意思就是while是和else一块的。
当有break或者return的时候，会跳出while块，
又因为while和else是一个整体，所以就跳出else，就不执行else
1.所以只要没有break或者return，不管while是否执行，都会执行else语句（continue也是可以执行else）
while--else   可以代替  do while循环
'''

# 1.验证不执行while，仍然执行
count = 55
while count < 3:
    print(count, " 小于 5")
    count = count + 1
else:
    print(count, " 大于或等于 5")
#输出
'''
55  大于或等于 5
'''

# 2.验证break存在是否，不执行else
count = 1
while count < 3:
    print(count, " 小于 5")
    count = count + 1
    if count == 2:
        break
else:
    print(count, " 大于或等于 5")

#输出
'''
1  小于 5
'''

# 3.验证  while 正常循环时候，会执行else
count = 1
while count < 3:
    print(count, " 小于 5")
    count = count + 1

else:
    print(count, " 大于或等于 5")

#输出
'''
1  小于 5
2  小于 5
3  大于或等于 5
'''