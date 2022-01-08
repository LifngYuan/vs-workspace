#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   ex5.py
@Time    :   2022/01/08 14:45:00
@Author  :   袁利锋
@Contact :   lifng.yuan@gmail.com
@Department   :  None
@Desc    :   None
'''

# here put the import lib
# # 列表内是否存在0

# # 定义一个随机生成的列表
# list=list(range(-1,10))
# # print(list)
# # 定义初始值标记为0
# flag=0

# n=0#n表示循环次数，每执行一次增加1
# # 使用for-in循环遍历
# for i in list:
#     print("这是执行的第",n,"次")
#     if i == 0:
#         flag=1#如果遍历到有0的值，flag就等于1
#         break
#     n+=1

# 判断是否存在0
# if flag ==1:
#     print("list列表中存在0")
# else:
#     print("list列表中不存在0")


# 使用break，判断一个列表内，是否存在奇数。

# 初始化一个自定义列表
list = list(range(2,8))
# 定义初始化标记为0
flag = 0

# 使用for-in循环遍历，遇到存在奇数flag=1，使用break跳出for-in循环
for i in list:
    if i%2==1:
        flag=1
        break

# 判断标记的值，确定列表中是否存在奇数
if flag==1:
    print("列表内存在奇数")
else:
    print("列表内不存在奇数")

