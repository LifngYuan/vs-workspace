#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   函数_作用域.py
@Time    :   2022/06/29 17:17:57
@Author  :   袁利锋
@Contact :   lifng.yuan@gmail.com
@Department   :  None
@Desc    :   None
'''

# here put the import lib

#例子1

""" def talk():
  message = "CSDN挺好的!"
  print(message)  #message 是方法talk（）的局部变量


talk()
# print(message)  在函数体内定义的message，它的作用范围仅限于函数体内；离开了函数体，其中的变量就消失了
# NameError:name 'message' is not defind 输出结果 """
# 修改后：
message = "我是最棒的！"
def talk():
  print(message)

talk()
print(message)