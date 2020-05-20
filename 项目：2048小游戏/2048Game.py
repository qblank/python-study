#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/19 15:02
# @Author  : evan_qb
# @Site    : 
# @File    : 2048Game.py
# @Software: PyCharm

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
import time

browser = webdriver.Chrome()
browser.get("https://2048game.com/")

try:
    time.sleep(1)
    htmlElem = browser.find_element_by_tag_name('html')
    for i in range(0, 1000):
        num = random.randint(1, 4)
        if num == 1:
            htmlElem.send_keys(Keys.UP)
        if num == 2:
            htmlElem.send_keys(Keys.LEFT)
        if num == 3:
            htmlElem.send_keys(Keys.RIGHT)
        if num == 4:
            htmlElem.send_keys(Keys.DOWN)
        i = i + 1
finally:
    print("结束")
