#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   ex3.py
@Time    :   2022/01/07 13:31:55
@Author  :   袁利锋
@Contact :   lifng.yuan@gmail.com
@Department   :  None
@Desc    :   None
'''

# here put the import lib
# 增值案例

# i=0
# while i<5:
#     print(i)
#     i+=1

# 减值案例

# i=5
# while i>0:
#     print(i)
#     i-=1


# 输出10以内的所有奇数；有两种方法

# x = 1

# 第一种：while循环：控制步长

# while x<10:
#     print(x,end=" ")
#     x+=2

# 第二种方法：使用条件语句，取模

# while x<10:
#     if x%2==1:
#         print(x,end=" ")
#     x+=1


# 空值
# 输入姓名为空的案例
# name=""
# while not name:
#     name=input("姓名不能为空：")
# print("hello",name)

# 将1到100以内的所有被7整除的数输出。（使用while）


# - 方式A：通过空值初始值和循环变量的方式；
# i=7
# while i<100:
#     print(i,end=" ")
#     i+=7

# - 方式B：通过循环结构嵌套的方式：
i=1
while i<100:
    if i%7==0:
        print(i,end=" ")
    i+=1