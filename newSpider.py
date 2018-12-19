#!/usr/bin/env python
# encoding: utf-8
'''
@author: heshengjin-何胜金
@contact: 2356899074@qq.com
@software: pycharm
@file: newSpider.py
@time: 2018/12/19 14:10
@desc:==爬取网易新闻排行榜==

网络爬虫之最基本的爬虫：爬取网易新闻排行榜
一些说明：

使用urllib2或requests包来爬取页面。

使用正则表达式分析一级页面，使用Xpath来分析二级页面。

将得到的标题和链接，保存为本地文件。
'''
import os
# import sys
import urllib2
import requests
import re
from lxml import etree

# 保存文件
def StringListSave(save_path, filename, slist):
    # 不存在就创建目录
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    # 文件
    path = save_path+"/"+filename+".txt"
    with open(path, "w+") as fp:
        # 窦靖童景甜唐艺昕机场“势不三立”有戏看了   http://lady.163.com/18/1219/00/E3BL885R00267VQQ.html
        for s in slist:
            fp.write("%s\t\t%s\n" % (s[0].encode("utf8"), s[1].encode("utf8")))

def Page_Info(myPage):
    '''Regex'''
    mypage_Info = re.findall(r'<div class="titleBar" id=".*?"><h2>(.*?)</h2><div class="more"><a href="(.*?)">.*?</a></div></div>', myPage, re.S)
    return mypage_Info

def New_Page_Info(new_page):
    '''Regex(slowly) or Xpath(fast)'''
    # new_page_Info = re.findall(r'<td class=".*?">.*?<a href="(.*?)\.html".*?>(.*?)</a></td>', new_page, re.S)
    # # new_page_Info = re.findall(r'<td class=".*?">.*?<a href="(.*?)">(.*?)</a></td>', new_page, re.S) # bugs
    # results = []
    # for url, item in new_page_Info:
    #     results.append((item, url+".html"))
    # return results
    dom = etree.HTML(new_page)
    new_items = dom.xpath('//tr/td/a/text()')
    new_urls = dom.xpath('//tr/td/a/@href')
    assert(len(new_items) == len(new_urls))
    return zip(new_items, new_urls)

def Spider(url):
    i = 0

    # 主页parent
    print "-start to downloading url [%s] " % url
    myPage = requests.get(url).content.decode("gbk")
    # myPage = urllib2.urlopen(url).read().decode("gbk")
    myPageResults = Page_Info(myPage)
    save_path = u"网易新闻抓取"
    filename = str(i)+"_"+u"新闻排行榜"
    StringListSave(save_path, filename, myPageResults)

    i += 1
    # 子页
    for item, url in myPageResults:
        print "-inner start to downloading url [%s] " % url
        new_page = requests.get(url).content.decode("gbk")
        # new_page = urllib2.urlopen(url).read().decode("gbk")
        newPageResults = New_Page_Info(new_page)
        filename = str(i)+"_"+item
        StringListSave(save_path, filename, newPageResults)
        i += 1


if __name__ == '__main__':
    print "---------------------start--------------------"
    start_url = "http://news.163.com/rank/"
    Spider(start_url)
    print "---------------------end----------------------"