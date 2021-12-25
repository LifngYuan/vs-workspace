#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   demo.py
@Time    :   2021/12/22 15:11:57
@Author  :   袁利锋
@Contact :   lifng.yuan@gmail.com
@Department   :  None
@Desc    :   None
'''

# here put the import lib
# 引入scrapy
import scrapy

class SpSpider(scrapy.Spider):
    name = "sp"
    allowed_domains=["spbeen.com"]
    start_urls = ["http://spbeen.com"]

    def parse(self, response,):
        # pass
        print(response.status,response.url)
