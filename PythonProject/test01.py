#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   test01.py
@Time    :   2022/01/03 16:37:01
@Author  :   袁利锋
@Contact :   lifng.yuan@gmail.com
@Department   :  None
@Desc    :   None
'''

# here put the import lib

# 1.将两个数字按照从大到小的顺序排序；
a = 999
b = 1288
if a < b:
    a, b = b, a
print("a=", a, "b=", b)
# 2.计算4个数值当中的最大值（MapReduce）；
date=[12,22,43,5]
date_max=max(date)
print("最大值=",date_max)