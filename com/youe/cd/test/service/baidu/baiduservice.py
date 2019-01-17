import time

def baidu_search(self):
    driver = self.driver
    driver.find_element_by_id("kw").send_keys("selenium webdriver")
    driver.find_element_by_id("su").click()
    time.sleep(2)

def baidu_set(self):
    driver = self.driver
    #设置每页搜索结果为100 条
    m=driver.find_element_by_name("NR")
    m.click()
    time.sleep(2)
    m.find_element_by_xpath("//option[@value='50']").click()
    time.sleep(2)
    #保存设置的信息
    driver.find_element_by_xpath("//input[@value='保存设置']").click()
    time.sleep(2)
    driver.switch_to.alert.accept()