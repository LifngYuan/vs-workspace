#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   case01.py
@Time    :   2022/01/05 14:41:19
@Author  :   袁利锋
@Contact :   lifng.yuan@gmail.com
@Department   :  None
@Desc    :   None
'''

# here put the import lib
age = int(input("请输入参观游园的年龄："))

if age<3:
    price=0
elif age<18:
    price=50
elif age<60:
    price=100
else:
    price=60

print("nianlingshi:",age)
print("jiageshi:",price)