import time

def mail_login(self, username, password):
    driver = self.driver;

    driver.switch_to.frame(0)
    driver.find_element_by_name("email").clear()
    driver.find_element_by_name("email").send_keys(username)
    driver.find_element_by_name("password").clear()
    driver.find_element_by_name("password").send_keys(password)
    driver.find_element_by_id("dologin").click()
    time.sleep(5)