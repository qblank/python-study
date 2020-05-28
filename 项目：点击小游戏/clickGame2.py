#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/19 13:24
# @Author  : evan_qb
# @Site    : 
# @File    : clickGame.py
# @Software: PyCharm

from selenium import webdriver
import time

brower = webdriver.Chrome()
brower.get("http://www.webhek.com/post/color-test.html")
try:
    startStopBtn = brower.find_element_by_class_name("btns")
    startStopBtn.click()
    boxs = brower.find_element_by_id("box").find_elements_by_tag_name("span")
    while True:
        for i in range(len(boxs) - 1):
            boxs = brower.find_element_by_id("box").find_elements_by_tag_name("span")
            flag = boxs[i].get_attribute("style") != boxs[i + 1].get_attribute("style")
            print(flag)
            if flag:
                boxs[i].click()


finally:
    print("结束")

