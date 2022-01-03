#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   example3.py
@Time    :   2022/01/03 15:09:38
@Author  :   袁利锋
@Contact :   lifng.yuan@gmail.com
@Department   :  None
@Desc    :   None
'''

# here put the import lib

# 将两个数按照从小到大排序
x = 66
y = 77
print("x=", x, "y=", y)
# 1.
# if x<y:
#     t=x
#     x=y
#     y=t
# print("x=",x,"y=",y)

# 2.
# if x>y:
#     print(y,x)
# if x<=y:
#     print(x,y)

# 3.
if x > y:
    x, y = y, x
print("x=", x, "y=", y)
