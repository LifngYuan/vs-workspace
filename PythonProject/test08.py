#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   test08.py
@Time    :   2022/01/05 14:07:18
@Author  :   袁利锋
@Contact :   lifng.yuan@gmail.com
@Department   :  None
@Desc    :   None
'''

# here put the import lib

age = int(input("请输入参观游园的年龄："))
if age < 18 or age > 60:
    print("你可以免费游览")
else:
    print("请付费参观")
