#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   test05.py
@Time    :   2022/01/04 18:01:39
@Author  :   袁利锋
@Contact :   lifng.yuan@gmail.com
@Department   :  None
@Desc    :   None
'''

# here put the import lib

age=int(input("请输入要判断的年龄："))
if age <18:
    print("青少年儿童")
elif 18<=age<60:
    if 40<=age<60:
        print("中年")
    else:
        print("青年")
else:
    print("老年人")