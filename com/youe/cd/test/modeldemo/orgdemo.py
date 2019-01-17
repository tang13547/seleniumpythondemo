import unittest

# 功能函数
def multiply(a,b):
    return a * b
def setUpModule():
    print('集成测试 >>>>>>>>>>>>>>开始')
def tearDownModule():
    print("集成测试 >>>>>>>>>>>>>>结束")

class TestUM1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("Test Class Start ----->")
    @classmethod
    def tearDownClass(cls):
        print("Test Class End ----->")
    def setUp(self):
        print("setUp start=========>")
    def tearDown(self):
        print("==== END ! ====")

    #=====测试用例========
    def test_numbers(self):
        print('1test_numbers')
        self.assertEqual(multiply(5,6),30)
    def test_strings(self):
        print('2test_strings')
        assert multiply('b',2) == 'bb'

class TestUM2(unittest.TestCase):
    def test_3(self):
        print('3test_3')

if __name__ == '__main__':
    unittest.main()
