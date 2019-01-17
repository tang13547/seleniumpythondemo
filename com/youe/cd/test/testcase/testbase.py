from selenium import webdriver
import unittest

from com.youe.cd.test.util.initialbrowser import InitialBrowser


class TestBase(InitialBrowser):

    @classmethod
    def setUpClass(cls):
        #cls.driver = webdriver.Chrome()
        cls.browserSetUp("chrome")   #直接调用继承类InitialBrowser的静态方法

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        print("test method setUp...")
        self.driver.implicitly_wait(10)
        self.base_url = "https://www.126.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def tearDown(self):
        #self.driver.quit()
        #self.assertEqual([], self.verificationErrors)
        print("test method tearDown...")