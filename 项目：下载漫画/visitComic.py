#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/30 9:14
# @Author  : evan_qb
# @Site    : 
# @File    : visitComic.py
# @Software: PyCharm

import requests
from bs4 import BeautifulSoup
import urllib.request
import os

user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'

comicPath = 'F:\\test\\comic\\'
domainUrl = 'http://www.gllmh.com/'


def getRespone(url):
    req_header = {
        'User-Agent': user_agent
    }
    response = requests.get(url, headers=req_header)
    page = response.text
    page = page.encode('ISO-8859-1').decode('gbk', errors='ignore')
    result = BeautifulSoup(page, 'lxml')
    response.close()
    return result


def img_cover(url, titlePath, titleID):
    try:
        result = getRespone(url)
        imgList = result.select('.article-content img')
        for img in imgList:
            # 拼接路径
            img_url = img['src']
            urllib.request.urlretrieve(img_url, titlePath + "/%02d.jpg" % titleID)
            titleID = titleID + 1
            print("下载中....，进度:%d" % (titleID / len(imgList) * 100) + "%")
    except Exception as e:
        print("页面访问失败，继续访问下一个...")
        print(e)


def downImgUrlList(titleUrl, titlePath, titleID):
    result = getRespone(titleUrl)
    pageLiArr = result.select(".pagination-wrapper .pagination li a")
    print('访问分页的链接地址：' + titleUrl)
    img_cover(titleUrl, titlePath, titleID)
    for pageLi in pageLiArr[3:(len(pageLiArr) - 1)]:
        pageNo = pageLi.text
        tempUrl = titleUrl.replace('.html', '_' + pageNo + '.html')
        print('访问分页的链接地址：' + tempUrl)
        img_cover(tempUrl, titlePath, titleID)

def downComicByTypeUrl(url):
    result = getRespone(url)
    title = result.select('.listview')[0].text
    linkAList = result.select('ul li h3 a')
    print(title)
    typePath = comicPath + title
    if not os.path.exists(typePath):
        os.mkdir(typePath)
    print('-' * 50)
    for linkA in linkAList:
        titleUrl = domainUrl + linkA['href']
        titlePath = typePath + '/' + linkA['title'] + '/'
        if not os.path.exists(titlePath):
            os.mkdir(titlePath)
        print('正在下载:' + linkA['title'] + ':' + titleUrl)
        titleID = 0
        downImgUrlList(titleUrl, titlePath, titleID)


if __name__ == '__main__':
    # "http://www.gllmh.com/kbmh/xt300/"
    # downComicByTypeUrl('http://www.gllmh.com/kbmh/xt300/') 心跳300秒
    # downComicByTypeUrl('http://www.gllmh.com/gqbj/')
    downComicByTypeUrl('http://www.gllmh.com/bgyxz/')
