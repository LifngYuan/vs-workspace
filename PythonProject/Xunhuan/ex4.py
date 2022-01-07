#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   ex4.py
@Time    :   2022/01/07 14:23:00
@Author  :   袁利锋
@Contact :   lifng.yuan@gmail.com
@Department   :  None
@Desc    :   None
'''

# here put the import lib

import random

# 用while遍历列表
# list=[7,9,8,10,33,5]
# i = 0 
# while i<len(list):
#     print("======这是第",i+1,"次循环======")
#     print("刚刚进入循环时i的值是：",i)
#     print("list[",i,"]=",list[i])
#     i+=1
#     print("i的值增加1后：",i)

# 奇偶数
# list = [34,2,3,55,44,11,9,0,8,6]
# # 定义一个列表
# # 在定义两个空列表，分别表示jishu【】和oushu【】
# jishu=[]
# oushu=[]
# ①逐个遍历
# i=0
# while i<len(list):
#     if list[i]%2==0:
#         oushu.append(list[i])
#     else:
#         jishu.append(list[i])
#     i+=1
# print(oushu)
# print(jishu)
# ②随机遍历
# while len(list)>0:
#     n=list.pop()
#     if n%2==0:
#         oushu.append(n)
#     else:
#         jishu.append(n)
# print(oushu)
# print(jishu)

# 练习
# 计算一个列表内：
# - 奇数的个数
# - 偶数的个数
# 定义一个1-100的列表
x=range(1,100)#随机生成1到100内的数字
list =list(x)#把随机生成的数字转化成list列表
# print(list)
a=0
b=0
# 方法A
# i=0

# while i<len(list):
#     if i%2==1:
#         a+=1
#     else:
#         b+=1
#     i+=1
# print("奇数的个数是：",a)
# print("偶数的个数是：",b)

# 方法B
while len(list)>0:
    n=list.pop()
    if n%2==1:
        a+=1
    else:
        b+=1
print("奇数的个数是：",a)
print("偶数的个数是：",b)

