#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   ex.3.2.1.py
@Time    :   2022/01/09 11:22:22
@Author  :   袁利锋
@Contact :   lifng.yuan@gmail.com
@Department   :  None
@Desc    :   None
'''

# here put the import lib

# 根据半径，求圆的面积
# 诉求：计算半径是10的圆的面积

# 使用函数

# ①无参数、无返回值
def area():
    print(3.14*10*10)

area()

# ② 有参、无返回值
# def area1(r):
#     print(3.14*r*r)

# area1(10)

# ③ 无参、有返回值
# def area2():
#     return 3.14*10*10

# print(area2())

# ④ 有参有返回值
# def area3(r):
#     return 3.14*r*r

# print(area3(10))


# 总结：
# 如果没有返回值，直接调用函数，执行函数
# 如果有返回值，函数的运行结果 ，作为一个值来使用
# 无参数。函数的功能是固定的
# 如果有参数，函数的功能更灵活

# 根据长方形的边长计算面积
# ①
# def RecArea():
#     print(3*4)

# RecArea()
# 2
# def RecArea():
#     return 3*4

# print(RecArea())
# 3
# def RecArea(length,width):
#     print(length*width)

# RecArea(3,4)

# 4

def RecArea(length,width):
    return length* width

print(RecArea(3,4))
print(RecArea(5,6))