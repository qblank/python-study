#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/19 13:24
# @Author  : evan_qb
# @Site    : 
# @File    : clickGame.py
# @Software: PyCharm

from selenium import webdriver

brower = webdriver.Chrome()
brower.get("http://www.sorpack.com/dv_plus/game/csgaoshou.htm")
try:
    startStopBtn = brower.find_element_by_name("startstop")
    startStopBtn.click()

    radioBoxs = brower.find_elements_by_xpath("//input[@type='radio']")
    while True:
        for radioBox in radioBoxs:
            if radioBox.is_selected():
                radioBox.click()
        timeValue = brower.find_element_by_name("timeleft").get_attribute("value")
        print(timeValue)
        if int(timeValue) == 1:
            print("exit")
            break

finally:
    print("结束")

