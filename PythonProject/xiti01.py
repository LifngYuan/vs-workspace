#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   xiti01.py
@Time    :   2022/01/05 14:20:58
@Author  :   袁利锋
@Contact :   lifng.yuan@gmail.com
@Department   :  None
@Desc    :   None
'''

# here put the import lib
# 练习题：
# 1、面试成绩、笔试成绩都大于60分，可以进入复试；否则，没有资格进入复试；
# 2、面试成绩、笔试成绩任意一个科目小于60分，没有资格进入复试；否则进入复试；


MianShi = int(input("请输入您的面试成绩"))
BiShi = int(input("请输入您的笔试成绩："))
# 1.
if MianShi>60 and BiShi>60:
    print("可以进入复试")
else :
    print("没有资格进入复试")
# 2.
if MianShi<60 or BiShi<60:
    print("没有资格进入复试")
else:
    print("进入复试")

