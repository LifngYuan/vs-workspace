#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   test02.py
@Time    :   2022/01/04 15:26:23
@Author  :   袁利锋
@Contact :   lifng.yuan@gmail.com
@Department   :  None
@Desc    :   None
'''

# here put the import lib

# 练习：
# 1、计算两个数字当中的较小值
x = 22
y = -33
if x <= y:
    r = x
else:
    r = y
print(r)
# 2、根据成绩判断其对应的两种情况
#     及格：继续努力
#     不及格：请认真复习，准备补考
ChengJi = int(input("请输入你的考试成绩："))
if ChengJi >=60:
    print("恭喜，考试及格了，要继续努力哦！")
else:
    print("不及格！请认真复习，准备补考！")