#!/usr/bin/env python
# encoding: utf-8
'''
@author: heshengjin-何胜金
@contact: 2356899074@qq.com
@software: pycharm
@file: reTest.py
@time: 2018/12/20 9:27
@desc:正则表达式
blog-see:https://www.cnblogs.com/wxshi/p/6827056.html

re.I(re.IGNORECASE): 忽略大小写（括号内是完整写法，下同）
M(MULTILINE): 多行模式，改变'^'和'$'的行为（参见上图）
S(DOTALL): 点任意匹配模式，改变'.'的行为
L(LOCALE): 使预定字符类 \w \W \b \B \s \S 取决于当前区域设定
U(UNICODE): 使预定字符类 \w \W \b \B \s \S \d \D 取决于unicode定义的字符属性
X(VERBOSE): 详细模式。这个模式下正则表达式可以是多行，忽略空白字符，并可以加入注释。
'''

import re


# ********************************将正则表达式编译成Pattern对象********************************
pattern = re.compile(r'hello')



# ********************************使用Pattern匹配文本，获得匹配结果，无法匹配时将返回None********************************
match = pattern.match(r'hello world!')


# ********************************re.X模式********************************
a = re.compile(r"""\d +  # the integral part
                   \.    # the decimal point
                   \d *  # some fractional digits""", re.X)
b = re.compile(r"\d+\.\d*")


# ********************************re模块********************************
m = re.match(r'hello', 'hello world!')
print( m.group())
print( '====================================================================')



# ********************************Pattern对象相关********************************
p = re.compile(r'(\w+) (\w+)(?P<sign>.*)', re.DOTALL)

print( "p.pattern:", p.pattern)
print( "p.flags:", p.flags)
print( "p.groups:", p.groups)
print( "p.groupindex:", p.groupindex)

# -----search----
# 将正则表达式编译成Pattern对象
pattern = re.compile(r'world')
# 使用search()查找匹配的子串，不存在能匹配的子串时将返回None
# 这个例子中使用match()无法成功匹配
match = pattern.search('hello world!')

if match:
    # 使用Match获得分组信息
    print( match.group())

# -----split----
p = re.compile(r'\d+')
print( p.split('one1two2three3four4'))

# -----findall----
p = re.compile(r'\d+')
print( p.findall('one1two2three3four4'))

# -----finditer----
p = re.compile(r'\d+')
for m in p.finditer('one1two2three3four4'):
    print( m.group())

print ('====================================================================')

# ********************************Match对象相关********************************
m = re.match(r'(\w+) (\w+)(?P<sign>.*)', 'hello world!',re.S)

print( "m.string:", m.string)
print( "m.re:", m.re)
print( "m.pos:", m.pos)
print( "m.endpos:", m.endpos)
print( "m.lastindex:", m.lastindex)
print( "m.lastgroup:", m.lastgroup)

print( "m.group(1,2):", m.group(1, 2))
print( "m.groups():", m.groups())
print ("m.groupdict():", m.groupdict())
print( "m.start(2):", m.start(2))
print( "m.end(2):", m.end(2))
print( "m.span(2):", m.span(2))
print( r"m.expand(r'\2 \1\3'):", m.expand(r'\2 \1\3'))
print( '====================================================================')


if __name__ == "__main__":
    if match:
        # 使用Match获得分组信息
        print( match.group())