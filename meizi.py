#!/usr/bin/env python
# encoding: utf-8
'''
@author: heshengjin-何胜金
@contact: 2356899074@qq.com
@software: pycharm
@file: meizi.py
@time: 2018/12/19 17:25
@desc:
'''
import requests
from bs4 import BeautifulSoup
import random
from datetime import date
import os
import threading
import sys,re

PWD = "E:/Python/meizi/"

headers={
        "Referer":"http://www.mm131.com/",
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537."
    }
# 下载
def getMM131Img(siteUrl):
    resp=requests.get(siteUrl)
    resp.encoding='utf-8'
    soup = BeautifulSoup(resp.text,'html5lib')

    dirname=soup.find('div',class_='content').h5.string
    pagecount=soup.find('div',class_='content-page').span.string

    tmpm = re.findall('\d+',pagecount) #正则从字符串提取数字
    piccount=int(tmpm[0])

    imgStr=soup.find('div',class_='content-pic').img['src']
    prefix=imgStr[:imgStr.rfind("/")+1]
    picext="."+imgStr.split(".")[-1]
    resp.close()

    session=requests.Session()
    for img in [ prefix+str(i+1)+picext for i in range(piccount)]:
        name=img.split('/')
        if not dirname:
            dirname=date.today().strftime("%Y%m%d")
        filename=PWD +dirname+str(random.randrange(1000))+name[len(name)-1]

        with open(filename,'wb') as f:
            print(img)
            try:
                resp1=session.get(img,headers=headers,timeout=30,stream=True)
                for chunk in resp1.iter_content(chunk_size=1024):
                    f.write(chunk)
                resp1.close()
            except:
                print(sys.exc_info());
    session.close()
    print(u"图片下载完成")
if __name__=='__main__':
    if not os.path.exists(PWD):
        os.makedirs(PWD)
    for numberItem in range(1900, 1000000):
    # for numberItem in range(1900,3900):
        # print numberItem
        # print 'http://www.mm131.com/xinggan/'+bytes(numberItem)+'.html'
       try:
           getMM131Img('http://www.mm131.com/xinggan/'+bytes(numberItem)+'.html');
       except Exception,e:
           print e.message