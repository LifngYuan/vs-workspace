#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   ex6.py
@Time    :   2022/01/08 15:36:44
@Author  :   袁利锋
@Contact :   lifng.yuan@gmail.com
@Department   :  None
@Desc    :   None
'''

# here put the import lib
# 打印列表内的偶数
# 自定义生成一个随机列表
list=list(range(1,100))

# for-in循环
# for i in list:
#     if i %2==1:
#         continue
#     print(i)
# 输出一个列表内，所有被3整除的数
for i in list:
    if i%3 != 0:
        continue
    print(i)
