#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/4/30 12:41
# @Author  : 何胜金-heshengjin
# @Site    : 
# @File    : t.py
# @Software: PyCharm
"""
虚拟virtualenv
pip install requests
pip install beautifulsoup4
"""

import requests
from bs4 import BeautifulSoup


r = requests.get('https://www.ynjsedu.cn/publicaccess/courseDetail?pCourseGuid=181')
# 设置编码
r.encoding='utf-8'
# print(r.text)
# BeautifulSoup解析
soup = BeautifulSoup(r.text, "html.parser")
for aitem in soup.findAll("a"):
    print (aitem.string)