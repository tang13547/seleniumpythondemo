# coding = utf-8
from selenium import webdriver
import time

from com.youe.cd.test.util.config import config

#driver = webdriver.Chrome()
driver = webdriver.Chrome(executable_path=config.chromedriverPath)

#print("浏览器最大化")
driver.maximize_window()  #将浏览器最大化显示

driver.get("https://www.baidu.com")
time.sleep(3)

driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
time.sleep(3)

driver.quit()