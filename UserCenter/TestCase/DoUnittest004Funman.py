import unittest
import warnings
from tools_1.BaseDriver import  driver
from tools_2.Login_Page import LoginPage
from tools_2 import Funman_Page

class TestFunds(unittest.TestCase,LoginPage):

    @classmethod
    # 执行第一个用例前执行
    def setUpClass(cls):
        # 解决错误 ResourceWarning: Enable tracemalloc to get the object allocation traceback
        warnings.simplefilter('ignore', ResourceWarning)
        print('---test start!---')

    @classmethod
    # 执行所有用例之后执行
    def tearDownClass(cls):
        cls.driver = driver
        cls.driver.quit()
        print('---test end!---')

    def test_fun_man_1(self):
        lp = LoginPage(driver)
        lp.Login('13066660018','qwer1234')
        message = Funman_Page.fun_man_1()
        self.assertEqual(message,'一键购买')
        print('资金管理用例1执行完成')

    def test_fun_man_2(self):
        message = Funman_Page.fun_man_2()
        self.assertEqual(message,'出金申请已提交，请耐心等待...')
        print('资金管理用例2执行完成')

    def test_fun_man_3(self):
        message = Funman_Page.fun_man_3()
        self.assertEqual(message,'25')
        print('资金管理用例3执行完成')

if __name__ == '__main__':
    unittest.main(verbosity=2)
