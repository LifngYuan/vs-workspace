#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   case02.py
@Time    :   2022/01/05 14:49:01
@Author  :   袁利锋
@Contact :   lifng.yuan@gmail.com
@Department   :  None
@Desc    :   None
'''

# here put the import lib
# 已知坐标(x,y)，判断其所在的象限
x = int(input("请输入x的值："))
y = int(input("请输入y的值："))

# 方法1
# if x>0 and y>0:
#     print("(%d,%d)在第一象限"%(x,y))
# elif x>0 and y<0:
#     print("(%d,%d)在第四象限"%(x,y))
# elif x<0 and y>0:
#     print("(%d,%d)在第二象限"%(x,y))
# else:
#     print("(%d,%d)在第三象限"%(x,y))

# 方法2
if x>0:
    if y>0:
        print("(%d,%d)在第一象限"%(x,y))
    else:
        print("(%d,%d)在第四象限"%(x,y))
else:
    if y>0:
        print("(%d,%d)在第二象限"%(x,y))
    else:
        print("(%d,%d)在第三象限"%(x,y))