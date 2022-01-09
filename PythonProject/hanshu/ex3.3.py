#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   ex3.3.py
@Time    :   2022/01/09 14:11:57
@Author  :   袁利锋
@Contact :   lifng.yuan@gmail.com
@Department   :  None
@Desc    :   None
'''

# here put the import lib

# 定义局部函数
# 制作计算器

# 定义counter计算器的函数

# def counter(type,num1,num2):
    # 定义加法
#     def jia(num1,num2):
#         return num1+num2

#     # 定义减法
#     def jian(num1,num2):
#         return num1 - num2

#     # 定义乘法
#     def cheng(num1,num2):
#         return num1 * num2

#     # 定义除法
#     def chu(num1,num2):
#         return num1/num2

#     # 调用
#     if type == "jia":
#         return jia(num1,num2)
#     elif type == "jian":
#         return jian(num1,num2)
#     elif type == "cheng":
#         return cheng(num1,num2)
#     else:
#         return chu(num1,num2)

# print(counter("jia",12,13))


# 使用lambda函数

def  counter(type):
    if type=="add":
        return lambda x:x+12
    else:
        return lambda x:x*11

n = counter("add")

print(n(8))