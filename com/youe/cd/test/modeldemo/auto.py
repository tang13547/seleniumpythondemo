from com.youe.cd.test.modeldemo.widget import Widget
import unittest

#执行测试的类
class WidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.widget = Widget()

    def testSize(self):
        self.assertEqual(self.widget.getSize(), (40,40))

    def testResize(self):
        self.widget.reSize(100, 100)
        self.assertEqual(self.widget.getSize(), (100, 100))

    def tearDown(self):
        self.widget = None

#构造测试集
def suite():
    suite = unittest.TestSuite()
    suite.addTest(WidgetTestCase("testSize"))
    suite.addTest(WidgetTestCase("testResize"))
    return suite

#测试
if __name__ == "__main__":
    #unittest.main(defaultTest='suite')  #方式一
    #unittest.main()   #方式一second
    #方式二
    runner = unittest.TextTestRunner()
    runner.run(suite)

