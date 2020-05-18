#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/29 21:46
# @Author  : evan_qb
# @Site    : 
# @File    : 3.用BeautifulSoup模块解析HTML.py
# @Software: PyCharm

import requests, bs4

count = 1

# #  article-item-box > article-item-box

url = 'https://blog.csdn.net/Evan_QB/article/list/'
downpath = 'F:\\test\\download\\Evan_QB发布的文章列表.txt'
downFile = open(downpath, 'a', encoding='utf-8')
for i in range(1, 13):
    downFile.write('='*30 + '第' + str(i) + '页' + '='*30 + '\r\n')
    # 获取内容
    res = requests.get(url + str(i))
    res.raise_for_status()
    noStarchSoup = bs4.BeautifulSoup(res.text, 'lxml')
    # 解析内容
    # select获取对应元素的数据
    itembox = noStarchSoup.select('.article-list .csdn-tracking-statistics h4 > a')

    for item in itembox:
        # 获取链接地址
        itemUrl = item.attrs['href']
        cons = item.text.strip().split(' ')
        # 获取文章标题
        docTitle = cons[len(cons) - 1]
        downFile.write(str(count) + '.' + docTitle + '\t' * 2 + itemUrl + '\r\n')
        count += 1
print('获取成功')
downFile.close()



