#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   test04.py
@Time    :   2022/01/04 17:29:53
@Author  :   袁利锋
@Contact :   lifng.yuan@gmail.com
@Department   :  None
@Desc    :   None
'''

# here put the import lib

chengji = int(input("请输入本次考试的成绩："))
if chengji<60:
    print("不及格")
elif 60<=chengji <=90:
    print("良好")
else:
    print("优秀")