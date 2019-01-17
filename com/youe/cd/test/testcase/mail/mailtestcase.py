import unittest
import time
import ddt
from selenium import webdriver

from com.youe.cd.test.service.mail import mailservice
from com.youe.cd.test.testcase.testbase import TestBase
from com.youe.cd.test.util.action import elementaction
from com.youe.cd.test.util.config import config
from com.youe.cd.test.util.excelutil import ExcelUtil
from com.youe.cd.test.util.logger import Logger

filePath = "../../resources/data/testexcel.xlsx"
sheetName = "Sheet2"
test_datas = ExcelUtil(filePath, sheetName).get_dict_data()
#print(test_datas)

logger = Logger().getLogger()

@ddt.ddt
class Mail(TestBase, unittest.TestCase):


    #126邮箱登录用例(使用数据驱动ddt)
    @ddt.data(*test_datas)
    def test_mail_login(self, dicdatas):
        u"""126邮箱登录"""
        print("当前测试数据为：%s" %dicdatas)

        driver = self.driver
        #driver.get(config.base_url)
        elementaction.openPage(self, config.base_url)
        time.sleep(3)

        print("当前密码为:" + str(dicdatas["password"]))    #结果为：135470000.0 故只获取点号前面的部分，如下
        #调用服务层函数
        mailservice.mail_login(self, dicdatas["username"], str(dicdatas["password"]).split('.')[0])   #密码仅输入点号之前的部分

        #driver.get_screenshot_as_file("../../testOutput/screenshotsave/screenshot_" + nowTime + ".png")
        elementaction.getScreenshot(self, config.screenshotName)

        logger.info("mail测试log001 for info")
        logger.warn("mail测试log002 for warn")
        logger.error("mail测试log003 for error")

        actualStr = driver.find_element_by_xpath(".//*[@id='spnUid']").text
        self.assertEquals(dicdatas["username"] + "@126.com", actualStr)


if __name__ == "__main__":
    unittest.main()