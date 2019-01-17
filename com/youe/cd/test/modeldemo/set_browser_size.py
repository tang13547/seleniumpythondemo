# coding = utf-8
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Chrome()

#print("浏览器最大化")
#driver.maximize_window()  #将浏览器最大化显示
print("设置浏览器宽480，高800")
driver.set_window_size(480, 800)

driver.get("https://www.baidu.com")
time.sleep(3)

#WebDriverWait()方法等待
element = WebDriverWait(driver, 10).until(lambda driver : driver.find_element_by_id("kw"))
element.send_keys("selenium")

#添加智能等待
driver.implicitly_wait(30)
#driver.find_element_by_id("su").click()   #宽不够时，搜索按钮不可见

#添加固定休眠时间
time.sleep(3)

driver.quit()