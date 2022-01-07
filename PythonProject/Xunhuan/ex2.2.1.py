#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   ex2.2.1.py
@Time    :   2022/01/07 11:37:08
@Author  :   袁利锋
@Contact :   lifng.yuan@gmail.com
@Department   :  None
@Desc    :   None
'''

# here put the import lib

a = range(1,10,2)#生成可迭代对象a，以1为初始值，10为终止值，步长的2
print(a)
# range(1, 10, 2)
b = list(a)#把a转换成一个列表
print(b)
# [1, 3, 5, 7, 9]

c = range(1,5)#默认步长为1
print(list(c))
# [1, 2, 3, 4]

d = range(5)#默认从0开始，到5结束（不包含5），步长为1
print(list(d))
# [0, 1, 2, 3, 4]

# for-in 循环
for i in range(1,5):
    # print(i,end=" ")
    # 1 2 3 4
    print(i,"haha",end=" ")
    # 1 haha 2 haha 3 haha 4 haha