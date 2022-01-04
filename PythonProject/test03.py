#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   test03.py
@Time    :   2022/01/04 16:50:54
@Author  :   袁利锋
@Contact :   lifng.yuan@gmail.com
@Department   :  None
@Desc    :   None
'''

# here put the import lib
# 红绿灯

light = input("当前路口的红绿灯颜色：红色red、黄色yellow、绿色Green")
if light=="red":
    print("红灯亮，请停止!")
elif light=="green":
    print("绿灯亮了，请开车！")
else:
    print("黄灯亮了，请等一等！")