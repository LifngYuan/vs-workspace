#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   xunhuan01.py
@Time    :   2022/01/05 15:29:01
@Author  :   袁利锋
@Contact :   lifng.yuan@gmail.com
@Department   :  None
@Desc    :   None
'''

# here put the import lib
# for-in遍历循环列表
# 定义列表a
# a = [1,3,4,6,7,9,9,9]
# # 用for-in遍历
# for x in a:
#     print(x) 

# # for-in循环用enumerate遍历列表及索引
# a=["python","人工智能","大数据"]

# # 使用enumerate
# for a,b in enumerate(a):#a:index;b:name
#     print(a,b)

# 元组和列表的方法通用
# 遍历字典
# 三个方法
# items():返回字典内的key-value对
# keys():返回字典内的所有key列表
# values()：返回字典中所有value列表


#新建字典
grade={
    "zhangsan":66,
    "lisi":55,
    "wangwu":33,
    "zhaoliu":100
} 

# for-in遍历字典内的键值对
for a,b in grade.items():
    print(a,b) 

# for-in遍历字典内的key值
for c in grade.keys():
    print(c)

# for-in 遍历字典内的value值
for d in grade.values():
    print(d)