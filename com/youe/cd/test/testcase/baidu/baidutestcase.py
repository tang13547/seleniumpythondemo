from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
import HTMLTestRunner  #引入HTMLTestRunner 包

from com.youe.cd.test.service.baidu import baiduservice

class Baidu(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        #self.base_url = "http://www.baidu.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    #百度搜索用例
    def test_baidu_search(self):
        u"""百度搜索"""
        driver = self.driver

        driver.get(self.base_url + "/")
        time.sleep(3)

        baiduservice.baidu_search(self)   #调用服务层函数

        self.assertEquals('selenium webdriver_百度搜索', self.driver.title)

        #driver.quit()

    #百度设置用例
    def test_baidu_set(self):
        u"""百度设置"""
        driver = self.driver

        #进入搜索设置页
        driver.get(self.base_url + "/gaoji/preferences.html")
        time.sleep(2)

        baiduservice.baidu_set(self)  #调用服务层函数

        self.assertEqual(3, 3)

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    #unittest.main()
    suite = unittest.TestSuite()

    suite.addTest(Baidu("test_baidu_search"))
    suite.addTest(Baidu("test_baidu_set"))

    filename ='../report/htmlreport.html'
    fp = open(filename, 'wb')  #writting & binary mode  注意：python3没有file()方法，改为open()

    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title=u'百度搜索测试报告',
        description=u'用户执行情况：'
    )

    runner.run(suite)