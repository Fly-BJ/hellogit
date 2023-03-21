# !/use/bin/env python
# -*- coding:utf-8 -*-
# Python Knowledge Learing
# 

from selenium import webdriver
from time import sleep
import os
from selenium.webdriver.common.by import By


class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.baidu.com')
        self.driver.maximize_window()

    def test(self):
        pass

    def test001(self):
        pass

if __name__ == '__main__':
    case = TestCase()
    case.test()
