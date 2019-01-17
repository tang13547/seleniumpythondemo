from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

from com.youe.cd.test.service.youdao import youdaoservice

class Youdao(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.base_url = "http://www.youdao.com"
        self.verificationErrors = []
        self.accept_next_alert = True

    #有道搜索用例
    def test_youdao_search(self):
        u"""有道搜索"""
        driver = self.driver
        driver.get(self.base_url + "/")
        time.sleep(3)

        youdaoservice.youdao_search(self)   #调用服务层函数

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()