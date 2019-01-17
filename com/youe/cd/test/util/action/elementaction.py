from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

import time


def openPage(self, url):
    self.driver.get(url)

def getScreenshot(self, filepath):
    self.driver.get_screenshot_as_file(filepath)

def implicitlyWaitFor(self, waitTime=30):
    self.driver.implicitly_wait(waitTime)

def maximizeWindow(self):
    self.driver.maximize_window()

def switchToWindow(self, i):
    pass

def switchToLastWindow(self):
    allhandles = self.driver.window_handles

    for handle in allhandles:
        self.driver.switch_to.window(handle)

def switchToFrame(self, i=0):
    self.driver.switch_to.frame(i)

def switchToDefaultFrame(self):
    self.driver.switch_to.default_content()

def isContainsPageText(self, pageText):
    allstr = self.driver.page_source

    if pageText in allstr:
        return True
    else:
        return False
    #或
    # if allstr.index(pageText) > -1:
    #     return True
    # else:
    #     return False

def isElementPresent(self, by, byPath):
    """判断元素是否存在"""
    try:
        self.driver.find_element(by, byPath)
        return True
    except NoSuchElementException as e:
        print("元素不存在异常信息为：%s" %e);
        return False

def isElementDisplayed(self, by, byPath):
    """判断元素是否显示（或隐藏）"""
    return self.driver.find_element(by, byPath).is_displayed()

def waitElementDisplay(self, locator, waitTime):
    """等待waitTime秒（建议10或30秒左右），让元素可见（相对于隐藏）
    注意：参数locator为元组
    """
    WebDriverWait(self.driver, waitTime).until(EC.visibility_of_element_located(locator))

def isAlertPresent(self):
    try:
        self.driver.switch_to.alert
        return True
    except NoAlertPresentException as e:
        print("Alert未打到异常信息为：%s" %e)
        return False

def alertConfirm(self):
    try:
        alert = self.driver.switch_to.alert
        alert.accept()
        print("Alert确认成功")
    except NoAlertPresentException as e:
        print("找不到Alert")
        raise e

def alertDismiss(self):
    try:
        alert = self.driver.switch_to.alert
        alert.dismiss()
        print("Alert取消成功")
    except NoAlertPresentException as e:
        print("找不到Alert")
        raise e

def closeAlertAndGetItsText(self, acceptNextAlert=True):
    try:
        alert = self.driver.switch_to.alert
        alertText = alert.text
        if acceptNextAlert:
            alert.accept()
        else:
            alert.dismiss()
    except NoAlertPresentException as e:
        print("找不到Alert")
        raise e

def selectByVisibleText(self, by, byPath, text):
    try:
        select = Select(self.driver.find_element(by, byPath))
        select.select_by_visible_text(text)
    except NoSuchElementException as e:
        print("找不到下拉值，选择下拉列表失败，Text为：" + text)
        raise e

def selectByValue(self, by, byPath, value):
    try:
        select = Select(self.driver.find_element(by, byPath))
        select.select_by_value(value)
    except NoSuchElementException as e:
        print("找不到下拉属性名value的值，选择下拉列表失败，属性value的值为：" + value)
        raise e

def selectByIndex(self, by, byPath, index):
    try:
        select = Select(self.driver.find_element(by, byPath))
        select.select_by_index(index)
    except NoSuchElementException as e:
        print("找不到下拉列表索引index，选择下拉列表失败，index为：" + index)
        raise e

def moveToElement(self, by, byPath):
    """鼠标移动到元素"""
    actions = ActionChains(self.driver)
    actions.move_to_element(self.driver.find_element(by, byPath)).perform()

def moveToElementbyElement(self, element):
    """鼠标移动到元素"""
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()

def clickAndHold(self, by, byPath):
    """鼠标悬停操作"""
    actions = ActionChains(self.driver)
    actions.click_and_hold(self.driver.find_element(by, byPath)).perform()

def clickLeft(self, by, byPath):
    """鼠标左击(通过ActionChains类）操作"""
    actions = ActionChains(self.driver)
    actions.click(self.driver.find_element(by, byPath)).perform()

def clickRight(self, by, byPath):
    """鼠标右击(通过ActionChains类）操作"""
    actions = ActionChains(self.driver)
    actions.context_click(self.driver.find_element(by, byPath)).perform()

def clickDouble(self, by, byPath):
    """鼠标双击(通过ActionChains类）操作"""
    actions = ActionChains(self.driver)
    actions.double_click(self.driver.find_element(by, byPath)).perform()

def checkBoxCheckAll(self, by, byPath):
    """通过By by定位一组元素(复选框)，并全选"""
    checkBoxs = self.driver.find_elements(by, byPath)

    try:
        for checkBox in checkBoxs:
            checkBox.click()
            time.sleep(2)
    except KeyboardInterrupt as e:
        print("KeyboardInterrupt异常信息为：%s" %e)
        raise

def waitPageLoadComplete(self, waitTime):
    WebDriverWait(self.driver, waitTime).until(lambda self:True if self.driver.execute_script("return document.readyState") == "complete" else False)

def executeJS(self, js):
    """
    执行JS语句，常用js如下：
    js = "window.scrollTo(100,450);"  移动到指定位置
    js = "window.scrollTo(0,0)"  移动到顶部
    js = "window.scrollTo(0,document.body.scrollHeight)"   移动到底部
    js = "return document.readyState"   对应的结果是: complete
    js = "alert(\"This is your js alert!\")"  ?
    :param self: driver
    :param js: javascript语句
    :return:
    """
    self.driver.execute_script(js)