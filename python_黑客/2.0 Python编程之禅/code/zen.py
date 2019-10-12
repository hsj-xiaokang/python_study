# -*- coding: UTF-8 -*-

# stringStest = 'abcdefghijk'
 
# for char in stringStest[1:]:
# if char !='c':
# print 'not c'

stringStest = 'abcdefghijk'
 
for char in stringStest[1:]:
    if char !='c':
        print('not c')

# range转生成器
h = (char for char in range(1,100))
s = range(1,100)
print(h)
print(s)