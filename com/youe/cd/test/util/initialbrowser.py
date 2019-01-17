from selenium import webdriver


class InitialBrowser():
    @classmethod
    def browserSetUp(self, browser_ = "chrome"):
        try:
            if browser_ == "chrome":
                self.driver = webdriver.Chrome()
            elif browser_ == "firefox":
                self.driver = webdriver.Firefox()
            elif browser_ == "ie":
                self.driver = webdriver.Ie()
            else:
                print("输入了错误的browser_参数，系统默认以chrome执行")
                self.driver = webdriver.Chrome()

            #return self.driver
        except Exception as e:
            print("异常信息为：%s" %e)