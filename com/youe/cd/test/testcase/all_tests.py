import HTMLTestRunner
import unittest

from com.youe.cd.test.testcase.baidu import baidutestcase
from com.youe.cd.test.testcase.youdao import youdaotestcase
from com.youe.cd.test.testcase.mail import mailtestcase

suite = unittest.TestSuite()

#将测试用例加入到测试容器(套件)中
suite.addTest(unittest.makeSuite(baidutestcase.Baidu))
suite.addTest(unittest.makeSuite(youdaotestcase.Youdao))
suite.addTest(unittest.makeSuite(mailtestcase.Mail))

#执行测试套件
#runner = unittest.TextTestRunner()
#runner.run(suite)

#定义个报告存放路径，支持相对路径
filename ='../report/htmlreport.html'
fs = open(filename, 'wb')  #writting & binary mode  注意：python3没有file()方法，改为open()

runner = HTMLTestRunner.HTMLTestRunner(
    stream=fs,
    title=u'HTMLTestRunner测试报告',
    description=u'用户执行情况：'
)

runner.run(suite)

