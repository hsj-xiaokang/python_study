#!/usr/bin/env python
# encoding: utf-8
'''
@author: heshengjin-何胜金
@contact: 2356899074@qq.com
@software: pycharm
@file: mySpider.py
@time: 2018/12/19 15:09
@desc:
'''
import re
import os
import requests
import time

# 需要修改变量之前说明一下global
global PhotoNum
PhotoNum = 0
# 存放路径
PWD = "E:/Python/ai2018-3-12/huaban/"
# http头部
head = { "Referer":"http://huaban.com/",'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
# 超时时间
TimeOut = 30

# 花瓣网
url = "http://huaban.com/favorite/beauty/"
# 图片前缀
url_image = "http://hbimg.b0.upaiyun.com/"
# 下一页
urlNext = "http://huaban.com/favorite/beauty/?iqkxaeyv&limit=20&wfl=1&max="

# 下载图片开始
def downfile(file, url):
    # print("开始下载：", file, url)
    try:
        # 图片字节流保存文件
        r = requests.get(url, stream=True)
        with open(file, 'wb') as fd:
            for chunk in r.iter_content():
                fd.write(chunk)
    except Exception as e:
        print("下载失败了", e)

# 下一页请求
def requestpageText(url):
    try:
        Page = requests.session().get(url, headers=head, timeout=TimeOut)
        # 避免乱码
        Page.encoding = "utf-8"
        # print Page.text
        return Page.text
    except Exception as e:
        # print("联网失败了...重试中", e)
        time.sleep(5)
        # print("暂停结束")
        requestpageText(url)

# 网页请求
def requestUrl(url):
    global PhotoNum
    # print("*******************************************************************")
    # print(u'请求网址：[%s]' % url)

    text = requestpageText(url)
    pattern = re.compile('{"pin_id":(\d*?),.*?"key":"(.*?)",.*?"like_count":(\d*?),.*?"repin_count":(\d*?),.*?}', re.S)
    items = re.findall(pattern, text)
    print(items)

    max_pin_id = 0
    for item in items:
        max_pin_id = item[0]
        x_key = item[1]
        x_like_count = int(item[2])
        x_repin_count = int(item[3])

        if (x_repin_count > 10 and x_like_count > 10) or x_repin_count > 100 or x_like_count > 20:

            # print("开始下载第{0}张图片".format(PhotoNum))
            # 网络图片位置
            url_item = url_image + x_key
            # 文件名称
            filename = PWD + str(max_pin_id) + ".jpg"
            if os.path.isfile(filename):
                # print("文件存在：", filename)
                continue

            downfile(filename, url_item)
            PhotoNum += 1
    requestUrl(urlNext + max_pin_id)

# 本文件执行
if __name__ == '__main__':
    if not os.path.exists(PWD):
           os.makedirs(PWD)
    requestUrl(url)