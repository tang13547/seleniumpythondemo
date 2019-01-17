from selenium import webdriver

import os,time

from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

print("浏览器最大化")
driver.maximize_window()  #将浏览器最大化显示

file_path = 'file:///' + os.path.abspath('../resources/html/drop_down.html')

driver.get(file_path)
time.sleep(3)

#先定位到下拉框
#m=driver.find_element_by_id("ShippingMethod")
#再点击下拉框下的选项
#m.find_element_by_xpath("//option[@value='10.69']").click()

select = Select(driver.find_element_by_id("ShippingMethod"))

select.select_by_index(1)
time.sleep(2)
select.select_by_value('11.61')
time.sleep(2)
select.select_by_visible_text('UPS 3 Day Select')
time.sleep(3)

driver.quit()