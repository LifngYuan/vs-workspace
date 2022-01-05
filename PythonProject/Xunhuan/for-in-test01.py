#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   for-in-test01.py
@Time    :   2022/01/05 16:33:26
@Author  :   袁利锋
@Contact :   lifng.yuan@gmail.com
@Department   :  None
@Desc    :   None
'''

# here put the import lib

# 构造一个列表，其由正数、负数、零构成。
list=[1,-2,3,-4,5,6,-7,8,-9,0]
# 将其中的正数输出。
for i in list:
    if i>0:
        print(i)
    else:
        pass