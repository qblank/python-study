#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/19 22:39
# @Author  : evan_qb
# @Site    : 
# @File    : delBigFile.py
# @Software: PyCharm

basepath = 'D:\\'

import os

def printFile(path):
    for foldername, dirs, filenames in os.walk(path):
        for filename in filenames:
            try:
                filepath = os.path.join(foldername, filename)
                # print(filepath)
                if os.path.getsize(filepath) > 1 * 1024 * 1024 * 1024:
                    # if os.path.getsize(filepath) == 0:
                    print(filepath)
            except Exception as e:
                print('访问异常', e)


printFile(basepath)

