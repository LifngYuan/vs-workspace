#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   test06.py
@Time    :   2022/01/05 13:31:12
@Author  :   袁利锋
@Contact :   lifng.yuan@gmail.com
@Department   :  None
@Desc    :   None
'''

# here put the import lib
# 计算最大值
'''
x=999
y=66
z=x if x>y else y
print(z)
'''

# 计算绝对值
# x=-9
# print(x if x>0 else -x)

# shiyong if biaodashi ,panduanyigeshu de jiouxing

num = int(input("input a number:"))
print(num, "是奇数" if num % 2 == 1 else "是偶数")
