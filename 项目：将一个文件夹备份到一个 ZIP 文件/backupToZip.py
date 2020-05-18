#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/11 9:21
# @Author  : evan_qb
# @Site    : 
# @File    : backupToZip.py
# @Software: PyCharm

import zipfile, os


# 备份
def backupToZip(folder):
    os.chdir("F:\\test\\")
    folder = os.path.abspath(folder)
    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break
        number = number + 1
    # 创建zip文件
    print('创建 %s...' % (zipFilename))

    backupZip = zipfile.ZipFile(zipFilename, 'w')

    # 递归遍历文件夹和文件，添加到zip文件
    for foldername, subFolder, filenames in os.walk(folder):
        print('添加文件%s...' % foldername)
        backupZip.write(foldername)

        for filename in filenames:
            newBase = os.path.basename(folder) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue
            backupZip.write(os.path.join(foldername, filename))

    backupZip.close()
    print('备份成功')


backupToZip('F:\\test\\论文\\')
