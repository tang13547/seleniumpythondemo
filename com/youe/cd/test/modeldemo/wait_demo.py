# coding = utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

print("浏览器最大化")
driver.maximize_window()  #将浏览器最大化显示

driver.get("https://www.baidu.com")
time.sleep(3)

#WebDriverWait()方法等待。其中lambda为匿名函数, 如：add = lambda x, y : x+y        则add(1,2)  # 结果为3
#element = WebDriverWait(driver, 10).until(lambda driver : driver.find_element_by_id("kw"))
ele_locator = (By.ID, 'kw')
element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(ele_locator))    #注意：EC各类中的参数多为locator的元组，使用如：ele_locator = (By.ID, 'kw')
element.send_keys("selenium")

#添加智能等待
driver.implicitly_wait(30)
#driver.find_element_by_id("su").click()

#ele_locator = ('id', 'su')
driver.find_element('id', 'su').is_displayed()   #file_element()方法中不能直接使用元组locator


#添加固定休眠时间
time.sleep(3)

driver.quit()