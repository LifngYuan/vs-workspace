#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   test2.2.1.py
@Time    :   2022/01/07 12:06:01
@Author  :   袁利锋
@Contact :   lifng.yuan@gmail.com
@Department   :  None
@Desc    :   None
'''

# here put the import lib
# import math
# 1、计算1-100的和
# 1
# sum=0
# for i in range(1,101):
#     sum = sum+i
# print(sum)

# 2  使用函数sum的方式计算；
# print(sum(range(1,101)))

# 2.输出1-100内的所有奇数；
# 1,利用条件语句实现
# for i in range(1,100):
#     if i%2==1:
#         print(i)
# # 2.控制起始值和步长的方式实现
# for i in range(1,101,2):
#     print(i)


# 3.将1到100以内，所有被7整除的数输出；

# 1.
for i in range(1,100):
    if i%7==0:
        print(i,end=";")
#2.


