import time

def youdao_search(self):
    driver = self.driver
    driver.find_element_by_id("translateContent").send_keys("selenium")
    time.sleep(2)
    driver.find_element_by_id("border").click()
    time.sleep(3)